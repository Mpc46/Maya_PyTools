'''
/*****************************************************************************/
                                Mirror Guide v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Mirror existing guides functionality

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + mirror_guide [Function]

>> NOTES >> 
	Update 26/08/2023 : Start working on the script

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
from modules.base import Joint, Dag_Node as Dag

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


def mirror_guide():
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
