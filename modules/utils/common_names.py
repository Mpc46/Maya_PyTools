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
    To access nested dictionaries: DICT[dict][key]
 
>> CONTENTS >>
    + COLORS_DICT (Dict)
    + NODES_DICT (Dict)
    + ROTATE_ORDER_DICT (Dict)
    + JOINT_LABEL_DICT (Dict)

>> NOTES >> 
	Update 04/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [04/08/2023]:
        For his awesome course that led me to create this file. 

>> CONTACT >>
    luisf.carranza@outlook.com ←or→ https://mpc46.carrd.co
    Copyright (C) 2023 Luis Carranza. All rights reserved.
 
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
    "cyan": 18,

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

ROTATE_ORDER_DICT = {
    "xyz": 0, 
    "yzx": 1, 
    "zxy": 2, 
    "xzy": 3, 
    "yxz": 4, 
    "zyx": 5
}

JOINT_LABEL_DICT = {
    "side": {
        "Center": 0,
        "Left": 1,
        "Right": 2,
        "None": 3,

        "C": 0,
        "L": 1,
        "R": 2,
        "": 3
    },
    "type": {
        "None": 0,

        "Root": 1,
        "Hip": 2,
        "Knee": 3,
        "Foot": 4,
        "Toe": 5,

        "Spine": 6,
        "Neck": 7,
        "Head": 8,

        "Collar": 9,
        "Shoulder": 10,
        "Elbow": 11,

        "Hand": 12,
        "Finger": 13,
        "Thumb": 14,

        "PropA": 15,
        "PropB": 16,
        "PropC": 17,
        "Other": 18,

        "Index Finger": 19,
        "Middle Finger": 20,
        "Ring Finger": 21,
        "Pinky Finger": 22,
        "Extra Finger": 23,

        "Big Toe": 24,
        "Index Toe": 25,
        "Middle Toe": 26,
        "Ring Toe": 27,
        "Pinky Toe": 28,
        "Foot Thumb": 29
    }
}
