'''
/*****************************************************************************/
                            NoDel Modules
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    This library holds important scripts that are used as the 
    building fundation of the other scripts.

>> HOW TO USE >>
	This library is meant to be imported into larger scripts and/or
    hold those scripts and modules for later use or implementation.

>> CONTENTS >> 
    Libraries:
        + base
        + tests
        
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

from modules.nodel.base.dep_node import Dep_Node
from modules.nodel.base.dag_node import Dag_Node
from modules.nodel.base.attribute_base import Attributes, Attribute

# -----------------------------------------------------------------------------
# ENHANCED NODES

from modules.nodel.mesh_node import Mesh
from modules.nodel.joint_node import Joint