'''
/*****************************************************************************/
                                Test Path v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Tests for our Paths module.

>> HOW TO USE >>
	Simply run the script or run the script called "testing.py"
 
>> NOTES >> 
	Update 02/08/2023 : Start working on the script

>> THANKS >> 
Nick Hughes [02/08/2023]:
    For his awesome course that led me to create this file. 
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

import unittest
from modules.utils.path import (
    generateReprString,
    baseName,
    namespace,
    rootName
)

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Test_Path(unittest.TestCase):
        
    def test_generateReprString(self):
        clsName = "Dep_Node"
        name = "sphere_GRP"
        expectedResult = "Dep_Node('sphere_GRP')"

        result = generateReprString(clsName, name)

        self.assertEqual(result, expectedResult)
    
    
    def test_rootName(self): 
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        expectedResult = "namespace:sphere_GEO"
        
        result = rootName(name)
        
        self.assertEqual(result, expectedResult)

    
    def test_baseName(self):
        name = "namespace:base_GRP|namespace:sub_GRP|namespace:sphere_GEO"
        expectedResult = "sphere_GEO"
        
        result = baseName(name)
        
        self.assertEqual(result, expectedResult)
    
    
    def test_namespace(self):
        name = "namespace:base_GRP|namespace:sub_GRP|namespace:sphere_GEO"
        expectedResult = "namespace"
        
        result = namespace(name)
        
        self.assertEqual(result, expectedResult)
        pass
    

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()