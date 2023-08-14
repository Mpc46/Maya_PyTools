'''
/*****************************************************************************/
                        Attribute Base Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Our Dag Node functionality to deal with Maya attributtes
    in a simple and Pythonic way.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Attributes [Class]
    + Attribute [Class]

>> NOTES >> 
	Update 05/08/2023 : Start working on the script
    Update 06/08/2023 : Created Arithmetic methods for nodes
 
>> THANKS >> 
    Nick Hughes [5/08/2023]:
        For his awesome course that led me to create this file. 

>> CONTACT >>
    luisf.carranza@outlook.com ←or→ https://mpc46.carrd.co
    Copyright (C) 2023 Luis Carranza. All rights reserved.
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.utils import path
import string, six

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Attributes(object):
    """
    Attributes [Class]

    Class based way of calling the information that we need to deal 
    with Maya attributes nodes with dependency in a clean Python way.

    Args:
        object (obj): The DAG object to get/set attributes from.

    Raises:
        ValueError: If obj or node doesn't exist

    Returns:
        Object: The attribute object of our object.

    Contents:
    - SPECIAL METHODS:
        + __repr__ [Returns a string representation of our obj]
        + __getitem__ [Returns string representation of our attr]
        + __getattr__ [Returns string representation of our attr]

    - METHODS:
        + list [Returns a list of all attributes]
        + add [Adds an attribute to the current node]
        + zeroAttributes [Zero out all transform attributes]
    """
    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node):
        self.node = node

        if not node.exists():
            raise ValueError("Node does not exist: {}".format(node.name))

    def __repr__(self):
        return path.generateReprString(
            self.__class__.__name__,
            self.node.fullPath,
        )

    def __getitem__(self, attr):
        """
        __getitem__ [Special Method]

        Getting the attribute with a string input.

        Args:
            item (str): The attribute to get.

        Example:
            print(cube.a["rotateX"])
            # Output: "|cube_GEO.rotateX"
        """
        if attr in self.__dict__.keys():
            return self.__dict__[attr]

        return Attribute(self.node, attr)

    def __getattr__(self, attr):
        """
        __getattr__ [Special Method]

        Getting the attribute with a string input.

        Args:
            item (str): The attribute to get.

        Example:
            print(cube.a.rotateX)
            # Output: "|cube_GEO.rotateX"
        """
        if attr in self.__dict__.keys():
            return self.__dict__[attr]

        return Attribute(self.node, attr)

    # -------------------------------------------------------------------------
    # METHODS

    def list(self, **kwargs):
        """
        list [Method]

        Using maya.m functionality to list all attributes.

        Example:
            print(cube.a.list())
            # Output: list
        """
        return [
            Attribute(self.node, a)
            for a in m.listAttr(self.node, **kwargs)
        ]

    def add(self, **kwargs):
        """
        add [Method]

        Using functionality from maya.m addAttr to add
        an attribute to the current node.

        Args:
            longName (str): Fixed code name
            nn (str): Human redable name
            at (str): attributeType: Type, Long, float, enum
            en (str): "__________:__________"
            dv (int/float):  Default Value to set
            min (int/float): Min value to go to
            max (int/float): Max value to go to
            k (int): Keyable
            h (bool): Hidden

        Example:
            cube.a.add(ln="new_attr", nn="New Attr", at="float", k=1, dv=0)
            # Access new attribute:
                cube.a_new_attr >> sphere.a.rx # Connecting attributes
        """
        m.addAttr(self.node, **kwargs)

    def zeroAttributes(self, **kwargs):
        """
        zeroAttributes [Method]

        Zero's out the transform attributes of the node

        Example:
            cube.a.zeroAttributes()
        """
        m.makeIdentity(self.node.fullPath, **kwargs)


class Attribute(object):
    """
    Attribute [Class] (Inherits from: Dag_Node)

    Class based way of calling the information that we need to deal 
    with a Maya attribute node in a clean Pythonic way.

    Args:
        object (obj): The DAG object to get/set attribute from.

    Returns:
        Object: The attribute object of our object.

    Contents:
    - SPECIAL METHODS:
        + __str__ [Return fullPath of our obj] (str(obj))
        + __repr__ [Returns string representation of our obj] (obj)
        + __lshift__ [Connects Attr from A to B] ( A >> B)
        + __rshift__ [Connects Attr from B to A] ( A << B)

    - PROPERTIES:
        + attr [Returns obj attribute string]
        + attribute [Returns obj attribute string]
        + path [Returns obj attribute string path with node name and attr]
        + fullPath [Returns obj attribute string fullPath with node name and attr]
        + children [Returns a list of the children attributes if any]
        + parent [Returns a list of the parent attributes if any]
        + outputs [Returns all the outputs of an attribute]
        + connectionInput [Returns the input connection of an attribute]
        + connectionOutputs [Returns all output connections of an attribute]

    - METHODS:
        + exists [Checks wether our attribute exists]
        + set [Sets our attribute using functionality from maya.m]
        + get [Gets our attribute value using functionality from maya.m]
        + query [Query's our attribute value using functionality from maya.m]
        + connect [Connects this attribute to the passed item.] (>> and <<)
        + disconnect [Disconnects the attribute if connected]
        + delete [Deletes the attribute]
    """
    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node, attr):
        self.node = node
        self._attribute = attr

    def __str__(self):
        fullPath = self.fullPath
        if not fullPath:
            return ">>> INVALID OBJECT"
        return fullPath

    def __repr__(self):
        return path.generateReprString(
            self.__class__.__name__,
            self.fullPath,
        )

    def __lshift__(self, attr):
        """
        __lshift__ [Special Method]

        Connecting from the last item to the first.

        Example:
            node2.a.sx << node1.a.sy
        """
        attr.connect(self)

    def __rshift__(self, attr):
        """
        __lshift__ [Special Method]

        Connecting from the first item to the last.

        Example:
            node1.a.sx >> sphere_GEO.rotateX
        """
        self.connect(attr)

    # -------------------------------------------------------------------------
    # CONDITION NODES

    def _conditionNodeName(self, value):
        return value.node.name if isinstance(value, type(self)
                                             ) else self.node.name + "_" + str(value)

    def __eq__(self, value):  # ==
        """
        __eq__ [Special Method] (Equal, ==)

        Making a condition node and setting the first & second terms and operation.

        Example:
            node1.a.sx == node2.a.sx
        """
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition

        name = self._conditionNodeName(value)
        nodeName = "{0}_{1}_eq_CD".format(name, self.attr)

        # Returns nodeName, firstTerm, secondTerm, operation (0 = eq)
        return Condition(nodeName, self, value, 0).a.outColorR

    def __ne__(self, value):  # !=
        """
        __ne__ [Special Method] (NotEqual, !=)

        Making a condition node and setting the first & second terms and operation.

        Example:
            node1.a.sx != node2.a.sx
        """
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition

        name = self._conditionNodeName(value)
        nodeName = "{0}_{1}_ne_CD".format(name, self.attr)

        # Returns nodeName, firstTerm, secondTerm, operation (1 = ne)
        return Condition(nodeName, self, value, 1).a.outColorR

    def __gt__(self, value):  # >
        """
        __gt__ [Special Method] (Greater Than, >)

        Making a condition node and setting the first & second terms and operation.

        Example:
            node1.a.sx > node2.a.sx
        """
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition

        name = self._conditionNodeName(value)
        nodeName = "{0}_{1}_gt_CD".format(name, self.attr)

        # Returns nodeName, firstTerm, secondTerm, operation (2 = gt)
        return Condition(nodeName, self, value, 2).a.outColorR

    def __ge__(self, value):  # >=
        """
        __ge__ [Special Method] (Greater Than or equal, >=)

        Making a condition node and setting the first & second terms and operation.

        Example:
            node1.a.sx >= node2.a.sx
        """
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition

        name = self._conditionNodeName(value)
        nodeName = "{0}_{1}_ge_CD".format(name, self.attr)

        # Returns nodeName, firstTerm, secondTerm, operation (3 = ge)
        return Condition(nodeName, self, value, 3).a.outColorR

    def __lt__(self, value):  # <
        """
        __lt__ [Special Method] (Less than, <)

        Making a condition node and setting the first & second terms and operation.

        Example:
            node1.a.sx < node2.a.sx
        """
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition

        name = self._conditionNodeName(value)
        nodeName = "{0}_{1}_lt_CD".format(name, self.attr)

        # Returns nodeName, firstTerm, secondTerm, operation (4 = lt)
        return Condition(nodeName, self, value, 4).a.outColorR

    def __le__(self, value):  # <=
        """
        __le__ [Special Method] (Less or Equal, <=)

        Making a condition node and setting the first & second terms and operation.

        Example:
            node1.a.sx <= node2.a.sx
        """
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition

        name = self._conditionNodeName(value)
        nodeName = "{0}_{1}_le_CD".format(name, self.attr)

        # Returns nodeName, firstTerm, secondTerm, operation (5 = le)
        return Condition(nodeName, self, value, 5).a.outColorR

    def setCondition(self, **kwargs):
        # Importing here to avoid circular dependency
        from modules.nodel.base.attribute_condition import Condition
        return Condition(self.node).setCondition(**kwargs)

    # -------------------------------------------------------------------------
    # ARITHMETRIC NODES - OPERATIONS

    def __add__(self, value):
        """
        __add__ [Special Method] (+)

        Using the plusMinus node for the connections

        Example:
            calc = (node.a.sx + node.a.sy)
        """
        return self.plusMinusAverageNode(value)

    def __sub__(self, value): ###123 (makes it easier to search within our code)
        """
        __sub__ [Special Method] (-)

        Substracting the value passed or attribute

        Example:
            calc = node.a.sx - node.a.sy
        """
        return self.plusMinusAverageNode(value, operationType=2)

    def __mul__(self, value):
        """
        __mul__ [Special Method] (*)

        Multiplying the value passed or attribute

        Example:
            calc = node.a.sx * node.a.sy
        """
        return self.multiplyDivideNode(value, operationType=1)

    def __div__(self, value):
        """
        __div__ [Special Method] (/)

        Dividing the value passed or attribute

        Example:
            calc = node.a.sx / node.a.sy
        """
        return self.multiplyDivideNode(value, operationType=2)

    def __truediv__(self, value):
        """
        __truediv__ [Special Method] (/)

        Dividing the value passed or attribute

        Example:
            calc = node.a.sx / node.a.sy
        """
        return self.multiplyDivideNode(value, operationType=2)

    def __pow__(self, value):
        """
        __pow__ [Special Method] (**)

        Power the value passed or attribute

        Example:
            calc = node.a.sx ** node.a.sy
        """
        return self.multiplyDivideNode(value, operationType=3)
    
     # -------------------------------------------------------------------------
     # ARITHMETRIC NODES - NODE HANDLING / ATTRIBUTES

    def createNodeName(self, value, suffix):
        """
        createNodeName [Method]

        Creates a new node name.
        """
        suffixCut = (suffix[0] + "".join([i for i in suffix if i.isupper()])).upper()
        
        nodesAttached = "{0}_{1}_{2}_{3}".format(
            self.node.name, self.attr, value, suffixCut)
        
        nodeName = "".join(
            ["_" if i in string.punctuation else i for i in nodesAttached])

        return nodeName

    def checkConnectionAttribute(self, inputValue):
        """
        checkConnectionAttribute [Method]

        Check whether the connections are parents (True) or child (False) plugs.
        """
        inputIsParent = True if (isinstance(
            inputValue, Attribute) and inputValue.isParent) else False

        return True if (self.isParent and inputIsParent) else False
    
    # -------------------------------------------------------------------------
    # ARITHMETRIC NODES - CREATION
    
    def createPlusMinusAverage(self, nodeName, nodeType, 
                               operationType, attribute, value):
        """
        createPlusMinusAverage [Method]

        Creating the new plug and make the connections to the node.

        Args:
            nodeName (str): The full node name to use.
            nodeType (str): The type of object to use.
            operationType (int): The index of the node type to use.
            attribute (str): The attribute name to use.
            value (int/float/str/attributeObject): The value to use.

        Returns:
            class: The attribute nodal name and class.
        """
        # Importing here to avoid circular dependency
        from modules.nodel import Dep_Node
        
        # Creating the PMA node
        pma = Dep_Node(nodeName, nodeType)
        pma.a.operation.set(operationType)

        # Connect to the original item into the new node
        pma.a[attribute] << self

        if isinstance(value, (float, int)):
            pma.a[attribute].addToPlusMinusAverage(attribute, value)

        elif isinstance(value, six.string_types) or isinstance(value, Attribute):
            pma.a[attribute] << value
        
        if self.checkConnectionAttribute(value):
            return pma.a.output3D

        return pma.a.output1D
    
    def plusMinusAverageNode(self, value, operationType=1):
        """
        plusMinusAverageNode [Method]

        Adding or Substracting the value passed or attribute.

        Args:
            value (int/float/str/attributeObject): The value to use.
            operationType (int):The operation to use. Defaults to sum.
                operationType = 1 (sum)
                operationType = 2 (substract)
                operationType = 3 (average)
        Returns:
            object: self

        Example 1:
            addNode = node.a.sx + node.a.sy

        Example 2:
            calc = ((node.a.sx + node.a.sy) + node.a.sz) + 10
            calc.a.output >> node.a.s
        """
        # The node type
        nodeType = "plusMinusAverage"
        nodeName = self.createNodeName(value, nodeType)

        # Check whether the connections are both parent plugs or children
        attribute = "input3D" if self.checkConnectionAttribute(
            value) else "input1D"

        # This make the addition to a current plusMinus node if is self
        if (m.objectType(self.node) == nodeType) and (m.getAttr(self.node.a.operation) == operationType):
            self.addToPlusMinusAverage(attribute, value)

        # Make this the straight string and float input
        else:
            return self.createPlusMinusAverage(nodeName, nodeType, operationType, attribute, value)

        return self

    def addToPlusMinusAverage(self, attribute, value):
        """
        addToPlusMinusAverage [Method]

        Find the end attribute to add to.

        Args:
            attribute (int/float/str/attributeObject): The maya node.
            value (int/float/str/attributeObject): The maya node.
        """
        connectionIndex = m.getAttr(self.node.a[attribute], s=1)

        if isinstance(value, (float, int)):
            self.node.a["%s[%s]" % (attribute, connectionIndex)].set(value)
        else:
            self.node.a["%s[%s]" % (attribute, connectionIndex)] << value

    
    def multiplyDivideNode(self, value, operationType=1):
        """
        multiplyDivideNode [Method]

        Multiplying or Dividing the valuse passed or attribute.

        Args:
            value (int/float/str): The value to use and drive.
            operationType (int):The operation to use.
                operationType = 1 (multiply)
                operationType = 2 (divide)
                operationType = 3 (power)

        Returns:
            object: Created node

        Example 1:
            addNode = node.a.sx * node.a.sy

        Example 2:
            calc = ((node.a.sx * node.a.sy) * node.a.sz) * 10
            calc.a.output >> node.a.s
        """
        nodeType = "multiplyDivide"
        nodeName = self.createNodeName(value, nodeType)

        # This makes the addition to a current plusMinus node if is self

        # ---- Multiply

        if operationType == 1:

            # If scale (parent)
            if self.checkConnectionAttribute(value):
                return self.createMultiDivide(nodeName, nodeType, operationType, value)
            
            # If scaleX (child)
            else:
                return self.createMultiDoubleLinear(nodeName, value)
    
        # ---- Divide / power

        else:
            # If whole scale, translate or rotate value (parent)
            if self.checkConnectionAttribute(value):
                return self.createDivideParent(nodeName, nodeType, operationType, value)
            
            # If smaller amounts like scaleX, translateY, etc (child)
            else:
                return self.createDivideChildren(nodeName, nodeType, operationType, value)
            
    def createMultiDivide(self, nodeName, suffix, operationType, value):
        """
        createMultiDivide [Method]

        Create the multiplyDivide node that we need to work with.

        Args:
            nodeName (str): The full node name to use.
            suffix (str): The naming to use.
            operationType (int): The index of thje node type to use.
            value (int/float/str/attributeObject): The value to use.
        
        Returns:
            class: The attribute nodal class.
        """
        # Importing here to avoid circular dependency
        from modules.nodel import Dep_Node

        md = Dep_Node(nodeName, suffix)
        md.a.operation.set(operationType)

        md.a.input1 << self
        md.a.input2 << value

        return md.a.output

    def createMultiDoubleLinear(self, nodeName, value):
        """
        createMultiDoubleLinear [Method]

        Create the multi double linear node to work with.

        Args:
            nodeName (str): The full node name to use.
            value (int/float/str/attributeObject): The value to use.
        
        Returns:
            class: The attribute nodal class.
        """
        # Importing here to avoid circular dependency
        from modules.nodel import Dep_Node

        mdl = Dep_Node(nodeName[:-2] + "MDL", "multDoubleLinear")

        # Connect self into the new node
        mdl.a.input1 << self

        # Connect the value attr into the new node
        if isinstance(value, (float, int)):
            mdl.a.input2.set(value)
        else:
            mdl.a.input2 << value
        
        return mdl.a.output

    def createDivideParent(self, nodeName, nodeType, operationType, value):
        """
        createDivideParent [Method]

        Create the multi divide node to work with parent attributes

        Args:
            nodeName (str): The full node name to use.
            nodeType (str): The node to use.
            operationType (int): The index of thje node type to use.
            value (int/float/str/attributeObject): The value to use.
        
        Returns:
            class: The attribute object output.
        """
        # Importing here to avoid circular dependency
        from modules.nodel import Dep_Node

        multiply = Dep_Node(nodeName, nodeType)
        multiply.a.operation.set(operationType)

        # Connect self into the new node
        multiply.a.input1 << self

        # Connect the value attr into the new node
        if isinstance(value, (float, int)):
            multiply.a.input2.set(value)
        else:
            multiply.a.input2 << value

        return multiply.a.output

    def createDivideChildren(self, nodeName, nodeType, operationType, value):
        """
        createDivideChildren [Method]

        Create the multi divide node to work with child attributes

        Args:
            nodeName (str): The full node name to use.
            nodeType (str): The node to use.
            operationType (int): The index of the node type to use.
            value (int/float/str/attributeObject): The value to use.
        
        Returns:
            class: The attribute object output.
        """
        # Importing here to avoid circular dependency
        from modules.nodel import Dep_Node

        multiply = Dep_Node(nodeName, nodeType)
        multiply.a.operation.set(operationType)

        # Connect self into the new node
        multiply.a.input1X << self

        # Connect the value attr into the new node
        if isinstance(value, (float, int)):
            multiply.a.input2X.set(value)
        else:
            multiply.a.input2X << value

        return multiply.a.outputX


    # -------------------------------------------------------------------------
    # PROPERTIES- ARITHMETRIC NODES

    @property
    def isParent(self):
        """
        isParent [Property]

        Check whether the connection is a parent.
        """
        return bool(self.children)

    @property
    def isChild(self):
        """
        isChild [Property]

        Check whether the connection is a child.
        """
        return bool(self.parent)

    # -------------------------------------------------------------------------
    # PROPERTIES

    @property
    def attr(self):
        """
        attr [Property]

        Object attribute string.

        Example:
            print(sphere.a.rotateX.attr)
            # Output: "rotateX"
        """
        return self._attribute

    @property
    def attribute(self):
        """
        attribute [Property]

        Object attribute string.

        Example:
            print(sphere.a.rotateX.attribute)
            # Output: "rotateX"
        """
        return self._attribute

    @property
    def path(self):
        """
        path [Property]

        Object attribute string path with node name and attr.

        Returns:
            str: The obj attribute string path

        Example:
            print(sphere.a.rotateX.path)
            # Output: "sphere_GEO.rotateX"
        """
        nodePath = "{0}.{1}".format(self.node.path, self.attribute)
        if self.node.path and m.objExists(nodePath):
            return nodePath

    @property
    def fullPath(self):
        """
        fullPath [Property]

        Object attribute string full path with node full path, 
        name and attr.

        Returns:
            str: The obj attribute string path

        Example:
            print(sphere.a.rotateX.fullPath)
            # Output: "|BASE_GRP|SUB_GRP|sphere_GEO.rotateX"
        """
        nodePath = "{0}.{1}".format(self.node.fullPath, self.attribute)
        if self.node.fullPath and m.objExists(nodePath):
            return nodePath

    @property
    def children(self):
        """
        children [Property]

        Returns a list of the children attributes if any.

        Example:
            print(sphere.a.r.children)
            Output: [
                    attribute('sphere_GEO.rotateX'), 
                    attribute('sphere_GEO.rotateY'), 
                    attribute('sphere_GEO.rotateZ') 
                    ]

            print(sphere.a.rx.children)
            Output: []
        """
        if self.query(indexMatters=True, multi=True):
            multiIndices = m.getAttr(self, multiIndices=True)
            index = len(multiIndices) if multiIndices else 0
            lc = self.query(listChildren=True)

            # If children return all the multi indices attrs
            if lc:
                return [self.node.a["%s[%s].%s" % (self.attr, index, a)] for a in lc]
            
            # Return the single multi index item
            else:
                return [self.node.a["%s[%s]" % (self.attr, index)]]

        return [
            self.node.a[attr]
            for attr in self.query(listChildren=True) or []
        ]

    @property
    def parent(self):
        """
        parent [Property]

        Returns a list of the parent attributes if any.

        Example:
            print(sphere.a.rotateX.parent)
            Output: [attribute('sphere_GEO.rotate')]

            print(sphere.a.rotate.parent)
            Output: []
        """
        a = self.query(listParent=True)
        if a:
            return Attribute(self.node, a[0]) or []
        return []

    @property
    def outputs(self):
        """
        outputs [Property]

        Returns all the outputs of an attribute.

        Example:
            print(sphere.a.rX.outputs)
            Output: list
        """
        if self.node.exists():
            return self.node.a.list(o=True, ro=1)
        return None

    @property
    def connectionInput(self):
        """
        connectionInput [Property]

        Returns the input connection of an attribute.

        Example:
            print(sphere.a.rX.connectionInput)
            Output: Attribute('cube_GEO.rotateX')
        """
        # Import here to avoid dependency issues when using Dep_Node
        from modules.nodel import Dag_Node
        # Needs to be outside main herarchy to avoid cyclic dependency

        attrs = m.listConnections(self.fullPath, p=1, d=0) or []

        if self.children:
            for child in self.children:
                childAttrs = m.listConnections(child.fullPath, p=1, d=0)
                if childAttrs:
                    attrs += childAttrs

        inputs = []
        if attrs:
            for attr in attrs:
                nodeName = Dag_Node(attr.split(".")[0])
                attrName = attr.split(".")[-1]
                inputs.append(Attribute(nodeName, attrName))
            return inputs[0] if len(attrs) == 1 else inputs

        return None

    @property
    def connectionOutputs(self):
        """
        connectionOutputs [Property]

        Returns all the output connections of an attribute.

        Example:
            print(cube.a.rX.connectionOutputs)
            Output: [Attribute('sphere_GEO.rotateX'), etc...]
        """
        # Import here to avoid dependency issues when using Dep_Node
        from modules.nodel import Dag_Node

        attrs = m.listConnections(self.fullPath, p=1) or []

        if self.children:
            for child in self.children:
                childAttrs = m.listConnections(child.fullPath, p=1)
                if childAttrs:
                    attrs += childAttrs

        if attrs:
            attrNodes = [
                Attribute(Dag_Node(attr.split(".")[0]),
                          attr.split(".")[-1]) for attr in attrs]
            return attrNodes

        return None

    # -------------------------------------------------------------------------
    # METHODS

    def exists(self):
        """
        exists [Method]

        Checks wether our attribute exists

        Example:
            print(sphere.a.rX.exists())

            Output: True
        """
        if self.fullPath:
            return True
        return False

    def set(self, *args, **kwargs):
        """
        set [Method]

        Sets our attribute using functionality from maya.cmds

        Example:
            print(sphere.a.rx.set(1))
        """
        m.setAttr(self.fullPath, *args, **kwargs)

    def get(self, **kwargs):
        """
        get [Method]

        Gets our attribute value using functionality from maya.cmds

        Example:
            print(sphere.a.rx.get())

            Output: 1
        """
        return m.getAttr(self.fullPath, **kwargs)

    def query(self, **kwargs):
        """
        query [Method]

        Query's our attribute value using functionality from maya.cmds

        Example:
            print(sphere.a.rx.query(listParent=True))

            Output: ['rotate']
        """
        return m.attributeQuery(self.attribute, node=self.node, **kwargs)

    def connect(self, attr):
        """
        connect [Method]

        Connects this attribute to the passed item.

        Args:
            attr (obj): The obj attribute to be connected

        Example:
            sphere.a.rx.connect(cube.a.rx)
        """
        if not m.isConnected(self, attr):

            if (self.query(lc=1) != None) and (attr.query(lc=1) == None):
                raise ValueError(
                    """The driving of these values might be a parent value such as scale 
                    and the driven cannot then be a child such as scaleX, 
                    this must be handled on the input side"""
                )

            try:
                drivingAttrs = self.children or [self] * 3
                drivenAttrs = attr.children or [attr]

                for driver, driven in zip(drivingAttrs, drivenAttrs):
                    m.connectAttr(driver, driven, force=True)

            except (RuntimeError, AttributeError):
                m.connectAttr(self, attr, force=True)

            return self

    def disconnect(self):
        """
        disconnect [Method]

        Disconnects the attribute if connected

        Example:
            cube.a.r.disconnect()
        """
        allAttrs = self.children if self.children else self
        connections = m.listConnections(allAttrs, s=1, p=1)

        if not connections:
            return None

        if self.children:
            for child_attr in self.children:
                conn_attr = m.listConnections(child_attr, s=1, p=1)
                if not conn_attr:
                    continue

                if m.isConnected(conn_attr[0], child_attr):
                    m.disconnectAttr(conn_attr[0], child_attr)
        else:
            for attr in connections:
                if m.isConnected(attr, self.fullPath):
                    m.disconnectAttr(attr, self.fullPath)

    def delete(self):
        """
        delete [Method]

        Deletes the attribute.

        Example:
            cube.a.geo_vis.delete()
        """
        m.deleteAttr(self.fullPath)
