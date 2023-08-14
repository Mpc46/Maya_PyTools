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
from modules.nodel.base.attribute_base import Attributes
from modules.nodel.base.dag_dimension import Object_Dimension

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

    Contents:
    - SPECIAL METHODS:
        + __str__ [Returns the fullPath of the object]
        + __repr__ [Returns the class of the object and it's full Path]
        + __eq__ [Compares TWO class objects to see if they are the same Obj]

    - PROPERTIES:
        + dep [Returns the Object]
        + path [Returns the obj path]
        + fullPath [Returns the obj fullPath]
        + type [Returns the obj type]
        + name [Returns the obj name]
        + namespace [If any, returns obj namespace]
        + isLocked [Returns the state of the obj]

    - METHODS:
        + isReferenced [Checks if obj is reference, returns Bool]
        + exists [Checks if obj exists, returns Bool]
        + rename [Renames the object, returns self]
        + lock [Locks or Unlocks a node, protecting it]
        + delete [Deletes the objects from scene, not the class.obj itself]
        + create [Creates a node object if it doesn't exist]

    """

    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

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
            self.fullPath,
        )

    def __eq__(self, other):
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
        if self.dep:
            return self.dep.name()

    @property
    def fullPath(self):
        return self.path

    @property
    def type(self):
        return self.dep.typeName()

    @property
    def typ(self):
        return self.type

    @property
    def name(self):
        return path.baseName(self.fullPath)

    @property
    def namespace(self):
        return path.namespace(self.fullPath)

    @property
    def isLocked(self):
        return m.lockNode(self.fullPath, query=True, lock=True)[0]
    
    # -------------------------------------------------------------------------

    @property
    def a(self): # For us to call atributes with "a"
        """
        a [Property]

        Stands for attributes!

        Returns:
            class obj: Attributes
        """
        return Attributes(self)

    @property
    def o(self):
        """
        o [Property]

        Stands for Object dimension.

        Returns:
            class obj: Object Dimension.
        """
        return Object_Dimension(self)

    # -------------------------------------------------------------------------
    # METHODS

    def isReferenced(self):
        """
        isReferenced [Method]

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
        exists [Method]

        Checks if the object exists

        Returns:
            Bool: objExists
        """
        if self.fullPath and m.objExists(self.fullPath):
            return True
        return False

    def rename(self, name):
        """
        rename [Method]

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
        lock [Method] 

        Locks or unlocks a node Obj.

        Args:
            state (bool): Locks or unlocks the Obj. Defaults to True.
        """
        m.lockNode(self.fullPath, lock=state)

    def delete(self):  # Deletes the obj in scene but not the class obj
        """
        delete [Method]

        Deletes the obj in scene but not the class obj
        """
        if self.fullPath and m.objExists(self.fullPath):
            m.delete(self.fullPath)
        self._dep = None

    def create(self, nodeType):
        """
        create [Method]

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
