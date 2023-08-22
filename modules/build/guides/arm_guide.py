'''
/*****************************************************************************/
                                Arm Guide v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Arm guide.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Arm_Guide [Class]

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
from modules.build import Base_Guide as Guide

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Arm_Guide(Guide):
    def __init__(self, node=None):
        super().__init__(node)

        self.a.add(ln="AsuPtmMadre", nn="Arm", at="float", k=True)

    def build(self):
        arm_build()

def arm_build():
    clavicle_guide = Guide(m.joint(
                                n = "L_clavicle", 
                                p = [0.12, 14.376, -0.102],
                                o = [0, 2, 0]
                                    ))
    clavicle_guide.setLabel("L", "collar", True)

    shoulder_guide = Guide(m.joint(
                                n = "L_shoulder",
                                r = True, 
                                p = [1.584, 0, 0],
                                o = [0, 0, 0]
                                    ))
    shoulder_guide.setLabel("L", "shoulder", True)

    elbow_guide = Arm_Guide(m.joint(
                                n = "L_elbow", 
                                r = True,
                                p = [2.646, 0, 0],
                                o = [0, -4, 0]
                                    ))
    elbow_guide.setLabel("L", "elbow", False)

    wrist_guide = Arm_Guide(m.joint(
                                n = "L_wrist", 
                                r = True,
                                p = [2.259, 0, 0],
                                o = [0, 0, 0]
                                    ))
    wrist_guide.setLabel("L", "wrist", False)

class Hand_Guide(Guide):
    def __init__(self):
        super().__init__()