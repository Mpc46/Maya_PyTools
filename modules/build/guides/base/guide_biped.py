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
from modules.build import Guide_Main as gMain

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Biped_Guide(Guide):
    def __init__(self, node=None):
        super().__init__(node)

        self.a.s.lockHide()

        #self.setColor("yellow")
        self.a.add(ln="Ground_1", nn="Biped", at="float", k=True)

    def build(self):
        main_ctl = gMain(m.circle(n="Guide", r=20, nr=[0,1,0])[0])
        main_ctl.setColor("cyan")
        cog_build_guide()
        self.delete()


class Spine_Guide(Biped_Guide):
    def __init__(self, node=None):
        super().__init__(node)

        # Locking related Attributes
        self.a.ty.lockHide()
        self.a.r.lockHide()
        self.a.ry.unlockShow()
    
    def base_spine(self):
        """ They follow their own rules"""
        self.a.ty.unlockShow()
        self.a.tx.lockHide()


class Limbs_Guide(Biped_Guide):
    def __init__(self, node=None):
        super().__init__(node)

        self.a.add(ln="Ground_2", nn="Limb", at="float", k=True)


class Hand_Guide(Biped_Guide):
    def __init__(self, node=None):
        super().__init__(node)

    def build(self):
        hand_build_guide()


# -------------------------------------------------------------------------
# COG CREATE GUIDE
def cog_build_guide():
    cog_guide = Biped_Guide(m.joint(
                                n = "COG", 
                                p = [0, 60.584, 1.065],
                                o = [0, 0, 0]
                                    ))
    
    spine_build_guide()

    m.select(cog_guide)

    hip_build_guide()

    m.select(cl=True)

# -------------------------------------------------------------------------
# SPINE CREATE GUIDE

def spine_build_guide():
    spine1_guide = Spine_Guide(m.joint(
                                n = "spine_01", 
                                p = [0, 60.584, 1.065],
                                o = [0, 0, 90]
                                    ))
    spine1_guide.setLabel("C", "spine", True)
    spine1_guide.base_spine()

    spine2_guide = Spine_Guide(m.joint(
                                n = "spine_02",
                                r = True, 
                                p = [6.964, 0, 0],
                                o = [0, 0, 0]
                                    ))
    spine2_guide.setLabel("C", "spine mid", False)
   
    chest_guide = Spine_Guide(m.joint(
                                n = "chest", 
                                r = True,
                                p = [6.964, 0, 0],
                                o = [0, 0, 0]
                                    ))
    chest_guide.setLabel("C", "Chest", True)

    neck_build_guide()

    m.select(chest_guide)
    arm_build_guide()

    m.select(cl=True)

# -------------------------------------------------------------------------
# NECK & HEAD CREATE GUIDES

def neck_build_guide():
    neck1_guide = Spine_Guide(m.joint(
                                n = "neck_01", 
                                p = [0, 83.666, 0.127],
                                o = [0, -6.231, 0]
                                    ))
    neck1_guide.setLabel("C", "neck", True)
    
    neck2_guide = Spine_Guide(m.joint(
                                n = "neck_02",
                                r = True, 
                                p = [4.242, 0, 0],
                                o = [0, 0, 0]
                                    ))
    neck2_guide.setLabel("C", "neck mid", False)

    neck3_guide = Spine_Guide(m.joint(
                                n = "neck_03",
                                r = True, 
                                p = [4.242, 0, 0],
                                o = [0, 0, 0]
                                    ))
    neck3_guide.setLabel("C", "neck end", False)

    
    head_guide = Spine_Guide(m.joint(
                                n = "head",
                                r = True, 
                                p = [0, 0, 0],
                                o = [0, 0, 0]
                                    ))
    head_guide.setLabel("C", "head", True)

    # ------- JAW -------

    jaw0_guide = Spine_Guide(m.joint(
                                n = "jaw_00",
                                r = True, 
                                p = [1.090, 0, 0.378],
                                o = [0, 216.241, 0]
                                    ))
    jaw0_guide.setLabel("C", "Jaw Swing", False)
    
    jaw1_guide = Spine_Guide(m.joint(
                                n = "jaw_01",
                                r = True, 
                                p = [2.501, 0, 0],
                                o = [0, 48.909, 0]
                                    ))
    jaw1_guide.setLabel("C", "jaw", True)
    
    chin_guide = Spine_Guide(m.joint(
                                n = "chin",
                                r = True, 
                                p = [5.843, 0, 0],
                                o = [0, 0, 0]
                                    ))
    chin_guide.setLabel("C", "jaw end", False)

    
    # -------------------------------------------------------------------------
    m.select(head_guide) # HEAD END
    # -------------------------------------------------------------------------

    headEnd_guide = Spine_Guide(m.joint(
                                n = "headEnd",
                                r = True, 
                                p = [13.052, 0, 0],
                                o = [0, 0, 0]
                                    ))
    headEnd_guide.setLabel("C", "head end", False)

    # -------------------------------------------------------------------------
    m.select(head_guide) # EYES
    # -------------------------------------------------------------------------

    eye_guide = Biped_Guide(m.joint(
                                n = "L_eye",
                                r = True, 
                                p = [5.049, -2.172, 3.784],
                                o = [-148.245, -76.850, -31.832]
                                    ))
    eye_guide.setLabel("L", "eye", True)
    eye_guide.a.rx.lock()

    eyeEnd_guide = Biped_Guide(m.joint(
                                n = "L_eyeEnd",
                                r = True, 
                                p = [2.472, 0, 0],
                                o = [0, 0, 0]
                                    ))
    eyeEnd_guide.setLabel("L", "eye end", False)
    eyeEnd_guide.a.rx.lock()
    
    m.select(cl=True) # Deselect last created object

