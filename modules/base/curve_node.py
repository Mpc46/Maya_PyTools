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
    def points(self):
        return m.ls(self.fullPath + ".cv[*]", fl = 1)

    # -------------------------------------------------------------------------
    # METHODS

    def splitShape(self):
        newShapes = []
        for shape in self.shapes:
            newTrans = Dag_Node(m.createNode('transform', n=shape))
            m.parent(shape, newTrans, s=1)
            child = Dag_Node(newTrans.children[0])
            child.rename(newTrans.name).parentToWorld()
            newTrans.delete()
            newShapes.append(shape)

        self.delete()
        print(newShapes) ### DEL LATER          
        return newShapes

    def mergeShapeTo():
        pass
    
    # -----------------
    """
    import maya.cmds as mc

    for shape in mc.listRelatives(mc.ls(sl=1), c=1, type='shape'):
    newTrans = mc.createNode('transform', n='cvshape')
    mc.parent(shape, newTrans, s=1)
    
    """