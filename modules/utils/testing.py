'''
/*****************************************************************************/
                                Testing v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Testing tools to automate the testing of our code from within Maya.

>> HOW TO USE >>
	Run the function "testAllModules" to test all modules and their respective
    tests within the main module. The Function will check for existing tests.
 
>> NOTES >> 
	Update 02/08/2023 : Start working on the script

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

import modules
import os
import unittest

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def discoverAndRun(start_dir = ".", pattern = "test_*.py"):
    """
    discoverAndRun

    Discover and run test cases, returning the result.

    Args:
        start_dir (str, optional)  : The main directory to look in. 
                                        Defaults to ".".
        pattern (str, optional) : The name pattern of the test to run. 
                                        Defaults to "test_*.py".
    """
    
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir, pattern=pattern)
    
    # We'll use the standard text runner which prints to stdout
    runner = unittest.TextTestRunner()
    
    # Return a TestResult
    result = runner.run(tests)
    return result


def getTestOutput(module, pattern = "test_*.py"):
    
    result = discoverAndRun(os.path.dirname(module.__file__), pattern)
    
    print("\n>>> result.testsRun: \t%s" % (result.testsRun))
    print(">>> result.passes: \t\t%s" % (result.testsRun - len(result.errors)))
    print(">>> result.errors: \t\t%s" % (len(result.errors)))
    print(">>> result.failures: \t%s" % (len(result.failures)))
    print(">>> result.skipped: \t%s" % (len(result.skipped)))


def testAllModules():
    getTestOutput(modules)

# testAllModules() # Running all Tests