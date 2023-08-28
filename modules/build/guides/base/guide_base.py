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

def find_guide_main():
    main_guide = m.ls("Guide")

    gMain = Dag(main_guide[0])

    return gMain

def find_guide_joints():
    gMain = find_guide_main()
    guide_joints = gMain.allChildren[1:]
    guide_joints = [Joint(i) for i in guide_joints]

    return guide_joints

def mirror_guide():
    """
    Find and mirror the guides on scene.
    """
    
    guide_joints = find_guide_joints()
    
    side = "L_"
    
    joints_to_mirror = []
    mirrored_joints = []

    for jnt in guide_joints:
        if jnt.name.startswith(side):
            if jnt.parent.name.startswith(side):
                continue
            else:
                if not m.objExists(jnt.name.replace(side, "R_")):
                    joints_to_mirror.append(jnt)
    
    if not joints_to_mirror:
        m.error(">>> There's nothing left to mirror")

    for jnt in joints_to_mirror:
        mirrored =  m.mirrorJoint(jnt, mirrorYZ = True, sr=["L_", "R_"])
        for i in  mirrored:
            mirrored_joints.append(i)

    mirrored_joints = [Joint(i) for i in mirrored_joints]

    for jnt in mirrored_joints:
        jnt.setLabelSide("R")
        
        # Setting the joint orientation
        m.select(jnt)

        if "eye"  in jnt.name or jnt.labelType:
            mel.eval("joint -e  -oj xzy -secondaryAxisOrient ydown -ch -zso;")
        else:
            mel.eval("joint -e  -oj xzy -secondaryAxisOrient zdown -ch -zso;")

        if not jnt.children and "heel" not in jnt.name:
            jnt.setJointOrient(0)


    m.select(cl = True) # Cleaning last selected object.

    return mirrored_joints

def toggle_guide_name():
    """
    toggles guide joints label visibility.

    To keep track of guides with displayable names a temporary
    attribute will be added.
    """
    guide_joints = find_guide_joints()

    for jnt in guide_joints:
        if jnt.labelVis:
            jnt.a.add(ln="LabelVis", nn="LabelVis", at="bool")
            jnt.setLabelVis(False)

        elif jnt.a.LabelVis.exists():
            jnt.setLabelVis(True)
            jnt.a.LabelVis.delete()

    pass

def toggle_guide_axis():
    guide_joints = find_guide_joints()

    for jnt in guide_joints:
        if jnt.localAxis:
            jnt.hideLocalAxis()
        else:
            jnt.showLocalAxis()
    pass