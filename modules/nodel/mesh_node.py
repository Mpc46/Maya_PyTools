'''
/*****************************************************************************/
                            Mesh Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Our Mesh Node functionality.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Mesh_Node [Class]

>> NOTES >> 
	Update 10/08/2023 : Start working on the script
 
>> THANKS >> 
    Nick Hughes [10/08/2023]:
        For his awesome course that led me to create this file.

>> CONTACT >>
    luisf.carranza@outlook.com ←or→ https://mpc46.carrd.co
    Copyright (C) 2023 Luis Carranza. All rights reserved. 
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from maya import mel
from modules.nodel import Dag_Node, Dep_Node

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Mesh(Dag_Node):

    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, node):
        Dag_Node.__init__(self, node) # Initializing Dag_Node

        # Check that we are on the transform and not the shape node
        if m.objectType(node) == "mesh":
            self.node = self.node.parent

    # -------------------------------------------------------------------------
    # FORMATION

    @property
    def verts(self):
        return m.ls(self.fullPath + ".vtx[*]", fl=1)
    
    @property
    def edges(self):
        return m.ls(self.fullPath + ".e[*]", fl=1)
    
    @property
    def faces(self):
        return m.ls(self.fullPath + ".f[*]", fl=1)
    
    # -------------------------------------------------------------------------
    # TYPE

    @property
    def type(self):
        return m.objectType(self.shape)

    # -------------------------------------------------------------------------
    # SKIN CLUSTER

    @property
    def skinCluster(self):
        skinCluster = mel.eval("findRelatedSkinCluster \"%s\";" % self.fullPath)
        return Dep_Node(skinCluster)

    @property
    def joints(self):
        if self.skinCluster.exists():
            influences = [Dag_Node(i) for i in m.skinCluster(self.skinCluster, q=1, inf=1)]
            return influences

    def weightTo(self, joints, **kwargs):
        if self.exists():
            m.skinCluster(self.fullPath, joints, **kwargs)

    def softWeightTo(self, joints, rui=0, mi=3, tsb=1, dr=2, **kwargs):
        self.weightTo(joints, rui=rui, mi=mi, tsb=tsb, dr=dr, **kwargs)
    
    def hardtWeightTo(self, joints):
        self.weightTo(joints, rui=0, mi=1, tsb=1, dr=0.1)

    def copyWeightsTo(self, items):
        items = items if isinstance(items, (list, tuple)) else [items]
        if self.skinCluster.exists():
            joints = self.joints
            for item in [Mesh(i) for i in items]:
                if item.skinCluster:
                    item.skinCluster.delete()
                item.hardtWeightTo(joints)
                m.copySkinWeights(
                    ss=self.skinCluster.name,
                    ds=item.skinCluster.name,
                    noMirror=1,
                    sa="closestPoint",
                    ia="oneToOne"
                )
    
    def copyWeightsFrom(self, item):
      Mesh(item).copyWeightsTo(self)
    
    # -------------------------------------------------------------------------
    # TOPOLOGY

    def deleteTweaks(self):
        if self.exists():
            tweaks = list(set([i.name for i in self.history if m.objectType(i.name) == "tweak"]))

            if tweaks:
                m.delete(tweaks)

    # -------------------------------------------------------------------------
    # DUPLICATE

    def duplicate(self, **kwargs):
        if not self.exists():
            raise ValueError(">>> No item to duplicate")
        
        return Mesh(m.duplicate(self.fullPath, **kwargs)[0])