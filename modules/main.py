'''
/*****************************************************************************/
                                Main v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    For use in project identification.

>> HOW TO USE >>
    For the modules to work on maya you have to:
        - Copy whole module folder into Documents/maya/modules
        
    or better yet:
    
    On C:\<User Name>\Documents\maya\scripts
        create a file named: "userSetup.Py"

With the following ↓ code inside:

# Import sys to append modules path to sys.path        
import sys

TOOLS_PATH = "D:/Projects/VS Code/Maya" # Put the location of the module

sys.path.append(TOOLS_PATH)

sys.dont_write_bytecode = True # Stops the .pyc for being created

>> DEPENDENCIES >>
    - Maya cmds and OpenMaya (Requieres Autodesk Maya, pre-installed)
    - six (python.exe -m pip install six) [install trough pip]

>> NOTES >> 
	Update 02/08/2023 : Start working on the script.

>> THANKS >> 
Nick Hughes [02/08/2023]:
    For his awesome course that led me to create this file. 
 
/*****************************************************************************/
'''