# -------------------------------------------------------------------------
# HIP CREATE GUIDE

def hip_build_guide():
    hip_guide = Spine_Guide(m.joint(
                                n = "hip",
                                r = True, 
                                p = [0, 0, 0],
                                o = [0, 0, -90]
                                    ))
    hip_guide.setLabel("C", "hip swing", False)
    hip_guide.base_spine()

    hipEnd_guide = Spine_Guide(m.joint(
                                n = "hipEnd",
                                r = True, 
                                p = [5.919, 0, 0],
                                o = [0, 0, 0]
                                    ))
    hipEnd_guide.setLabel("C", "hip", True)

    leg_build_guide()

# -------------------------------------------------------------------------
# LEG CREATE GUIDE

def leg_build_guide():
    leg_guide = Limbs_Guide(m.joint(
                                n = "L_leg", 
                                r = True,
                                p = [0, 5.354, 0],
                                o = [0, 0, 0]
                                    ))
    leg_guide.setLabel("L", "hip", True)

    knee_guide = Limbs_Guide(m.joint(
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
                                p = [0.025, -2.495, -1.558],
                                o = [1.310, -14.786, -5.124]
                                    ))
    foot_in_guide.setLabel("L", "Bank In", True)

    toe_in_guide = Biped_Guide(m.joint(
                                n = "L_bigToe",
                                r = True, 
                                p = [5.302, 0, 0],
                                o = [0, 0, 0]
                                    ))
    toe_in_guide.setLabel("L", "big toe", True)

    # -------------------------------------------------------------------------
    # FOOT OUT
    m.select(toe_guide)

    foot_out_guide = Biped_Guide(m.joint(
                                n = "L_foot_out",
                                r = True, 
                                p = [0.028, 2.832, -1.558],
                                o = [-2.377, -14.656, 9.316]
                                    ))
    foot_out_guide.setLabel("L", "Bank Out", True)

    toe_out_guide = Biped_Guide(m.joint(
                                n = "L_pinkyToe",
                                r = True, 
                                p = [3.241, 0, 0],
                                o = [0, 0, 0]
                                    ))
    toe_out_guide.setLabel("L", "pinky toe", True)

    m.select(cl=True) # Deselect last created object


# -------------------------------------------------------------------------
# ARM CREATE GUIDE

def arm_build_guide():
    clavicle_guide = Limbs_Guide(m.joint(
                                n = "L_clavicle", 
                                p = [0.956, 82.173, -1.350],
                                o = [0, 0, -90]
                                    ))
    clavicle_guide.setLabel("L", "collar", True)

    shoulder_guide = Limbs_Guide(m.joint(
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
    index2_guide.setLabel("L", "index finger", False)
    
    index3_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_03",
                                r = True, 
                                p = [1.171, 0, 0],
                                o = [0, 0, 0]
                                    ))
    index3_guide.setLabel("L", "index finger", False)
    
    index4_guide = Hand_Guide(m.joint(
                                n = "L_indexFinger_04",
                                r = True, 
                                p = [1.399, 0, 0],
                                o = [0, 0, 0]
                                    ))
    index4_guide.setLabel("L", "index finger end", False)
    
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
    middle2_guide.setLabel("L", "middle finger", False)
    
    middle3_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_03",
                                r = True, 
                                p = [1.476, 0, 0],
                                o = [0, 0, 0]
                                    ))
    middle3_guide.setLabel("L", "middle finger", False)
    
    middle4_guide = Hand_Guide(m.joint(
                                n = "L_middleFinger_04",
                                r = True, 
                                p = [2, 0, 0],
                                o = [0, 0, 0]
                                    ))
    middle4_guide.setLabel("L", "middle finger end", False)
    
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
    ring2_guide.setLabel("L", "ring finger", False)

    
    ring3_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_03",
                                r = True, 
                                p = [1.397, 0, 0],
                                o = [0, 0, 0]
                                    ))
    ring3_guide.setLabel("L", "ring finger", False)
    
    ring4_guide = Hand_Guide(m.joint(
                                n = "L_ringFinger_04",
                                r = True, 
                                p = [1.425, 0, 0],
                                o = [0, 0, 0]
                                    ))
    ring4_guide.setLabel("L", "ring finger end", False)
    
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
    pinky2_guide.setLabel("L", "pinky finger", False)
    
    pinky3_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_03",
                                r = True, 
                                p = [0.905, 0, 0],
                                o = [0, 0, 0]
                                    ))
    pinky3_guide.setLabel("L", "pinky finger", False)
    
    pinky4_guide = Hand_Guide(m.joint(
                                n = "L_pinkyFinger_04",
                                r = True, 
                                p = [1.293, 0, 0],
                                o = [0, 0, 0]
                                    ))
    pinky4_guide.setLabel("L", "pinky finger end", False)
    
    # -------------------------------------------------------------------------
    m.select(hand_guide)
    # -------------------------------------------------------------------------
    # THUMB FINGER

    thumb0_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_00",
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
    thumb2_guide.setLabel("L", "thumb", False)
    
    thumb3_guide = Hand_Guide(m.joint(
                                n = "L_thumbFinger_03",
                                r = True, 
                                p = [1.730, 0, 0],
                                o = [0, 0, 0]
                                    ))
    thumb3_guide.setLabel("L", "thumb end", False)
    

    m.select(cl=True) # Deselect last created object

# :3