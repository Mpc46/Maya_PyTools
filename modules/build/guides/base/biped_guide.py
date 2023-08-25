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


# -------------------------------------------------------------------------
# LEG CREATE GUIDE

def leg_build_guide():
    hip_guide = Biped_Guide(m.joint(
                                n = "L_leg", 
                                p = [5.354, 54.665, 1.065],
                                o = [0, 0, -90.000]
                                    ))
    hip_guide.setLabel("L", "hip", True)

    knee_guide = Biped_Guide(m.joint(
                                n = "L_knee",
                                r = True, 
                                p = [23.519, 0, 0],
                                o = [0, 8.074, 0]
                                    ))
    knee_guide.setLabel("L", "knee", True)

    ankle_guide = Limbs_Guide(m.joint(
                                n = "L_ankle", 
                                r = True,
                                p = [26.302, 0, 0],
                                o = [0, 0, 0]
                                    ))
    ankle_guide.setLabel("L", "ankle", False)

    foot_build_guide()
    m.select(cl=True) # Deselect last created object

# -------------------------------------------------------------------------
# FOOT CREATE GUIDE

def foot_build_guide():
    foot_guide = Biped_Guide(m.joint(
                                n = "L_foot",
                                r = True, 
                                p = [0, 0, 0],
                                o = [-13.691, -64.119, 11.518]
                                    ))
    foot_guide.setLabel("L", "foot", True)

    toe_guide = Biped_Guide(m.joint(
                                n = "L_toe",
                                r = True, 
                                p = [6.533, 0, 0],
                                o = [0, -18.513, 0]
                                    ))
    toe_guide.setLabel("L", "toe", True)

    toeEnd_guide = Limbs_Guide(m.joint(
                                n = "L_toeEnd", 
                                r = True,
                                p = [5.904, 0, 0],
                                o = [0, 0, 0]
                                    ))
    toeEnd_guide.setLabel("L", "toeEnd", False)

    # -------------------------------------------------------------------------
    # HEEL
    m.select(foot_guide)

    heel_guide = Biped_Guide(m.joint(
                                n = "L_heel",
                                r = True, 
                                p = [0, 0, -6.064],
                                o = [3.929, -33.150, -7.159]
                                    ))
    heel_guide.setLabel("L", "heel", True)

    # -------------------------------------------------------------------------
    # FOOT IN
    m.select(toe_guide)

    foot_in_guide = Biped_Guide(m.joint(
                                n = "L_foot_in",
                                r = True, 
                                p = [0, -2.495, -1.462],
                                o = [1.817, -14.734, -7.112]
                                    ))
    foot_in_guide.setLabel("L", "Bank In", True)

    # -------------------------------------------------------------------------
    # FOOT OUT
    m.select(toe_guide)

    foot_out_guide = Biped_Guide(m.joint(
                                n = "L_foot_out",
                                r = True, 
                                p = [0, 2.832, -1.453],
                                o = [-2.377, -14.656, 9.316]
                                    ))
    foot_out_guide.setLabel("L", "Bank Out", True)

    m.select(cl=True) # Deselect last created object


# -------------------------------------------------------------------------
# ARM CREATE GUIDE

