'''
/*****************************************************************************/
                            Guides Modules
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    This library contains modules for building rigging guides.

>> HOW TO USE >>
	This library is meant to be imported into larger scripts and/or
    hold those scripts and modules for later use or implementation.
    
>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''
# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES - Importing here to trimmed down imports
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# BASE NODES

from modules.build.guides.base.guide_base import (Base_Guide,
                                                  find_guide_main,
                                                  find_guide_joints,
                                                  mirror_guide,
                                                  toggle_guide_name,
                                                  toggle_guide_axis)

from modules.build.guides.base.guide_base import Guide_Main

# -----------------------------------------------------------------------------
# ENHANCED NODES

from modules.build.guides.build_guide import build_guide