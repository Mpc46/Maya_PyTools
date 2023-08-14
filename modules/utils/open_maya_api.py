'''
/*****************************************************************************/
                            Open Maya API v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    A utility function that facilitates the converstion of Maya Nodes
    into various API objects like "Mobject", or "MDagPath".

>> HOW TO USE >>
	Input instructions on how to use
 
>> CONTENTS >> 
    + toDpendencyNode [Func]
    + toMObject [Func]

>> NOTES >> 
	Update 02/08/2023 : Start working on the script
    Update 03/08/2023 : Added the "toMDagPath" function

>> THANKS >> 
    Nick Hughes [02/08/2023]:
        For his awesome course that led me to create this file. 
        
>> CONTACT >>
    luisf.carranza@outlook.com ←or→ https://mpc46.carrd.co
    Copyright (C) 2023 Luis Carranza. All rights reserved.

/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import OpenMaya


# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def toDpendencyNode(node):
    """
    toDpendencyNode [Function]

    Convert a node into an OpenMaya Dependency Node.

    Args:
        node (str): The maya node.

    Returns:
        Object: The OpenMaya Dependency Object.

    Example:
        name = "L_hand_JNT"
        obj = toDependencyNode(name)
        print(obj.typeName())

        # Output: joint
    """

    obj = toMObject(node)

    return OpenMaya.MFnDependencyNode(obj)


def toMObject(node):
    """
    toMObject [Function]

    Converts a node into an OpenMaya Object.

    Args:
        node (str): The maya node.

    Returns:
        Object: The OpenMaya Object.

    Example:
        name = "L_hand_JNT"
        obj = toMObject(name)
        print(obj.fullPathName())

        # Output: |BASE_GRP|SUB_GRP|L_hand_JNT
    """

    selectionList = OpenMaya.MSelectionList()
    selectionList.add(node)

    obj = OpenMaya.MObject()
    selectionList.getDependNode(0, obj)

    return obj


def toMDagPath(node):
    """
    toMDagPath [Function]

    Converts a node into an OpenMaya Dag Object.

    Args:
        node (str): The maya node.

    Returns:
        Object: The OpenMaya Object.

    Example:
        name = "L_hand_JNT"
        obj = toMDagPath(name)
        print(obj.partialPathName())
        print(obj.fullPathName())

        # Output: L_hand_JNT
        # Output: |BASE_GRP|SUB_GRP|L_hand_JNT
    """
    
    obj = toMObject(node)
    if obj.hasFn(OpenMaya.MFn.kDagNode):
        dag = OpenMaya.MDagPath.getAPathTo(obj)
        return dag
