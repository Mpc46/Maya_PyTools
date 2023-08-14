'''
/*****************************************************************************/
                                Color v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Color functionality (Color override)

>> HOW TO USE >>
	This module is meant to be imported into larger scripts.

>> CONTENTS >>
    + getColorFromInteger [Func]
    + getColrFromString [Func]
    + getColor [Func]
    + setColor [Func]

>> NOTES >> 
	Update 04/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [04/08/2023]:
        For his awesome course that led me to create this file. 
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------
import six # Need to install module trough pip
from maya import cmds
from modules.utils.common_names import COLORS_DICT

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def getColorFromInteger(color):
    """
    getColorFromInteger [Function]

    Takes an integer of a color Maya's index number and returns
    the string(name) representation of that color. 

    Maya color index range is 0 to 31
    
    Args:
        color (int): The color string to get.

    Returns:
        Str: The color index name if found.
    
    Example:
        getColorFromInteger(24)
        # Output: "dark orange"
    """
    return [i for i in COLORS_DICT if COLORS_DICT[i] == color][0]

def getColorFromString(color):
    """
    getColorFromString [Function]

    Takes a string of a color and returns Maya's color index
    ovverideColor attribute.
    
    Args:
        color (str): The color index to get.

    Returns:
        Int: The color index if found.
    
    Example:
        getColorFromString("Blue")
        # Output: 6
    """
    if color.lower() in COLORS_DICT:
        return COLORS_DICT[color.lower().replace("_", " ")]
    
    raise ValueError("Sorry but the color name you entered was not found")

def getColor(item):
    """
    getColor [Function]

    Gets the color of the object shape item passed.

    Args:
        item (str): The object to get the color from.
    
    Returns:
        int : The color index name if found.
        
    Example:
        getColor("hand_CTRL")
        # Output : 26
    """
    # Extend objects with it's shapes and filter the selection by Types
    
    objectRelatives = cmds.listRelatives(item, shapes=1, f=1, ni=1) or []
    objectRelatives.append(item)
    
    allObjects = cmds.ls(objectRelatives, type=['nurbsCurve', 'locator', 'joint'])
    
    for obj in allObjects:
        if cmds.getAttr("{0}.overrideEnabled".format(obj)):
            return cmds.getAttr("{0}.overrideColor".format(obj))

def setColor(objects, color=None):
    """
    setColor [Function]

    Takes a list of objects and sets their colors.

    Args:
        objects (list): The object to change the color of.
        color (int/str): The objects color to set.
        
    Example:
        setColor(24)
        # Output: Item color changed.
    """

    if not color:
        raise ValueError("Please pass either the color number or name: '%s' not understood." % str(color))

    # Then we have the information to set the color with so passing
    if isinstance(color, six.string_types):
        color = getColorFromString(color)

    elif type(color) != int:
        raise TypeError("Format not understood: Please pass either the color number or name.")

    # Force objects to be a list
    objectsList = objects if type(objects) == list else [objects]

    # Extend objects with its shapes and filter the selection by Types

    extendedSelection = []
    shapes = cmds.listRelatives(objectsList, shapes=1, f=1, ni=1) or []
    extendedSelection.extend(cmds.ls(objectsList, l=1))
    extendedSelection.extend(shapes)

    allObjects = cmds.ls(extendedSelection, type=['nurbsCurve', 'locator', 'joint'])

    # Change Color Override
    for obj in allObjects:
        if cmds.objExists(obj + ".overrideEnabled") and cmds.objExists(obj + ".overrideColor"):
            cmds.setAttr("{0}.overrideEnabled".format(obj), 1)
            cmds.setAttr("{0}.overrideColor".format(obj), color)
