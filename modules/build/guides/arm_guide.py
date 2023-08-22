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
from modules.build import Base_Guide as Guide

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Arm_Guide(Guide):
    def __init__(self, node=None):
        super().__init__(node)

        self.a.add(ln="AsuPtmMadre", nn="Arm", at="float", k=True)

    def build(self):
        arm_build_guide()

# -------------------------------------------------------------------------

def arm_build_guide():
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
                                o = [0, -2, 0]
                                    ))
    elbow_guide.setLabel("L", "elbow", False)

    wrist_guide = Arm_Guide(m.joint(
                                n = "L_wrist", 
                                r = True,
                                p = [2.259, 0, 0],
                                o = [0, 0, 0]
                                    ))
    wrist_guide.setLabel("L", "wrist", False)

    hand_build_guide()
    
# -------------------------------------------------------------------------
class Hand_Guide(Guide):
    def __init__(self, node=None):
        super().__init__(node)

    def build(self):
        hand_build_guide()

# -------------------------------------------------------------------------

def hand_build_guide():
    hand_guide = Hand_Guide(m.joint(
                                n = "L_hand", 
                                p = [6.603, 14.376, -0.25],
                                o = [0, 0, 0]
                                    ))
    hand_guide.setLabel("L", "hand", True)

    # -------------------------------------------------------------------------
    # INDEX FINGER

    index1_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_01",
                                r = True, 
                                p = [0.908, 0.033, 0.21],
                                o = [0, 2.233, 0]
                                    ))
    index1_guide.setLabel("L", "index finger", True)

    index2_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_02",
                                r = True, 
                                p = [0.312, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    index3_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_03",
                                r = True, 
                                p = [0.203, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    index4_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_04",
                                r = True, 
                                p = [0.272, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide.name)
    # -------------------------------------------------------------------------
    # MIDDLE FINGER

    middle1_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_01",
                                r = True, 
                                p = [0.863, 0.055, -0.002],
                                o = [0, 0.901, 0]
                                    ))
    middle1_guide.setLabel("L", "middle finger", True)

    middle2_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_02",
                                r = True, 
                                p = [0.406, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    middle3_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_03",
                                r = True, 
                                p = [0.256, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    middle4_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_04",
                                r = True, 
                                p = [0.307, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide.name)
    # -------------------------------------------------------------------------
    # RING FINGER

    ring1_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_01",
                                r = True, 
                                p = [0.831, 0.039, -0.189],
                                o = [0, 2.265, 0]
                                    ))
    ring1_guide.setLabel("L", "ring finger", True)

    ring2_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_02",
                                r = True, 
                                p = [0.233, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    ring3_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_03",
                                r = True, 
                                p = [0.233, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    ring4_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_04",
                                r = True, 
                                p = [0.266, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide.name)
    # -------------------------------------------------------------------------
    # PINKY FINGER

    pinky1_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_01",
                                r = True, 
                                p = [0.755, 0.032, -0.368],
                                o = [0, 2.796, 0]
                                    ))
    pinky1_guide.setLabel("L", "pinky finger", True)

    pinky2_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_02",
                                r = True, 
                                p = [0.261, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    pinky3_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_03",
                                r = True, 
                                p = [0.154, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    pinky4_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_04",
                                r = True, 
                                p = [0.235, 0, 0],
                                o = [0, 0, 0]
                                    ))
