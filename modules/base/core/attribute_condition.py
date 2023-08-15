'''
/*****************************************************************************/
                        Attribute Condition v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Condition Node Functionality

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Condition [Class] 

>> NOTES >> 
	Update 05/08/2023 : Start working on the script
 
>> THANKS >> 
    Nick Hughes [5/08/2023]:
        For his awesome course that led me to create this file. 

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''
# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from modules.base import Dep_Node

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Condition(Dep_Node):
    """
    Condition [Class] (Inherits from: Dep_Node)

    The class that will carry our condition node information.
    """
    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node, firstTerm=None, secondTerm=None, operation=None):
        Dep_Node.__init__(self, node, "condition") # Creates condition nodeType

        # Set the attribute that we are working with that will set the condition
        if firstTerm:
            self.setFirstTerm(firstTerm)

        if secondTerm:
            self.setSecondTerm(secondTerm)

        if operation:
            self.a.operation.set(operation)

    # -------------------------------------------------------------------------
    # METHODS

    def setFirstTerm(self, firstTerm):
        """
        setFirstTerm [Method]

        Set the first term that we'll use to drive the maya codition node.

        Args:
            firstTerm (float): First term of the maya condition node.
        """
        return self.setConditionTerm(firstTerm, "firstTerm")

    def setSecondTerm(self, secondTerm):
        """
        setSecondTerm [Method]

        Set the second term that we'll use to drive the maya codition node.

        Args:
            secondTerm (float): Second term of the maya condition node.
        """
        return self.setConditionTerm(secondTerm, "secondTerm")

    def setConditionTerm(self, value, term):
        """
        setConditionTerm [Method]

        Set the terms and the value of the terms that will drive the  condition

        Args:
            value (float, int): Value of the terms in condition node.
            term (Parameter): The term (First or Second) that we'll use.
        
        Returns:
            self.a.outColor
        """
        # Direct input to node of value float or int
        if isinstance(value, (float, int)):
            self.a[term].set(value)
        
        # whole parent attr value like translate or rotate (not rotateX)
        elif (value.__class__.__name__ == "Attribute") and (value.children):
            valAttrX, valAttrY, valAttrZ = value.children
            (valAttrX + valAttrY + valAttrZ) >> self.a[term]
            return self.a.outColor
        
        # Single attr value
        else:
            self.a[term] << value
        
        # Return the output that we will use
        return self.a.outColorR

    def setCondition(self, ifTrue=None, ifFalse=None, returnParent=False):
        """
        setOperation [Method]

        Set the values of the True and the False in the condition node.
        Either use an int, float, list, tuple, or str ("scaleX" or "scale" or "sx")

        Args:
            ifTrue (int, float, list, tuplem str, attributeObj):The value to use.
            ifFalse (int, float, list, tuplem str, attributeObj):The value to use.
            returnParent (bool): Whether we return a parent/child attribute. Default False.
        
        Returns:
            class attr: The class parent or child attr to work with.

        Syntax:
            ({FirstTerm} {Operation} {SecondTerm}).setCondition(ifTrue={values}, ifFalse={values})             
        
            Operations are the same as Python!
        
        Example 1:
            (node1.a.sx <= node2.a.sx).setCondition(ifTrue=node1.a.sx, ifFalse=node2.a.sx)

        Example 2:
            (node1.a.sx <= node2.a.sx).setCondition(ifTrue=1, ifFalse=0) >> node1.a.sz

        Example 3:
            calc = node1.a.sx <= node2.a.sx
            calc.setCondition(ifTrue=[1,2,3], ifFalse[10,3,4]) >> node1.a.sz
        """
        # Connect the value attr into the new node
        for attr, value in zip(["colorIfTrue", "colorIfFalse"], [ifTrue, ifFalse]):
            
            # Setting an integer/float
            if isinstance(value, (float, int)):
                self.a[attr + "R"].set(value)
            
            # Setting list or tuples
            elif isinstance(value, (list, tuple)):
                self.a[attr].set(*value)
                returnParent = True
            
            else:
                # Setting parent attributes
                if (value.__class__.__name__ == "Attribute") and  (value.children):
                    self.a[attr] << value
                    returnParent  = True
                
                # Setting a child attriute
                else:
                    self.a[attr + "R"] << value
        
        return self.a["outColor"] if returnParent else self.a["outColorR"]
