'''
/*****************************************************************************/
                                Biped Guide v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Biped guide.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Biped_Guide [Class]

>> NOTES >> 
	Update 23/08/2023 : Start working on the script

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

class Biped_Guide(Guide):
    def __init__(self, node=None):
        super().__init__(node)

        self.setColor("cyan")
        self.a.add(ln="Ground_1", nn="Biped", at="float", k=True)

    def build(self):
        arm_build_guide()
        leg_build_guide()


class Limbs_Guide(Biped_Guide):
    def __init__(self, node=None):
        super().__init__(node)

        self.a.add(ln="Ground_2", nn="Limb", at="float", k=True)


class Hand_Guide(Guide):
    def __init__(self, node=None):
        super().__init__(node)

    def build(self):
        hand_build_guide()


# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


# -------------------------------------------------------------------------
# LEG CREATE GUIDE

def leg_build_guide():
    hip_guide = Biped_Guide(m.joint(
                                n = "L_leg", 
                                p = [0.886, 9.199, 0.156],
                                o = [0, -0.815, -90.000]
                                    ))
    hip_guide.setLabel("L", "hip", True)

    knee_guide = Biped_Guide(m.joint(
                                n = "L_knee",
                                r = True, 
                                p = [4.193, 0, 0],
                                o = [0, 10.577, 0]
                                    ))
    knee_guide.setLabel("L", "knee", True)

    ankle_guide = Limbs_Guide(m.joint(
                                n = "L_ankle", 
                                r = True,
                                p = [4.210, 0, 0],
                                o = [0, 0, 0]
                                    ))
    ankle_guide.setLabel("L", "ankle", False)

    m.select(cl=True) # Deselect last created object

# -------------------------------------------------------------------------
# ARM CREATE GUIDE

def arm_build_guide():
    clavicle_guide = Biped_Guide(m.joint(
                                n = "L_clavicle", 
                                p = [0.12, 14.376, -0.102],
                                o = [0, 2, 0]
                                    ))
    clavicle_guide.setLabel("L", "collar", True)

    shoulder_guide = Biped_Guide(m.joint(
                                n = "L_shoulder",
                                r = True, 
                                p = [1.584, 0, 0],
                                o = [0, 0, 0]
                                    ))
    shoulder_guide.setLabel("L", "shoulder", True)

    elbow_guide = Limbs_Guide(m.joint(
                                n = "L_elbow", 
                                r = True,
                                p = [2.646, 0, 0],
                                o = [0, -2, 0]
                                    ))
    elbow_guide.setLabel("L", "elbow", True)

    wrist_guide = Limbs_Guide(m.joint(
                                n = "L_wrist", 
                                r = True,
                                p = [2.259, 0, 0],
                                o = [0, 0, 0]
                                    ))
    wrist_guide.setLabel("L", "wrist", False)

    hand_build_guide()
    m.select(cl=True) # Deselect last created object


# -------------------------------------------------------------------------
# HAND CREATE GUIDE

def hand_build_guide():
    hand_guide = Hand_Guide(m.joint(
                                n = "L_hand", 
                                p = [6.606, 14.376, -0.25],
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
    
    # -------------------------------------------------------------------------
    m.select(hand_guide.name)
    # -------------------------------------------------------------------------
    # THUMB FINGER

    thumb1_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_01",
                                r = True, 
                                p = [0.098, -0.155, 0.046],
                                o = [-32.447, -44.969, -14.663]
                                    ))
    thumb1_guide.setLabel("L", "thumb", True)

    thumb2_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_02",
                                r = True, 
                                p = [0.560, 0, 0],
                                o = [3.695, 17.328, 0.981]
                                    ))
    
    thumb3_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_03",
                                r = True, 
                                p = [0.321, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    thumb4_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_04",
                                r = True, 
                                p = [0.313, 0, 0],
                                o = [0, 0, 0]
                                    ))

    m.select(cl=True) # Deselect last created object