def arm_build_guide():
    clavicle_guide = Biped_Guide(m.joint(
                                n = "L_clavicle", 
                                p = [0.956, 82.173, -1.350],
                                o = [0, 0, 0]
                                    ))
    clavicle_guide.setLabel("L", "collar", True)

    shoulder_guide = Biped_Guide(m.joint(
                                n = "L_shoulder",
                                r = True, 
                                p = [9.566, 0, 0],
                                o = [0, 0.5, 0]
                                    ))
    shoulder_guide.setLabel("L", "shoulder", True)

    elbow_guide = Limbs_Guide(m.joint(
                                n = "L_elbow", 
                                r = True,
                                p = [13.595, 0, 0],
                                o = [0, -1, 0]
                                    ))
    elbow_guide.setLabel("L", "elbow", True)

    wrist_guide = Limbs_Guide(m.joint(
                                n = "L_wrist", 
                                r = True,
                                p = [13.518, 0, 0],
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
                                p = [37.634, 82.173, -1.350],
                                o = [0, 0, 0]
                                    ))
    hand_guide.setLabel("L", "hand", True)

    # -------------------------------------------------------------------------
    # INDEX FINGER

    index0_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_00",
                                r = True, 
                                p = [1.309, 0.075, 0.726],
                                o = [-0.623, -5.496, 3.016]
                                    ))
    index0_guide.setLabel("L", "index meta", False)

    index1_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_01",
                                r = True, 
                                p = [4, 0, 0],
                                o = [0.337, 7.605, -2.958]
                                    ))
    index1_guide.setLabel("L", "index finger", True)

    index2_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_02",
                                r = True, 
                                p = [1.981, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    index3_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_03",
                                r = True, 
                                p = [1.171, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    index4_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_04",
                                r = True, 
                                p = [1.399, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide)
    # -------------------------------------------------------------------------
    # MIDDLE FINGER

    middle0_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_00",
                                r = True, 
                                p = [1.267, 0.069, 0.084],
                                o = [0.048, 2.361, 3.104]
                                    ))
    middle0_guide.setLabel("L", "middle meta", False)

    middle1_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_01",
                                r = True, 
                                p = [4, 0, 0],
                                o = [0.080, -0.229, -3.101]
                                    ))
    middle1_guide.setLabel("L", "middle finger", True)

    middle2_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_02",
                                r = True, 
                                p = [1.974, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    middle3_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_03",
                                r = True, 
                                p = [1.476, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    middle4_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_04",
                                r = True, 
                                p = [2, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide)
    # -------------------------------------------------------------------------
    # RING FINGER

    ring0_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_00",
                                r = True, 
                                p = [1.242, 0.072, -0.599],
                                o = [0.700, 8.714, 3.089]
                                    ))
    ring0_guide.setLabel("L", "ring meta", False)

    ring1_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_01",
                                r = True, 
                                p = [4, 0.039, -0.189],
                                o = [-0.233, -6.259, -3.028]
                                    ))
    ring1_guide.setLabel("L", "ring finger", True)

    ring2_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_02",
                                r = True, 
                                p = [1.939, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    ring3_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_03",
                                r = True, 
                                p = [1.397, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    ring4_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_04",
                                r = True, 
                                p = [1.425, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide)
    # -------------------------------------------------------------------------
    # PINKY FINGER

    pinky0_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_00",
                                r = True, 
                                p = [1.125, 0.086, -1.244],
                                o = [1.433, 15.996, 3.235]
                                    ))
    pinky0_guide.setLabel("L", "pinky meta", False)

    pinky1_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_01",
                                r = True, 
                                p = [3.673, 0, 0],
                                o = [-0.556, -14.015, -2.975]
                                    ))
    pinky1_guide.setLabel("L", "pinky finger", True)

    pinky2_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_02",
                                r = True, 
                                p = [1.476, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    pinky3_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_03",
                                r = True, 
                                p = [0.905, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    pinky4_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_04",
                                r = True, 
                                p = [1.293, 0, 0],
                                o = [0, 0, 0]
                                    ))
    
    # -------------------------------------------------------------------------
    m.select(hand_guide)
    # -------------------------------------------------------------------------
    # THUMB FINGER

    thumb0_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_01",
                                r = True, 
                                p = [1.466, -0.811, 1.164],
                                o = [45.544, -32.643, -22.500]
                                    ))
    thumb0_guide.setLabel("L", "thumb meta", False)

    thumb1_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_01",
                                r = True, 
                                p = [2.276, 0, 0],
                                o = [0, 0, -1.957]
                                    ))
    thumb1_guide.setLabel("L", "thumb", True)

    thumb2_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_02",
                                r = True, 
                                p = [1.551, 0, 0],
                                o = [0, 0, -2.389]
                                    ))
    
    thumb3_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_03",
                                r = True, 
                                p = [1.730, 0, 0],
                                o = [0, 0, 0]
                                    ))
    

    m.select(cl=True) # Deselect last created object

# :3