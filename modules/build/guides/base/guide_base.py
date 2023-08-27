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
from maya import mel
from modules.base import Joint, Curve, Dag_Node as Dag

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Guide_Main(Curve):
    """
    Ctl_Guide The main control and filter to identify guides.
    """
    def __init__(self, node, **kwargs):
        super().__init__(node, **kwargs)

    pass


class Base_Guide(Joint):
    """
    Base guide for setting up common attributes and behaviour.
    """

    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node=None, **kwargs):
        super().__init__(node, **kwargs)

        self.a.add(ln="PtmMadre", nn="Base", at="float", k=True)

    pass

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


def mirror_guide():
    """
    Find and mirror the guides on scene.
    """
    main_guide = m.ls("Guide")

    gMain = Dag(main_guide[0])
    side = "L_"
    guide_joints = gMain.allChildren[1:]
    guide_joints = [Joint(i) for i in guide_joints]
   
    joints_to_mirror = []
    mirrored_joints = []

    for jnt in guide_joints:
        if jnt.name.startswith(side):
            if jnt.parent.name.startswith(side):
                continue
            else:
                joints_to_mirror.append(jnt)
    
    for jnt in joints_to_mirror:
        mirrored =  m.mirrorJoint(jnt, mirrorYZ = True, sr=["L_", "R_"])
        for i in  mirrored:
            mirrored_joints.append(i)

    mirrored_joints = [Joint(i) for i in mirrored_joints]

    for jnt in mirrored_joints:
        jnt.setLabelSide("R")
        m.select(jnt)
        mel.eval("joint -e  -oj xzy -secondaryAxisOrient zdown -ch -zso;")

    return mirrored_joints

#mirror_guide()

# joint -e  -oj xzy -secondaryAxisOrient zup -ch -zso;