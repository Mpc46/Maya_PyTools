'''
/*****************************************************************************/
                             Build Guide v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Build rig from existing guides on scene.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> NOTES >> 
	Update 27/08/2023 : Started to work on the script.

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
from modules.build.guides import (mirror_guide, 
                                  find_guide_main,
                                  find_guide_joints)

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def build_guide():
    mirror_guide()
    build_guide_structure()
    pass


def build_guide_structure():
    guide_main = find_guide_main()

    rig_main = Dag("Rig", "transform")
    guide_main.parentTo(rig_main)

    joint_grp = generate_skeleton()
    joint_grp.parentTo(rig_main)

    geo_grp = Dag("Geometry", "transform")
    geo_grp.parentTo(rig_main)
    
    guide_main.hide()
    
    grps = [rig_main, joint_grp, geo_grp]
    return grps


def generate_skeleton():

    joint_grp = Dag("Skeleton", "transform")
    
    guide_joints = find_guide_joints()[::-1]
    bind_joints = []

    for jnt in guide_joints:
        # SETTING NEW JOINT 
        new_joint = Joint(m.joint(n=jnt.name, o = jnt.jointOrient))
        new_joint.setLabel(jnt.labelSide, jnt.labelType, False) # Setting Labels
        #new_joint.a.segmentScaleCompensate.set(0)

        # AVOIDING NAME COLLISIONS
        guide_suffix = "_guide"
        jnt.rename(jnt.name + guide_suffix) # Avoid same names
        if new_joint.parent != joint_grp:
            new_joint.parentTo(joint_grp)

        new_joint.moveTo(jnt)
        bind_joints.append(new_joint)

    bind_joints = [Joint(i) for i in bind_joints]

    # Recreating hierarchy
    for nJnt, gJnt in zip(bind_joints,guide_joints):
        if gJnt.parent:
            parent = str(gJnt.parent)[:-6]
            parent = parent.split("|")[-1]

            if parent == "Guide":
                m.parent(nJnt.name, joint_grp)
            else:
                m.parent(nJnt.name, parent)

    for jnt in bind_joints:
        labels = ["COG", "Root"]
        for label in labels:
            if label in jnt.labelType:
                jnt.parentTo(joint_grp)
        
    
    return joint_grp

# -----------------------------------------------------------------------------
# SYSTEMS
# -----------------------------------------------------------------------------
fingers = []

# -----------------------------------------------------------------------------
# BUILD SYSTEMS
# -----------------------------------------------------------------------------

