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
    create_rig_structure _summary_
    """
    # MAIN HIERARCHY

    main_grp = Dag_Node("Rig", "transform")

    systems_grp = Dag_Node("Systems", "transform")
    systems_grp.parentTo(main_grp)

    controls_grp = Dag_Node("Controls", "transform")
    controls_grp.parentTo(main_grp)

    skeleton_grp = Dag_Node("Skeleton", "transform")
    skeleton_grp.parentTo(main_grp)

    geo_grp = Dag_Node("Geometry", "transform")
    geo_grp.parentTo(main_grp)

    # SUB-SYSTEMS HIERARCHY
    Fk_grp = Dag_Node("FkSystem", "transform")
    Fk_grp.parentTo(systems_grp)

    ik_grp = Dag_Node("IkSystem", "transform")
    ik_grp.parentTo(systems_grp)
    pass


# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

create_rig_structure()