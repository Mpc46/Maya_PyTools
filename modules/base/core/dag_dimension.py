'''
/*****************************************************************************/
                            DAG Dimensions v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Our object dimensions functionality.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Object_Dimension [Class]

>> NOTES >> 
	Update 08/08/2023 : Start working on the script
 
>> THANKS >> 
    Nick Hughes [08/08/2023]:
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
from modules.utils.math import getDistanceBetween

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Object_Dimension(object):
    """
    Object_Dimension [Class]

    Class based way of calling the information regarding, objects, their
    dimensions and pivots.

    Args:
        object (_type_): _description_
    """
    def __init__(self, node):
        self._node = node

        if not self.worldMatrix:
            raise ValueError(">>> No worldMatrix and therefore no dimension found for this object.")
        
    @property
    def worldMatrix(self):
        return self._node.a.worldMatrix.exists()    
    
    @property
    def xformBoundingBox(self):
        """ Xform Bounding Box
            
            Returns:
                list: [minTX, minTY, minTZ, maxTX, maxTY, maxTZ]
        """
        return m.xform(self._node, q=1, bbi=1)
        
    @property
    def bb(self):
        """ Xform Bounding Box"""
        return self.xformBoundingBox
    
    @property
    def width(self):
        return self.bb[3] - self.bb[0] # From list example on BB
    
    @property
    def height(self):
        return self.bb[4] - self.bb[1]
    
    @property
    def depth(self):
        return self.bb[5] - self.bb[2]
    
    @property
    def centre(self):
        """ Gathering the centre of the object in world space.
            
            Returns:
                list: [x, y, z]
        """
        return [
            (self.bb[3] + self.bb[0]) / 2,
            (self.bb[4] + self.bb[1]) / 2,
            (self.bb[5] + self.bb[2]) / 2
        ]
    
    @property
    def center(self):
        return self.centre
    
    @property
    def position(self):
        """ Position will return the world space translate and rotate pivot of the object """
        from modules.base import Dag_Node as Dag
        tempDag = Dag(m.group(em=1, w=1)); tempDag.moveTo(self._node);

        position = [float(format(i, "f")) for i in m.xform(tempDag, ws=1, t=1, q=1) 
                    + m.xform(tempDag, ws=1, ro=1, q=1)]
        
        tempDag.delete()

        return position
    
    @property
    def pivot(self):
        """ Returns the translation pivot and object rorate value """
        return m.xform(self._node.fullPath, q=1, piv=1)[:3] + m.xform(self._node.fullPath, q=1, ws=1, ro=1)

    # --------------------------------------------------------------
         
    def copyPivot(self, driverObject, drivenObject):
        """ Copy the pivot of an object in maya from a driver to a driven object """
        # Get the pìvot position of the source object
        source_translate = m.xform(driverObject, q=1, ws=1, t=1)

        # Move the pivot of the target object to the source pivot position
        m.xform(drivenObject, ws=1, pivots=source_translate)
    
    def copyPivotTo(self, item):
        return self.copyPivot(self._node, item)

    def copyPivotFrom(self, item):
        return self.copyPivot(item, self._node)

    def centrePivot(self):
        m.xform(self._node.fullPath, cp=1)

    def centerPivot(self):
        return self.centrePivot()
    
    # --------------------------------------------------------------

    def distanceTo(self, item):
        """ Gets the distance in world space between two objects 
        
            Returns:
                Output: float

            Example:
                3.434342
        """
        distance = getDistanceBetween(str(self._node), str(item))

        return distance
    