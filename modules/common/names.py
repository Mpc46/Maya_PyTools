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
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
 
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
    "blendColors":  "blend"
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
        "center": 0,
        "left": 1,
        "right": 2,
        "none": 3,

        "c": 0,
        "l": 1,
        "r": 2,
        "": 3
    },
    "type": {
        "none": 0,

        "root": 1,
        "hip": 2,
        "knee": 3,
        "foot": 4,
        "toe": 5,

        "spine": 6,
        "neck": 7,
        "head": 8,

        "collar": 9,
        "shoulder": 10,
        "elbow": 11,

        "hand": 12,
        "finger": 13,
        "thumb": 14,

        "propa": 15,
        "propb": 16,
        "propc": 17,
        "other": 18,

        "index finger": 19,
        "middle finger": 20,
        "ring finger": 21,
        "pinky finger": 22,
        "extra finger": 23,

        "big toe": 24,
        "index toe": 25,
        "middle toe": 26,
        "ring toe": 27,
        "pinky toe": 28,
        "foot thumb": 29
    }
}
