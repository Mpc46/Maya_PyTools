'''
/*****************************************************************************/
                            Test Joint Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Tests for our Joint Node Functionality

>> HOW TO USE >>
	Simply run the script or run the script called "testing.py"
 
>> NOTES >> 
	Update 13/08/2023 : Start working on the script
    
>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.

/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

import unittest
from maya import cmds as m
from modules.base import Mesh, Joint

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Test_Joint(unittest.TestCase):

    def setUp(self):
        self.sphereName = "sphere_GEO"
        self.sphere = Mesh(m.polySphere(n=self.sphereName, r=1)[0])

        self.cubeName = "cube_GEO"
        self.cube = Mesh(m.polyCube(n=self.cubeName, w=1, h=2, d=3)[0])

        m.select(cl=True)
        self.body_j1 = Joint("body_j1")

        m.select(cl=True)
        self.body_j2 = Joint("body_j2")

    def tearDown(self):
        self.sphere.delete()
        self.cube.delete()
        self.body_j1.delete()
        self.body_j2.delete()

    # -------------------------------------------------------------------------
    # EXISTS

    def test_joint_exists(self):
        self.assertTrue(self.sphere.exists())
        self.assertTrue(self.cube.exists())

        self.assertTrue(self.body_j1.exists())
        self.assertTrue(self.body_j2.exists())

    # -------------------------------------------------------------------------
    # RADIUS

    def test_joint_radius(self):
        self.assertEqual(self.body_j1.radius, 1.0)

        self.body_j2.setRadius(12)
        self.assertEqual(self.body_j2.radius, 12.0)

    # -------------------------------------------------------------------------
    # JOINT ORIENT

    def test_joint_orient(self):
        self.assertEqual(self.body_j1.jointOrient, [0.0, 0.0, 0.0])

        self.body_j2.setJointOrient(20, 30, 55)
        expectedResult = [20.0, 30.0, 55.0]
        result = [round(i, 4) for i in self.body_j2.jointOrient]
        self.assertEqual(result, expectedResult)

        self.body_j1.setJointOrient(80.5)
        expectedResult = [80.5, 0.0, 0.0]
        result = [round(i, 4) for i in self.body_j1.jointOrient]
        self.assertEqual(result, expectedResult)

    # -------------------------------------------------------------------------
    # JOINT LABEL

    def test_joint_label(self):
        expectedResult = ['center', 'none', False]
        result = self.body_j1.label
        self.assertCountEqual(result, expectedResult)

        self.body_j2.setLabel("l", "shoulder", 1)
        expectedResult = ['left', 'shoulder', True]
        result = self.body_j2.label
        self.assertCountEqual(result, expectedResult)

        self.body_j1.setLabelSide("r")
        self.assertTrue(self.body_j1.labelSide == "right")

        self.body_j1.setLabelType("Test")
        expectedResult = 18
        result = m.getAttr(self.body_j1.name+".type")
        self.assertTrue(result == expectedResult)
        self.assertEqual(self.body_j1.labelType, "Test")

        self.body_j2.setLabelVis(0)
        self.assertEqual(self.body_j2.labelVis, False)

    # -------------------------------------------------------------------------
    # HANDLE AND LOCAL AXIS

    def test_joint_handle(self):
        self.assertFalse(self.body_j1.handle)

        self.body_j1.showHandle()
        self.assertEqual(self.body_j1.handle, True)

        self.body_j1.hideHandle()
        self.assertNotEqual(self.body_j1.handle, True) 


    def test_joint_localAxis(self): 
        self.assertFalse(self.body_j1.localAxis)

        self.body_j1.showLocalAxis()
        self.assertEqual(self.body_j1.localAxis, True)

        self.body_j1.hideLocalAxis()
        self.assertNotEqual(self.body_j1.localAxis, True) 


    # -------------------------------------------------------------------------
    # DRAW STYLE

    def test_joint_drawStyle(self): 
        self.assertEqual(self.body_j2.drawStyle, 0)

        self.body_j2.setDrawStyle(2)
        self.assertEqual(self.body_j2.drawStyle, 2)

    # -------------------------------------------------------------------------
    # ROTATE ORDER

    def test_joint_rotateOrder(self): 
        expectedResult = 0
        result = self.body_j1.rotateOrder
        self.assertEqual(expectedResult, result)

        self.body_j1.setRotateOrder("zyx")
        expectedResult = 5
        result = self.body_j1.rotateOrder
        self.assertEqual(expectedResult, result)

        self.body_j1.setRotateOrder(3)
        expectedResult = 3
        result = self.body_j1.rotateOrder
        self.assertEqual(expectedResult, result)


# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    unittest.main()
