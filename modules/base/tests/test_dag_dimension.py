'''
/*****************************************************************************/
                            Test Dag Dimension v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Tests for our Object dimensions Functionality

>> HOW TO USE >>
	Simply run the script or run the script called "testing.py"
 
>> NOTES >> 
	Update 08/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [08/08/2023]:
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
from maya import cmds as m
from modules.base import Dag_Node as Dag

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Test_Object_Dimension(unittest.TestCase):

    def setUp(self):
        self.attrs = ["tx", "ty", "tz", "rx", "ry", "rz"]

        self.sphereName = "sphere_GEO"
        self.sphere = Dag(m.polySphere(n=self.sphereName, r=1)[0])

        self.cubeName = "cube_GEO"
        self.cube = Dag(m.polyCube(n=self.cubeName, w=1, h=2, d=3)[0])

    def tearDown(self) -> None:
        self.sphere.delete()
        self.cube.delete()
    
    # -----------------------------------------------------------------------------

    def test_dag_dimension_worldMatrix_pass(self): 
        self.assertTrue(self.sphere.o.worldMatrix)

    def test_dag_dimension_worldMatrix_fail(self):
        calc = (self.cube.a.scaleX == self.sphere.a.scaleX)
        
        with self.assertRaises(ValueError):
            self.assertFalse(calc.node.o.worldMatrix)
        
        calc.node.delete()

    def test_dag_dimension_xformBoundingBox(self):
        expectedResult = [-1.0, -1.0, -1.0, 1.0, 1.0, 1.0]
        self.assertEqual([round(i, 4) for i in self.sphere.o.xformBoundingBox], expectedResult)

    def test_dag_dimension_bb(self):
        expectedResult = lambda x: self.sphere.o.xformBoundingBox
        testedResult = lambda x: self.sphere.o.bb

        self.assertEqual(testedResult.__code__.co_code, expectedResult.__code__.co_code)

    def test_dag_dimension_width(self):
        self.assertEqual(round(self.sphere.o.width, 2), 2.0)
        self.assertEqual(round(self.cube.o.width, 2), 1.0)

    def test_dag_dimension_height(self):
        self.assertEqual(round(self.sphere.o.height, 2), 2.0)
        self.assertEqual(round(self.cube.o.height, 2), 2.0)

    def test_dag_dimension_depth(self):
        self.assertEqual(round(self.sphere.o.depth, 2), 2.0)
        self.assertEqual(round(self.cube.o.depth, 2), 3.0)

    def test_dag_dimension_centre(self):
        self.assertEqual([round(i, 2) for i in self.sphere.o.centre], [0, 0, 0])
        self.assertEqual([round(i, 2) for i in self.cube.o.centre], [0, 0, 0])

    def test_dag_dimension_center(self):
        expectedResult = lambda x: self.sphere.o.centre
        testedResult = lambda x: self.sphere.o.center

        self.assertEqual(testedResult.__code__.co_code, expectedResult.__code__.co_code)

    def test_dag_dimension_position(self):
        self.assertEqual(self.sphere.o.position, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        [self.sphere.a[i].set(1) for i in self.attrs]
        self.assertEqual(self.sphere.o.position, [1, 1, 1, 1, 1, 1])

    # def test_dag_dimension_pivot(self): pass

    def test_dag_dimension_copyPivotTo(self):
        tempDag = Dag(m.group(em=1, w=1))
        self.sphere.a.tx.set(1)
        self.sphere.a.ty.set(2)
        self.sphere.a.tz.set(3)

        tempDag.moveTo(self.sphere)
        self.assertEqual(tempDag.o.centre, [1, 2, 3])
         
        self.cube.o.copyPivotTo(self.sphere)

        tempDag.moveTo(self.sphere)
        self.assertEqual(tempDag.o.centre, [0, 0, 0])

        tempDag.delete()


    def test_dag_dimension_copyPivotFrom(self):
        tempDag = Dag(m.group(em=1, w=1))
        self.sphere.a.tx.set(1)
        self.sphere.a.ty.set(2)
        self.sphere.a.tz.set(3)

        tempDag.moveTo(self.sphere)
        self.assertEqual(tempDag.o.centre, [1, 2, 3])
         
        self.sphere.o.copyPivotFrom(self.cube)

        tempDag.moveTo(self.sphere)
        self.assertEqual(tempDag.o.centre, [0, 0, 0])

        tempDag.delete()

    def test_dag_dimension_centrePivot(self):
        tempDag = Dag(m.group(em=1, w=1)) 

        self.sphere.a.tx.set(1)
        self.sphere.a.ty.set(2)
        self.sphere.a.tz.set(3)

        self.sphere.o.copyPivotFrom(self.cube)
        tempDag.moveTo(self.sphere)
        self.assertEqual(tempDag.o.centre, [0, 0, 0])

        self.sphere.o.centerPivot()
        
        tempDag.moveTo(self.sphere)
        self.assertEqual([round(i, 4) for i in tempDag.o.centre], [1, 2, 3])
        
        tempDag.delete()

    def test_dag_dimension_distanceTo(self): 
        self.cube.a.t.set(0, 10, 0)
        self.assertTrue(self.sphere.o.distanceTo(self.cube) == 10)
        
        self.cube.a.t.set(10, 0, 0)
        self.assertTrue(self.sphere.o.distanceTo(self.cube) == 10)


# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
