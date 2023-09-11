'''
/*****************************************************************************/
                            DAG Base v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Our Dag Node functionality to deal with Maya Nodes
    with or without object dependency.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Dag_Base [Class]

>> NOTES >> 
	Update 03/08/2023 : Start working on the script
    Update 10/09/2023 : Added batch channel attributes manipulation  
 
>> THANKS >> 
    Nick Hughes [03/08/2023]:
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
from modules.base import Dep_Node
from modules.utils import color, open_maya_api
from modules.utils.common import createOffset
from modules.utils.common import matchMove
from modules.common.functions import getKeyFromValue
from modules.common.names import ROTATE_ORDER_DICT

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Dag_Node(Dep_Node):
    """
    Dag_Base [Class] (Inherits from: Dep_Node) [Previously Dag_Node]

    Class based way of calling the information that we need to deal 
    with Maya Base nodes with dependency in a clean Python way.

    Args:
        node (node/str) :   Takes either a ready-made base node or the name 
                            of one to create. You can use m commands here.
        nodeType (str)  :   Used for creating a specified node type. (optional)

    Returns:
        Object: The OpenMaya Dependency Object.

    Example:
        cube = Dag_Node(m.polyCube(n = cube))
        dag = Dag_Node("node_001")
        dag.rename("footbar_001")
        print(dag.fullPath)
    """
    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node, nodeType=None):
        self._dag = None

        Dep_Node.__init__(self, node)  # Needs to be initialize after Dag

        # Create on initiate if nodeType is passed
        if nodeType:
            self.create(nodeType)

    # -------------------------------------------------------------------------
    # GETTER AND SETTER

    @property
    def node(self):  # Getter - Gets the current node.
        return self._node

    @node.setter
    def node(self, node):  # Setter - Set a new node.
        self._dag = None  # from node to None

        if not Dep_Node.node.fset(self, node):
            return False

        self._dag = open_maya_api.toMDagPath(self.node)

        return True

    # ----------------------------------------------------------------

    @property
    def dag(self):  # Returns the Open Maya mDag path associated with the node.
        return self._dag

    # ----------------------------------------------------------------

    @property
    def path(self):
        if self.dag:
            return self.dag.partialPathName()
        else:
            return Dep_Node.path.fget(self)

    @property
    def fullPath(self):
        if self.dag:
            return self.dag.fullPathName()
        else:
            return Dep_Node.fullPath.fget(self)

    # ----------------------------------------------------------------

    @property
    def shapes(self):
        shapes = []
        for shape in m.listRelatives(self.fullPath, s=True, f=True, ni=True) or []:
            shapes.append(Dag_Node(shape))

        return shapes

    @property
    def shape(self):
        shapes = self.shapes

        return shapes[0] if len(shapes) else Dag_Node(None)

    # ----------------------------------------------------------------

    @property
    def children(self):
        children = []
        shapes = self.shapes

        for child in m.listRelatives(self.fullPath, c=True, f=True, ni=True) or []:
            if child not in shapes:
                children.append(Dag_Node(child))

        return children

    @property
    def allChildren(self):
        children = []
        for child in m.listRelatives(self.fullPath, ad=True, f=True, ni=True) or []:
            children.append(Dag_Node(child))

        return children

    @property
    def parent(self):
        parent = m.listRelatives(self.fullPath, p=True, f=True)

        if parent:
            return Dag_Node(parent[0])

    @property
    def allParents(self):
        parents = []
        parent = self.parent

        while parent:  # Cycle until no parent is found
            parents.append(parent)
            parent = parent.parent  # Get the parent of the parent

        return parents

    # ----------------------------------------------------------------

    @property
    def order(self):
        """
        Get your current index, by checking first your parent node
        then, get the children of that node, index all the children,
        and outputting your index number

        Returns:
            int: Index number of our obj.
        """
        return self.parent.children.index(self)

    def reorder(self, index):
        """
        Set the index number of obj

        Args:
            index (int): Set the index number
        """
        m.reorder(self.name, r=index)

    # ----------------------------------------------------------------

    def parentTo(self, item):
        """
        Parents obj to another obj

        Args:
            item (obj, str): The object to become parent
        """
        m.parent(self.fullPath, item)

    def parentToWorld(self):
        """ Parent obj to world """
        m.parent(self.fullPath, w=True)

    def moveTo(self, item):
        """
        Match transformations of our obj to another

        Args:
            item (obj): The object to match.
        """
        matchMove([Dag_Node(item).name, self.fullPath])

    def moveHere(self, items):
        """
        Match transformations of our obj to other objs.

        Args:
            items (list): The objects to match.
        """
        matchMove([self.fullPath] + [Dag_Node(i).name for i in items])

    # ----------------------------------------------------------------

    @property
    def offset(self):
        return self.parent

    def createOffset(self, count=1):
        """
        Create Offset groups for our obj

        Args:
            count (int): Number of groups to create. Defaults to 1.

        Returns:
            offsetName: The name of our offset group
        """
        if self.exists():
            for i in range(count):
                offsetName = createOffset([self.name])

            return Dag_Node(offsetName)

    # ----------------------------------------------------------------

    @property
    def color(self):
        return color.getColor(self.fullPath)

    @property
    def colorAsString(self):
        if self.color is None:
            return None
        
        return color.getColorFromInteger(self.color)

    def setColor(self, value):
        """ Set the override color of our object """
        color.setColor(self.fullPath, value)

        return self

    # ----------------------------------------------------------------

    @property
    def history(self):
        """ Returns obj construction history. """
        if self.exists():
            history = [Dag_Node(i) for i in m.listHistory(self.fullPath)]
            return history
        
        return []

    def deleteHistory(self):
        """ Deletes obj construction history. """
        if self.exists():
            m.delete(self.fullPath, ch=1)

    def duplicate(self, **kwargs):
        """
        Duplicates the obj, method accepts maya **kwargs
        """
        if not self.exists():
            raise ValueError(">>> No maya node to duplicate")

        return Dag_Node(m.duplicate(self.fullPath, **kwargs)[0])
    
    # -------------------------------------------------------------------------
    # CONSTRAINTS

    def _getConstraint(self, constraintType):
        """
        Gathers the requiered type of constraints

        Args:
            constraintType (Str): The type of constraint.

        Returns:
            Obj: The constraints connected to our object.
        """
        constraints = m.listConnections(
            self.fullPath, s=True, d=False, t=constraintType)

        return Dag_Node(constraints[0] if constraints else Dag_Node(None))

    @property
    def getGeometryConstraint(self):
        return self._getConstraint("geometryConstraint")

    @property
    def getAimConstraint(self):
        return self._getConstraint("aimConstraint")

    @property
    def getOrientConstraint(self):
        return self._getConstraint("orientConstraint")

    @property
    def getPointConstraint(self):
        return self._getConstraint("pointConstraint")

    @property
    def getParentConstraint(self):
        return self._getConstraint("parentConstraint")

    @property
    def getScaleConstraint(self):
        return self._getConstraint("scaleConstraint")

    def constraintWeightingAttributes(self, constraintType):
        """
        Not using the maya parentConstraint python as it does not pick up
        name changes

        Args:
            constraintType (Str): The type of constraint.

        Returns:
            Obj List: The list of weights of the constraints connected to our object.
        """
        constraint = self._getConstraint(constraintType)

        return [constraint.fullPath + "." + i for i in
                m.listAttr(constraint, k=1, c=1) if "W" in (i[-2] or i[-3])]

    def geometryConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example
            sphere.c.geometryConstraint("pCube1", mo=True)
        """
        return Dag_Node(m.geometryConstraint(self.fullPath, *args, **kwargs)[0])

    def aimConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example:
            sphere.c.aimConstraint("pCube1", mo=True)
        """
        return Dag_Node(m.aimConstraint(self.fullPath, *args, **kwargs)[0])

    def orientConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example:
            sphere.c.orientConstraint("pCube1", mo=True)
        """
        return Dag_Node(m.orientConstraint(self.fullPath, *args, **kwargs)[0])

    def pointConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example:
            sphere.c.pointConstraint("pCube1", mo=True)
        """
        return Dag_Node(m.pointConstraint(self.fullPath, *args, **kwargs)[0])

    def parentConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example:
            sphere.c.parentConstraint("pCube1", mo=True)
        """
        return Dag_Node(m.parentConstraint(self.fullPath, *args, **kwargs)[0])

    def scaleConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example:
            sphere.c.scaleConstraint("pCube1", mo=True)
        """
        return Dag_Node(m.scaleConstraint(self.fullPath, *args, **kwargs)[0])

    def parentScaleConstraint(self, *args, **kwargs):
        """
        Creates a constraint, you can parse Maya arguments to the method

        Example:
            sphere.c.parentScaleConstraint("pCube1", mo=True)
        """
        m.scaleConstraint(self.fullPath, *args, **kwargs)

        return Dag_Node(m.parentConstraint(self.fullPath, *args, **kwargs)[0])

    # -------------------------------------------------------------------------
    # DISPLAY OPTIONS

    # ---- VISIBILITY ------
    
    def setVisibility(self, value):
        """
        Set the visibility attribute of our object

        Args:
            value (bool): Visibility value
        """
        if self.exists():
            m.setAttr("{item}.v".format(item=self.fullPath), value)

    def show(self):
        """ Set obj visibility to 1 """
        self.setVisibility(1)

    def hide(self):
        """ Set obj visibility to 0 """
        self.setVisibility(0)

    # ---- HANDLE ------

    @property
    def handle(self):
        handle = self.a.displayHandle.get()

        return handle

    def setHandle(self, value):
        """
        Set the handle visibility of our object

        Args:
            value (bool): Visibility value
        """
        if self.exists():
            self.a.displayHandle.set(value)

    def showHandle(self):
        self.setHandle(1)

    def hideHandle(self):
        self.setHandle(0)

    # ---- LOCAL AXIS ------

    @property
    def localAxis(self):
        localAxis = self.a.displayLocalAxis.get()
        return localAxis

    def setLocalAxis(self, value):
        """
        Set the local axis visibility of our object
        
        Args:
            value (bool): Visibility value
        """
        if self.exists():
            self.a.displayLocalAxis.set(value)

    def showLocalAxis(self):
       self.setLocalAxis(1)

    def hideLocalAxis(self):
        self.setLocalAxis(0)

    # -------------------------------------------------------------------------
    # TRANSFORM OPTIONS

    # ---- ROTATE ORDER ------

    @property
    def rotateOrder(self):
        rotOrder = self.a.rotateOrder.get()
        rotOrder = getKeyFromValue(ROTATE_ORDER_DICT, rotOrder)
        return rotOrder

    def setRotateOrder(self, value):
        """
        setRotateOrder of the object.

        Args:
            value (int/str): the rotation order
            
        Example:
            setRotateOrder(1) / setRotateOrder('xyz')
        """
        if isinstance(value, str):
            if value.lower() in ROTATE_ORDER_DICT:
                order = ROTATE_ORDER_DICT[value]
                self.a.rotateOrder.set(order)
            else:
                raise ValueError(
                    ">>> Sorry but the rotateOrder name you entered was not found")

        elif isinstance(value, int) and value in range(0, 6):
            self.a.rotateOrder.set(value)

        else:
            raise TypeError(
                ">>> Please pass either the number or name of the rotationOrder")

        return self.rotateOrder
    
    # ---- ATTRIBUTE BATCH MANIPULATION ------

    def lockAll(self):
        self.a.t.lock()
        self.a.r.lock()
        self.a.s.lock()
        self.a.v.lock()

    def unlockAll(self):
        self.a.t.unlock()
        self.a.r.unlock()
        self.a.s.unlock()
        self.a.v.unlock()

    def hideAll(self):
        self.a.t.hide()
        self.a.r.hide()
        self.a.s.hide()
        self.a.v.hide()

    def showAll(self):
        self.a.t.show()
        self.a.r.show()
        self.a.s.show()
        self.a.v.show()

    def lockHideAll(self):
        self.a.t.lockHide()
        self.a.r.lockHide()
        self.a.s.lockHide()
        self.a.v.lockHide()
   
    def unlockShowAll(self):
        self.a.t.unlockShow()
        self.a.r.unlockShow()
        self.a.s.unlockShow()
        self.a.v.unlockShow()
    