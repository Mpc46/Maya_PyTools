'''
/*****************************************************************************/
                                Arm Guide v 1.0
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
from modules.build import Base_Guide

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Arm_Guide(Base_Guide):
    def __init__(self):
        super().__init__()

class Hand_Guide(Base_Guide):
    def __init__(self):
        super().__init__()