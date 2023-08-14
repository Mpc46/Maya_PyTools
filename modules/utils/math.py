'''
/*****************************************************************************/
                                Math v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Math calculations and functionality.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Dag_Node [Class]

>> NOTES >> 
	Update 08/08/2023 : Start working on the script
 
>> THANKS >> 
    Nick Hughes [08/08/2023]:
        For his awesome course that led me to create this file. 
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------
from maya import cmds as m
import math
import six


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def getDistanceBetween(obj1, obj2):
    """
    getDistanceBetween [Function]

    Measures the distance between the objects passed.

    Alist can be passed if the x,y,z has already be ascertained.

    Args:
        obj1 (str/list): The item to gather the position from or the list of the X,Y,Z.
        obj2 (str/list): The item to gather the position from or the list of the X,Y,Z.

    Returns:
        float: The distance in the scene between the items.
    """
    
    objectDistance1 = m.xform(obj1, ws=1, t=1, q=1) if isinstance(obj1, six.string_types) else obj1
    objectDistance2 = m.xform(obj2, ws=1, t=1, q=1) if isinstance(obj2, six.string_types) else obj2

    return getDistanceBetweenCalculation(objectDistance1, objectDistance2)

def getDistanceBetweenCalculation(objectDistance1, objectDistance2):
    """
    getDistanceBetweenCalculation [Function]

    Return the 3D or 3D distance based on coordinates passed.

    Returns:
        float: The distance in the scene between the items.
    """
    xDiff = objectDistance2[0] - objectDistance1[0]
    yDiff = objectDistance2[1] - objectDistance1[1]

    if len(objectDistance1) > 2:
        zDiff = objectDistance2[2] - objectDistance1[2]
        return math.sqrt(xDiff*xDiff + yDiff*yDiff + zDiff*zDiff)
    
    return math.sqrt(xDiff*xDiff + yDiff*yDiff)