'''
/*****************************************************************************/
                                Common v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    All common needed functions.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + matchMove [Func]
    + createOffset [Func]

>> NOTES >> 
	Update 04/08/2023 : Start working on the script
 
>> THANKS >> 
    Nick Hughes [04/08/2023]:
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


# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def matchMove(selection, point=0, orient=0):
    """
    matchMove [Function]

    Takes a driver location object and a list of driven items to move in that 
    order. The default option is to use a parentConstrain to move both translate 
    and rotate unless point or orient are set to True.  
    The first item in list/selection is gonna be the driver of our function.

    Args:
        selection (List): A list of items in the scene. Defaults to None.
        point (Bool): The type of contraint to create. Defaults to False.
        orient (Bool): The type of contraint to create. Defaults to False.

    Example:
        matchMove(["sphere_GEO", "MODEL_GRP"])
    """
    parentObj = selection.pop(0)  # Remove parent from list

    for obj in selection:
        # Repositions Obj
        try:
            if point or orient:
                if point:
                    constraint = m.pointConstraint(parentObj, obj, mo=False)
                if orient:
                    constraint = m.orientConstraint(
                        parentObj, obj, mo=False)
            else:
                constraint = m.parentConstraint(parentObj, obj, mo=False)

            # Remove the constraint
            m.delete(constraint)

        except Exception as e:
            print(">>> matchMove Error: {0}: {1}".format(type(e).__name__, e))


def createOffset(selection, grpName = "_OFF_GRP"):
    """
    createOffset [Function]

    Takes the selection passed in the scene or the selection passed and
    creates the offset groups in their locations.

    Args:
        selection (List): A list of items in the scene. Defaults to None.
        grpName (Str): Name of the Offset Groups Suffix. Defaults to "_OFF_GRP".

    Returns:
        list : List of the Offset groups that have been created.

    Example:
        createOffset("sphere_GEO")

        # Output: ["sphere_GEO_OFF_GRP"] 
    """
    newlyCreatedGroups = []
    offsetGrpNames = [
        grpName, "_PLACER_GRP", "_PLACER_OFF_GRP", "_SUB_GRP", "_SUB_OFF_GRP",
        "_ZERO_GRP", "_ZERO_OFF_GRP", "_BASE_GRP", "_BASE_OFF_GRP",
        ]

    for num, item in enumerate(selection):
        if not m.objExists(item):
            print(
                ">>> Could not create Offset group as item does not exist: {}".format(item))
            continue

        offGrpParent = m.pickWalk(item, d="Up")[0]

        # If the current item ends with the group name, we remove the first name from the
        # offsetGrpNames list, we also remove the group name from the current item name.
        if item.endswith(grpName):
            offsetGrpNames.pop(0)
            newItemName = item.replace(grpName, "")
        else:
            # If the item doesn't end with the group name, we keep the item name as is
            newItemName = item

        # Here we're creating a new group name by appending the first available
        # name from the name List
        groupName = next((newItemName + suffix for suffix in offsetGrpNames
                          if not m.objExists(newItemName + suffix)), None)

        # If a group name was created successfully we create a new group
        if groupName:
            offGrp = m.group(em=1, w=1, n=groupName)
            matchMove([item, offGrp])

            m.parent(item, offGrp)

            if str(offGrpParent) != str(item):
                m.parent(offGrp, offGrpParent)

            newlyCreatedGroups.append(offGrp)

        else:
            print(">>> Could not create offset group for: {}".format(item))

        return newlyCreatedGroups


def duplicateChain(chain=None, suffix="_new"):
    """
    Takes a list of objects and duplicates them with a new suffix.

    Args:
        chain (list): The chain to duplicate. Defaults to None.
        suffix (str): The suffix of the new joints. Defaults to "_new".

    Returns:
        list: the list of the newly created objects.
    """
    from modules.base import Dag_Node as dag

    if chain is None:
        chain = []

    if not isinstance(chain, list):
        chain = [chain]

    chain = [dag(i) for i in chain]
    new_chain = []

    for i in chain:
        item = i.duplicate(n="{}{}".format(i.name, suffix), po=len(chain) > 1)
        new_chain.append(item)
        if len(new_chain) > 1:
            item.parentTo(new_chain[-2])

    for obj in new_chain:
        if not obj.name.endswith(suffix):
            obj.rename("{}{}".format(obj.name, suffix))

    return new_chain