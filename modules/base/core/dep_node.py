'''
/*****************************************************************************/
                        Dependency Node (DEP Node) v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Our Dep Node functionality to deal with Maya base Nodes
    with no object dependency. (Utility nodes [multiplyDivide, etc])

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Dep_Node [Class]

>> NOTES >> 
	Update 02/08/2023 : Start working on the script
    Update 03/08/2023 : Improved documentation
 
>> THANKS >> 
    Nick Hughes [02/08/2023]:
        For his awesome course that led me to create this file.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.utils import open_maya_api, path
from modules.base.core.attribute_base import Attributes
from modules.base.core.dag_dimension import Object_Dimension

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Dep_Node(object):
    """
    Dep_Node [Class]

    Class based way of calling the information that we need
    to deaal with Maya Base nodes with no object dependency.

    Args:
        node (node/str) :   Takes either a ready-made base node or the name 
                            of one to create. You can use m commands here.
        nodeType (str)  :   Used for creating a specified node type. (optional)

    Returns:
        Object: The OpenMaya Dependency Object.

    Example:
        cube = Dep_Node(m.polyCube(n = cube))
        dep = Dep_Node("node_001")
        dep.rename("footbar_001")
        dep.delete()
    """

    def __init__(self, node, nodeType=None):
        self._dep = None
        self.node = node

        # Create on initiate if nodeType is passed
        if nodeType and not self.exists():
            self.create(nodeType)

    def __str__(self):
        fullPath = self.fullPath
        if not fullPath:
            return "INVALID OBJECT"
        return fullPath

    def __repr__(self):
        return path.generateReprString(
            self.__class__.__name__,
            self.fullPath )

    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __eq__(self, other):
        """ Compares TWO class objects to see if they are the same Object. """
        if isinstance(other, self.__class__):
            return self.fullPath == other.fullPath
        elif self.fullPath == other:
            return True
        elif self.path == other:
            return True

        return False

    # -------------------------------------------------------------------------
    # GETTER AND SETTER

    @property
    def node(self):  # Getter - Gets the current node.
        return self._node

    @node.setter
    def node(self, node):  # Setter - Set a new node.
        self._dep = None
        self._node = str(node) if node != None else None

        if not self.node or not m.objExists(self.node):
            return False

        self._dep = open_maya_api.toDpendencyNode(self.node)
        
        return True

    # -------------------------------------------------------------------------
    # PROPERTIES

    @property
    def dep(self):
        return self._dep

    @property
    def path(self):
        """ Returns object name. """
        if self.dep:
            return self.dep.name()

    @property
    def fullPath(self):
        """ Returns object name. """
        return self.path

    @property
    def type(self):
        """ Returns object typeName, example: "joint" """
        return self.dep.typeName()

    @property
    def typ(self):
        """ Returns object type. """
        return self.type

    @property
    def name(self):
        """ Returns object name. """
        return path.baseName(self.fullPath)

    @property
    def namespace(self):
        return path.namespace(self.fullPath)

    @property
    def isLocked(self):
        """ Returns state of the object. """
        return m.lockNode(self.fullPath, query=True, lock=True)[0]

    # -------------------------------------------------------------------------

    @property
    def a(self):  # For us to call atributes with "a"
        """
        Stands for attributes!

        Returns:
            class obj: Attributes
        """
        return Attributes(self)

    @property
    def o(self):
        """
        Stands for Object dimension.

        Returns:
            class obj: Object Dimension.
        """
        return Object_Dimension(self)

    # -------------------------------------------------------------------------
    # METHODS

    def isReferenced(self):
        """
        Checks if the object is Referenced

        Returns:
            Bool: isNodeReferenced
        """
        return m.referenceQuery(
            self.fullPath,
            isNodeReferenced=True
        )

    def exists(self):
        """
        Checks if the object exists

        Returns:
            Bool: objExists
        """
        if self.fullPath and m.objExists(self.fullPath):
            return True
        return False

    def rename(self, name):
        """
        Renames obj with given string.

        Args:
            name (str): New name of the object.

        Returns:
            self: The obj __repr__ method.
        """
        m.rename(self, name)
        return self

    def lock(self, state=True):
        """
        Locks or unlocks a node Obj.

        Args:
            state (bool): Locks or unlocks the Obj. Defaults to True.
        """
        m.lockNode(self.fullPath, lock=state)

    def unlock(self):
        """ Unlocks the object. """
        self.lock(0)

    def delete(self):  # Deletes the obj in scene but not the class obj
        """ Deletes the obj in scene but not the class obj. """
        if self.fullPath and m.objExists(self.fullPath):
            m.delete(self.fullPath)
        self._dep = None

    def create(self, nodeType):
        """
        Creates an object if it doesn't already exists.

        Args:
            nodeType (str): The node type, example "multiplyDivide"

        Raises:
            ValueError: if obj already exists.

        Returns:
            self: the __repr__ of the object.
        """
        if self.fullPath:
            txt = """>>> This node already exists: 
            \n\tName: \"{}\"\n\tType: {}""".format(self.node, nodeType)
            raise ValueError(txt)

        self.node = m.createNode(nodeType, n=self.node)
        return self

    def hideNode(self, value = 0):
        """ Hides node from channelBox (isHistoricallyInteresting)"""
        self.a.isHistoricallyInteresting.set(value)
        return self