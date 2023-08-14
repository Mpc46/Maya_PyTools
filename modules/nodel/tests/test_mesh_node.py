'''
/*****************************************************************************/
                            Test Mesh Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Tests for our Mesh Node Functionality

>> HOW TO USE >>
	Simply run the script or run the script called "testing.py"
 
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

import unittest
from maya import cmds as m
from modules.nodel import Mesh, Dag_Node, Dep_Node

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Test_Mesh(unittest.TestCase):

    def setUp(self):
        self.sphereName = "sphere_GEO"
        self.sphere = Mesh(m.polySphere(n=self.sphereName, r=1)[0])

        self.cubeName = "cube_GEO"
        self.cube = Mesh(m.polyCube(n=self.cubeName, w=1, h=2, d=3)[0])

        self.body_j1_name = "body_j1"
        self.body_j2_name = "body_j2"
        
        m.select(cl=True)
        self.body_j1 = Dag_Node(m.joint(n=self.body_j1_name))
        m.select(cl=True)
        self.body_j2 = Dag_Node(m.joint(n=self.body_j2_name))

        m.skinCluster(self.sphere.fullPath, [self.body_j1, self.body_j2], rui=0, mi=3, tsb=1, dr=2)


    def tearDown(self) -> None:
        self.sphere.delete()
        self.cube.delete()
        self.body_j1.delete()
        self.body_j2.delete()

    # -------------------------------------------------------------------------
    # FORMATION

    def test_mesh_verts(self): 
        self.assertEqual(self.sphere.verts[0], self.sphereName + ".vtx[0]")
        self.assertEqual(self.sphere.verts[1], self.sphereName + ".vtx[1]")

    def test_mesh_edges(self): 
        self.assertEqual(self.sphere.edges[0], self.sphereName + ".e[0]")
        self.assertEqual(self.sphere.edges[1], self.sphereName + ".e[1]")
        
    def test_mesh_faces(self): 
        self.assertEqual(self.sphere.faces[0], self.sphereName + ".f[0]")
        self.assertEqual(self.sphere.faces[1], self.sphereName + ".f[1]")
        

    # -------------------------------------------------------------------------
    # TYPE

    def test_mesh_type(self): 
        self.assertEqual(self.sphere.type, "mesh")

    # -------------------------------------------------------------------------
    # SKIN CLUSTER

    def test_mesh_skinCluster(self): 
        self.assertTrue(self.sphere.skinCluster.exists())

    def test_mesh_joints(self): 
        self.assertEqual(self.sphere.joints, [self.body_j1, self.body_j2])

    def test_mesh_weightTo(self): 
        joints = [self.body_j1, self.body_j2]
        self.cube.weightTo(joints, rui=0, mi=3, tsb=1, dr=2)

        self.assertTrue(self.sphere.skinCluster.exists())
        self.assertTrue(self.cube.skinCluster.exists())

    def test_mesh_softWeightTo(self): 
        joints = [self.body_j1, self.body_j2]
        self.cube.softWeightTo(joints)
        self.assertTrue(self.cube.skinCluster.exists())

    def test_mesh_hardtWeightTo(self):
        joints = [self.body_j1, self.body_j2] 
        self.cube.hardtWeightTo(joints)
        self.assertTrue(self.cube.skinCluster.exists())

    def test_mesh_copyWeightsTo(self): 
        self.sphere.copyWeightsTo(self.cube)
        self.assertTrue(self.cube.skinCluster.exists())

    def test_mesh_copyWeightsFrom(self): 
        self.cube.copyWeightsFrom(self.sphere)
        self.assertTrue(self.cube.skinCluster.exists())

    # -------------------------------------------------------------------------
    # TOPOLOGY

    def test_mesh_deleteTweaks(self): 
        sphere2 = Mesh(m.polySphere(n=self.sphereName)[0])
        m.move(0, 4, 0, self.body_j2, r=1)
        m.move(4, 4, 4, self.sphere.verts[:33],a=1)
        m.blendShape(sphere2, self.sphere, tc=0)

        self.assertTrue(Dep_Node("tweak1").exists())
        self.sphere.deleteTweaks()
        self.assertFalse(Dep_Node("tweak1").exists())

        sphere2.delete()

    # -------------------------------------------------------------------------
    # DUPLICATE

    def test_mesh_duplicate(self): 
        sphere2 = self.sphere.duplicate(n="test_sphere")
        self.assertTrue(sphere2.exists())
        self.assertEqual(sphere2.name, "test_sphere")

        sphere2.delete()

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()