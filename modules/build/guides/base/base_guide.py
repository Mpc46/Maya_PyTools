'''
/*****************************************************************************/
                                Base Guide v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Base guide class to set global parameters that affect all guides.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Window_Base [Class]

>> NOTES >> 
	Update 22/08/2023 : Start working on the script

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.base import Joint
# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Base_Guide(Joint):
    """
    XD
    """

    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node=None, **kwargs):
        super().__init__(node, **kwargs)

        self.a.add(ln="PtmMadre", nn="Base", at="float", k=True)