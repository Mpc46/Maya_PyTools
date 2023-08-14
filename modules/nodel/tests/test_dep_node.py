'''
/*****************************************************************************/
                            Test Dep Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Tests for our Dep Node Functionality

>> HOW TO USE >>
	Simply run the script or run the script called "testing.py"
 
>> NOTES >> 
	Update 03/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [02/08/2023]:
        For his awesome course that led me to create this file. 

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.

/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

import unittest
from maya import cmds
from modules.nodel import Dep_Node

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Test_Dep_Node(unittest.TestCase):

    def setUp(self) -> None:  # When test start do this
        self.sphereName = "sphere_GEO"
        self.jointName = "sphere_JNT"

        self.sphere = Dep_Node(cmds.polySphere(n=self.sphereName)[0])
        self.object = Dep_Node(self.sphereName)

        cmds.select(cl=True)  # Clear selection

        self.joint = Dep_Node(cmds.joint(n=self.jointName))

    def tearDown(self) -> None:  # After test is done, delete all
        if cmds.objExists(self.sphereName):
            cmds.delete(self.sphereName)

        if cmds.objExists(self.jointName):
            cmds.delete(self.jointName)

    def test_dep_node__str__(self):
        self.assertEqual(str(self.sphere), self.sphereName)

    def test_dep_node__repr__(self):
        self.assertEqual(
            self.sphere.__repr__(),
            "Dep_Node('sphere_GEO')"
        )

    def test_dep_node__eq__(self):
        self.assertTrue(self.sphere == self.object)
        self.assertTrue(self.sphere.fullPath == self.object.fullPath)
        self.assertTrue(self.sphere.path == self.object.path)

        self.assertFalse(self.sphere == self.joint)

    def test_dep_node_node_getter(self):
        self.assertEqual(self.sphere.node, self.sphere.name)
        self.assertEqual(self.joint.node, self.jointName)
        self.assertNotEqual(self.joint.node, self.sphereName)

    def test_dep_node_node_setter(self):
        self.sphere.node = self.jointName
        self.assertEqual(self.sphere.node, self.jointName)
        cmds.delete(self.sphereName)

    def test_dep_node_path(self):
        self.assertEqual(self.sphere.fullPath, self.sphereName)

    def test_dep_node_fullpath(self):
        self.assertEqual(self.sphere.fullPath, self.sphereName)
        self.assertEqual(self.sphere.fullPath, self.sphere.path)
        self.assertNotEqual(self.sphere.fullPath, self.joint.fullPath)

    def test_dep_node_isReference(self):
        self.assertFalse(self.sphere.isReferenced())

    def test_dep_node_exists(self):
        self.assertTrue(self.sphere.exists())

        cmds.delete(self.sphere)

        self.assertFalse(self.sphere.exists())

    def test_dep_node_exists_fake_object(self):
        self.assertFalse(Dep_Node("FAKE_OBJECT").exists())

    def test_dep_node_type(self):
        self.assertEqual(self.joint.type, "joint")
        self.assertNotEqual(self.joint.type, "nurbsCurve")

    def test_dep_node_typ(self):
        self.assertEqual(self.joint.typ, "joint")
        self.assertNotEqual(self.joint.typ, "nurbsCurve")

    def test_dep_node_name(self):
        self.assertTrue(self.sphere.name == self.sphereName)
        self.assertFalse(self.sphere.name == "sphere_FAKE_MESH")

    def test_dep_node_namespace(self):
        self.assertIsNone(self.sphere.namespace)

    def test_dep_node_namespace_is_not_none(self):
        cmds.namespace(add='FOO')
        namespace = "FOO:"
        self.sphere.rename(namespace + self.sphereName)
        self.assertEqual(self.sphere.namespace, "FOO")
        cmds.delete(self.sphere)
        cmds.namespace(rm='FOO')

    def test_dep_node_rename(self):
        newName = "sphere_renamed_GEO"
        self.sphere.rename(newName)
        self.assertEqual(self.sphere.name, newName)
        # Del it cause won't find it on TearDown
        cmds.delete(self.sphere)

    def test_dep_node_lock_and_islocked(self):
        self.assertFalse(self.sphere.isLocked)

        self.sphere.lock(1)
        self.assertTrue(self.sphere.isLocked)

        self.sphere.lock(False)
        self.assertFalse(self.sphere.isLocked)

    def test_dep_node_delete(self):
        self.assertTrue(self.object.exists())
        self.object.delete()
        self.assertFalse(self.object.exists())

    def test_dep_node_create_multiply_divide_node(self):
        mdNode = Dep_Node("geo_MD", "multiplyDivide")
        self.assertTrue(mdNode.exists())

        mdNode.delete()
        self.assertFalse(mdNode.exists())

    def test_dep_node_create_and_delete_vector_product_node(self):
        vectorProduct = Dep_Node(cmds.shadingNode(
            'vectorProduct', asUtility=True, n="test_VP"))
        self.assertTrue(vectorProduct.exists())

        vectorProduct.delete()
        self.assertFalse(vectorProduct.exists())

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    unittest.main()
