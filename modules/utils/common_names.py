'''
/*****************************************************************************/
                                Common Names v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Common naming for the maya color override.

>> HOW TO USE >>
	This module is meant to be imported or referenced into larger scripts.
 
>> CONTENTS >>
    + COLORS_DICT (Dict);

>> NOTES >> 
	Update 04/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [04/08/2023]:
        For his awesome course that led me to create this file. 
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# DICTIONARIES
# -----------------------------------------------------------------------------

COLORS_DICT = {
    "grey": 0,
    
    "black": 1,
    "dark grey": 2,
    "light grey": 3,
    
    "dark red": 4,
    "dark blue": 5,
    "blue": 6,
    
    "dark green": 7,
    "dark purple": 8,
    "hot pink": 9,
    
    "brown": 10,
    "dark brown": 11,
    "apple": 12,
    
    "red": 13,
    "green": 14,
    "cobalt": 15,
    
    "white": 16,
    "yellow": 17,
    "light blue": 18,
    
    "arctic": 19,
    "pink": 20,
    "orange": 21,
    
    "light yellow": 22,
    "fern": 23,
    "dark orange": 24,
    
    "dark yellow": 25,
    "pear": 26,
    "parakeet": 27,
    
    "sky": 29,
    "lapis": 30,
    "purple": 31,
}

NODES_DICT = {
    "multiplyDivide": "Md",
    "condition": "Cnd",
    "plusMinusAverage": "Pma",
}
