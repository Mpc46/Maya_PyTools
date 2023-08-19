'''
/*****************************************************************************/
                            Joint Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Class based approach to work with joints and their properties.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Joint [Class] (Inherits from Dag_Node)

>> NOTES >> 
	Update 11/08/2023 : Started to work on the script.
    Update 12/08/2023 : Added joint label functionality.

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
    # METHODS


    # -----------------