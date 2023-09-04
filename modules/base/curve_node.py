'''
/*****************************************************************************/
                            Curve Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Class based approach to work with curves and their properties.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Curve [Class] (Inherits from Dag_Node)

>> NOTES >> 
	Update 21/08/2023 : Started to work on the script.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.

/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.base import Dag_Node

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Curve(Dag_Node):
    """
    Curve [Class] (Inherits from: Dag_Node)

    Class based way of calling the information that we need to deal 
    with Maya curves in a clean Python way.
    """
    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node, **kwargs):

        Dag_Node.__init__(self, node)

        if node and kwargs:
            self.create(**kwargs)
    
    # -------------------------------------------------------------------------
    # FORMATION

    @property
    def cvs(self):
        """ Returns list of curve points on shape. """
        return m.ls(self.fullPath + ".cv[*]", fl = 1)

    @property
    def cvPositions(self):
        """ Returns dictionary of positions of curve points. """
        epCoordinates = {}
        for i in self.cvs:
            epCoordinates[i] = m.pointPosition( "{}".format(i), w=True )

        return epCoordinates
    
    @property
    def cvPositionsList(self):
        """ Returns list of positions of curve points. """
        cv_position_list = []

        for i in self.cvPositions.values():
            cv_position_list.append(i)
            
        return cv_position_list
    
    # -------------------------------------------------------------------------
    # METHODS

    def splitCurve(self):
        """
        splitCurve into individual curves based on shapes.

        Returns:
            list: The new curves created from self.
        """
        newShapes = []

        for shape in self.shapes:
            newTrans = Dag_Node(m.createNode('transform', n=shape))
            m.parent(shape, newTrans.path, s=1)
            child = Dag_Node(newTrans.children[0])
            child.rename(newTrans.name).parentTo(self)
            newTrans.delete()
            newShapes.append(shape)
       
        return newShapes

    def mergeCurves(self, *items):
        """
        Merges curves shapes to self, and then deletes empty transforms.

        Example:
            curve1.mergeCurves(crv2, crv3)
        """
        items = [items] if len(items) < 1 else items
        for crv in items:
            cvShape = crv.shape
            m.parent(cvShape, self.fullPath, r=True, s=True)
            crv.delete()
        
        return self.fullPath
    
    # -----------------
