'''
/*****************************************************************************/
                            Common functions v 1.0
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
    + getKeyFromValue [Func]
    + ToCamelCase [Func]

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

from maya import cmds


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
                    constraint = cmds.pointConstraint(parentObj, obj, mo=False)
                if orient:
                    constraint = cmds.orientConstraint(
                        parentObj, obj, mo=False)
            else:
                constraint = cmds.parentConstraint(parentObj, obj, mo=False)

            # Remove the constraint
            cmds.delete(constraint)

        except Exception as e:
            print(">>> matchMove Error: {0}: {1}".format(type(e).__name__, e))


def createOffset(selection, grpName="_OFF_GRP"):
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
        if not cmds.objExists(item):
            print(
                ">>> Could not create Offset group as item does not exist: {}".format(item))
            continue

        offGrpParent = cmds.pickWalk(item, d="Up")[0]

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
                          if not cmds.objExists(newItemName + suffix)), None)

        # If a group name was created successfully we create a new group
        if groupName:
            offGrp = cmds.group(em=1, w=1, n=groupName)
            matchMove([item, offGrp])

            cmds.parent(item, offGrp)

            if str(offGrpParent) != str(item):
                cmds.parent(offGrp, offGrpParent)

            newlyCreatedGroups.append(offGrp)

        else:
            print(">>> Could not create offset group for: {}".format(item))

        return newlyCreatedGroups


def getKeyFromValue(dictionary, target_value):
    """
    getKeyFromValue [Function]

    Get a dictionary key from it's value
    key:value

    Args:
        dictionary (dict): The dictionary to use
        target_value (any): the value to get key from

    Returns:
        key: The key value

    Example:
        my_dic = {"one":1, "two":2}
        getKeyFromValue(my_dic, 1)
        Output: "one"
    """
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None  # >>> No key was found for the value


def ToCamelCase(string, splitBy=None):
    """
    ToCamelCase [Function]

    Takes a string and returns a camel case version of it.

    Args:
        string (str): A string to camel case.
        splitBy (str/optional): the parameter to split with.


    Returns:
        str: AStringToCamelCase.
    """
    string_Title = string.title()  # Makes every word upperCase

    if splitBy is not None:
        string_List = string_Title.split(splitBy)  # Creates list
    else:
        string_List = string_Title.split()

    if len(string_List) > 1:
        camelCase = "".join(string_List)  # Merge list into string
        return camelCase
    else:
        return string_Title  # Nothing to Split just return title string
