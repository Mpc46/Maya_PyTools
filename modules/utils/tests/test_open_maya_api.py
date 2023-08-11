'''
/*****************************************************************************/
                            Test Open Maya API v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Tests for our Open Maya API Functionality

>> HOW TO USE >>
	Simply run the script or run the script called "testing.py"
 
>> NOTES >> 
	Update 03/08/2023 : Start working on the script

>> THANKS >> 
Nick Hughes [02/08/2023]:
    For his awesome course that led me to create this file. 

/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

import unittest
from maya import cmds, OpenMaya
from modules.utils.open_maya_api import toMObject, toDpendencyNode

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Test_Maya_Open_API(unittest.TestCase):

    def setUp(self) -> None:  # -> None, The method won't return any value
        self.jointName = "L_hand_JNT"
        self.joint = cmds.joint(n=self.jointName)

        self.baseGrp = cmds.group(n="BASE_GRP", em=True)
        self.subGrp = cmds.group(n="SUB_GRP", em=True)
        cmds.parent(self.subGrp, self.baseGrp)
        cmds.parent(self.joint, self.subGrp)

    def tearDown(self) -> None:
        cmds.delete(self.baseGrp)

    def test_toDpendencyNode(self):
        expectedResult = "joint"

        result = toDpendencyNode(self.jointName)
        nodeTypeName = result.typeName()

        self.assertEqual(nodeTypeName, expectedResult)

    def test_toMObject(self):
        expectedResult = "|BASE_GRP|SUB_GRP|L_hand_JNT"

        result = toMObject(self.jointName)
        fullPathName = OpenMaya.MFnDagNode(result).fullPathName()

        self.assertEqual(fullPathName, expectedResult)


# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
