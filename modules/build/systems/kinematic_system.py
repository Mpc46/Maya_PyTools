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
from modules.build.rig_structure import create_rig_structure

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


def switch(joints=[], switch_ctl=None):
    create_rig_structure()
    blendColor = NODES_DICT["blendColors"]

    joints = [Joint(i) for i in joints]

    if switch_ctl is None:
        switchName = (joints[-1].name) + "_switch_Ctl"
        switch_ctl = Curve.gear(switchName)
        switch_ctl.switch(joints[-1].name)

        switch_ctl.offset.parentTo("GearSystem")
        m.sets( switch_ctl.name, add="ControlSet" ) # Add to set

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

    ik_joints = ik_system(ik_joints)
    m.select(clear=True)

    # -----------------------------------------------------------------------------
    # Set visibility

    # CREATE REVERSE NODE
    reverse_name = switch_ctl.name.replace("Ctl", "Rv")
    reverse_node = Dag_Node(reverse_name, "reverse")
    switch_ctl.a.blend >> reverse_node.a.inputX

    # IK VISIBILITY
    ik_joints_grp = ik_joints[0]
    ik_controls_grp = ik_joints[1]
    switch_ctl.a.blend >> ik_joints_grp.a.v
    switch_ctl.a.blend >> ik_controls_grp.a.v
    
    # FK VISIBILITY
    fk_joints_grp = fk_joints[0]
    fk_controls_grp = fk_joints[1]
    reverse_node.a.outputX >> fk_joints_grp.a.v 
    reverse_node.a.outputX >> fk_controls_grp.a.v

    # Add to main  hierarchy
    joints[0].parentTo("Skeleton")
    m.sets( (i for i in joints), add="SkeletonSet" ) # Add to set

    m.select(clear=True)


def fk_system(joints=[]):
    create_rig_structure()
    joints = [Joint(i) for i in joints]
    ctrls = []

    for jnt in joints:
        ctlName = "{}_Ctl".format(jnt.name)
        ctl = Curve(m.circle(n=ctlName, normal = (1,0,0))[0])
        ctl.moveTo(jnt)
        ctl.parentConstraint(jnt, mo=True)
        ctl.setColor("blue")

        jnt_rad = jnt.radius
        jnt.setRadius(jnt_rad * .75)

        ctrls.append(ctl)
        m.sets( ctl.name, add="ControlSet" ) # Add to set

        ctl_index = ctrls.index(ctl.name)

        if ctl_index > 0:
            ctl.parentTo(ctrls[ctl_index -1 ])
        
        ctl.createOffset(1)
    
    # Add to main  hierarchy 
    jnt_ofs_name = joints[0].name + "_Jnt_Grp"
    jnt_ofs  = Dag_Node(jnt_ofs_name, "transform")
    jnt_ofs.parentTo("FkJoints")
    joints[0].parentTo(jnt_ofs)

    ctl_ofs_name = joints[0].name + "_Ctl_Grp"
    ctl_ofs = Dag_Node(ctl_ofs_name, "transform")
    ctl_ofs.parentTo("FkControls")
    ctrls[0].parent.parentTo(ctl_ofs)
    
    return [jnt_ofs, ctl_ofs]


def ik_system(joints=[]):
    create_rig_structure()
    joints = [Joint(i) for i in joints]
    ctrls = []

    for jnt in joints:
        jnt_rad = jnt.radius
        jnt.setRadius(jnt_rad * .5)

    ikh = Dag_Node(m.ikHandle(sj= joints[0], ee=joints[-1], n=joints[-1].name + "_Ikh")[0])
    ikh_ctl = Curve(m.circle(n=joints[-1].name + "_Ctl", normal = (1,0,0))[0])

    ikh_ctl.moveTo(ikh)
    ikh_ctl.createOffset(1)
    ikh_ctl.setColor("red")
    ikh.parentTo(ikh_ctl)
    ikh.hide()
    
    poleVecor_ctl = Curve(m.circle(n=joints[1].name + "_Ctl", normal = (0,0,1))[0])
    poleVecor_ctl.moveTo(joints[1])
    poleVecor_ctl.createOffset(1)
    poleVecor_ctl.setColor("red")

    poleVecor_ctl.parent.a.tz.set(-5)
    m.poleVectorConstraint(poleVecor_ctl, ikh)

    ctrls.append(ikh_ctl)
    ctrls.append(poleVecor_ctl)
    m.sets( (i for i in ctrls), add="ControlSet" ) # Add to set
    
    # Add to main  hierarchy
    jnt_ofs_name = joints[0].name + "_Jnt_Grp"
    jnt_ofs  = Dag_Node(jnt_ofs_name, "transform")
    jnt_ofs.parentTo("IkJoints")
    joints[0].parentTo(jnt_ofs)

    ctl_ofs_name = joints[0].name + "_Ctl_Grp"
    ctl_ofs = Dag_Node(ctl_ofs_name, "transform")
    ctl_ofs.parentTo("IkControls")

    ikh_ctl.parent.parentTo(ctl_ofs)
    poleVecor_ctl.parent.parentTo(ctl_ofs)
    
    return [jnt_ofs, ctl_ofs]

