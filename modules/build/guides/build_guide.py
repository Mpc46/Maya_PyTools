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
                                  find_guide_main)

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
    geo_grp = Dag("Geometry", "transform")
    geo_grp.parentTo(rig_main)
    joint_grp = Dag("Skeleton", "transform")
    joint_grp.parentTo(rig_main)

    
    pass


# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

