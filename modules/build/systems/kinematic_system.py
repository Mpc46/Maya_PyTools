'''
/*****************************************************************************/
                            Kinematic System v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Module contains functions related to the creation of a blend/switch
    system, creating IK and FK chains from a list of joints. 

>> HOW TO USE >>
	This library is meant to be imported into larger scripts and/or
    hold those scripts and modules for later use or implementation.
    
>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''
# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.base import Joint, Dep_Node, Dag_Node, Curve
from modules.utils.common import duplicateChain
from modules.common.names import NODES_DICT

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


def switch(joints=[], switch_ctl=None):
    
    blendColor = NODES_DICT["blendColors"]

    joints = [Joint(i) for i in joints]

    if not switch_ctl:
        switchName = (joints[-1].name) + "_switch_CTL"
        switch_ctl = Dag_Node(m.circle(n=switchName)[0])

        switch_ctl.setColor("yellow").moveTo(joints[-1].name)
        switch_ctl.createOffset(1)
        switch_ctl.a.add(ln="blend", nn="FK/IK", at="float", 
                         min=0, max=1, dv=0, k=True)

    ik_joints = duplicateChain(joints, "_IK")
    fk_joints = duplicateChain(joints, "_FK")

    for jnt in joints:
        jnt.setColor("green")

        blendRotName = "{}_{}_ROT".format(jnt.name, blendColor)
        blendRot = Dep_Node(m.createNode("blendColors", n=blendRotName))
        jnt.a.r << blendRot.a.output
        switch_ctl.a.blend >> blendRot.a.blender

        blendTraName = "{}_{}_TRA".format(jnt.name, blendColor)
        blendTra = Dep_Node(m.createNode("blendColors", n=blendTraName))
        jnt.a.t << blendTra.a.output
        switch_ctl.a.blend >> blendTra.a.blender

        for ik in ik_joints:
            ik.setColor("red")

            if ik.name.split("_")[0:2] == blendTra.name.split("_")[0:2]:
                if not blendTra.a.color1.connectionInput:
                    ik.a.t >> blendTra.a.color1

            if ik.name.split("_")[0:2] == blendRot.name.split("_")[0:2]:
                if not blendRot.a.color1.connectionInput:
                    ik.a.r >> blendRot.a.color1

        for fk in fk_joints:
            fk.setColor("blue")

            if fk.name.split("_")[0:2] == blendTra.name.split("_")[0:2]:
                if not blendTra.a.color2.connectionInput:
                    fk.a.t >> blendTra.a.color2

            if fk.name.split("_")[0:2] == blendRot.name.split("_")[0:2]:
                if not blendRot.a.color2.connectionInput:
                    fk.a.r >> blendRot.a.color2

    fk_joints = fk_system(fk_joints)
    m.select(clear=True)


def fk_system(joints=[]):
    joints = [Joint(i) for i in joints]
    ctrls = []

    for jnt in joints:
        ctlName = "{}_Ctl".format(jnt)
        ctl = Curve(m.circle(n=ctlName, normal = (1,0,0))[0])
        ctl.moveTo(jnt)
        ctl.parentConstraint(jnt, mo=True)

        ctrls.append(ctl)

        ctl_index = ctrls.index(ctl.name)

        if ctl_index != 0:
            ctl.parentTo(ctrls[ctl_index - 1])
        
        ctl.createOffset(1)

    return [joints, ctrls]


def ik_system(joints=[]):
    joints = [Joint(i) for i in joints]


    
    pass

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------





