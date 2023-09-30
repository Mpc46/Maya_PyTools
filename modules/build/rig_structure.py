'''
/*****************************************************************************/
                            Rig Structure v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Main rigging system structure to use on automated systems

>> HOW TO USE >>
    This module contents are intended to be imported, referenced or
    inheritance to another class.

>> NOTES >> 
	Update 10/09/2023 : Started to work on the script.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------
from maya import cmds as m
from modules.base import Dag_Node

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def create_rig_structure():
    """
    creates the basic rig folder and component structure to use.
    """
    if  m.objExists("Rig"):
        return Dag_Node("Rig")
    
    # -----------------------------------------------------------------------------
    # MAIN HIERARCHY

    main_grp = Dag_Node("Rig", "transform")

    systems_grp = Dag_Node("Systems", "transform")
    systems_grp.parentTo(main_grp)

    skeleton_grp = Dag_Node("Skeleton", "transform")
    skeleton_grp.parentTo(main_grp)

    geo_grp = Dag_Node("Geometry", "transform")
    geo_grp.parentTo(main_grp)

    # -----------------------------------------------------------------------------
    # SUB-SYSTEMS HIERARCHY

    # ----- FK SYSTEM ----- 

    Fk_grp = Dag_Node("FkSystem", "transform")
    Fk_grp.parentTo(systems_grp)

    fk_jnt_grp = Dag_Node("FkJoints", "transform")
    fk_jnt_grp.parentTo(Fk_grp)

    fk_ctl_grp = Dag_Node("FkControls", "transform")
    fk_ctl_grp.parentTo(Fk_grp)

    # ----- IK SYSTEM ----- 

    ik_grp = Dag_Node("IkSystem", "transform")
    ik_grp.parentTo(systems_grp)

    ik_jnt_grp = Dag_Node("IkJoints", "transform")
    ik_jnt_grp.parentTo(ik_grp)

    ik_ctl_grp = Dag_Node("IkControls", "transform")
    ik_ctl_grp.parentTo(ik_grp)

    # ----- GEAR SYSTEM ----- 

    gear_grp = Dag_Node("GearSystem", "transform")
    gear_grp.parentTo(systems_grp)
    
    # -----------------------------------------------------------------------------
    # SETS

    m.select(clear=True)
    
    m.sets(n = "ControlSet")
    m.sets(n = "SkeletonSet")
    m.sets( "ControlSet", "SkeletonSet", n="RigSet" )
    
    return main_grp
