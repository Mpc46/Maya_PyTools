'''
/****************************** Mpc46Module v 1.0 ****************************/
                     ________________________________________
                    |                                        |
                    |  Script done by: Luis Felipe Carranza  |
                    |________________________________________|

>> DESCRIPTION >>
    This is a module to code  faster and easier for maya

>> NOTES >> 
	Update 13/05/2023 : Se comenzo a trabajar en el script
    Update 31/07/2023 : Improve functions and format PEP8
    Update 14/08/2023 : Deprecated, working on class oriented modules.

>> HOW TO USE >>
	Standalone module with built-in functionalit

>> THANKS >> 
    alexandrewillc (Twitter @oamoros0) [16/06/2023]
        for his contribution in optimizing the Match Transform modules 

>> CONTACT >>
    luisf.carranza@outlook.com ←or→ https://mpc46.carrd.co
    Copyright (C) 2023 Luis Carranza. All rights reserved.

******************************************************************************/
'''

import maya.cmds as cmds
import maya.mel as mel
import sys
import os

# selection
sel = cmds.ls(sl=True, l=True)

# Override colors
color_Index = {"blue": 6,
               "red": 13,
               "green": 14,
               "yellow": 17,
               "cyan": 18}


def ColorOverride(Obj, index):
    try:
        shape = cmds.listRelatives(Obj, shapes=True)[0]
        cmds.setAttr(shape + '.overrideEnabled', 1)
        if isinstance(index, int):
            cmds.setAttr(shape + '.overrideColor', index)
        elif isinstance(index, str):
            cmds.setAttr(shape + '.overrideColor', color_Index[index])
    except:
        cmds.setAttr(Obj + '.overrideEnabled', 1)
        if isinstance(index, int):
            cmds.setAttr(Obj + '.overrideColor', index)
        elif isinstance(index, str):
            cmds.setAttr(Obj + '.overrideColor', color_Index[index])
        return

# Create node functions


def createCircle(d=3, s=8, r=5, a='y', n="circle", c=None, ch=False):
    """
    createCircle

    Description:
    Function for creating circles curves in Maya with extended Utility

    Args:
        d (int, 1 or 3): Degree of the circle. Defaults to 3.
        s (int): Number of points on curve. Defaults to 8.
        r (int): Radius or size of curve. Defaults to 5.
        a (str, tuple): Normal, where curve is pointing at. Defaults to 'y'.
        n (str): Name of the curve. Defaults to "circle".
        c (str, optional): The color of the curve. Defaults to None.
        ch (bool): Construction History. Defaults to False.
    """
    # checks the "a" argument and assigns the value accordingly
    if isinstance(a, str) and a == "x" or a == "y" or a == "z":
        axis_dic = {"y":(0, 1, 0), "x":(1, 0, 0), "z":(0, 0, 1)}
        axis = axis_dic[a]
 
    elif isinstance(a, tuple):
        axis = a
    else:
        print("\n ERROR: Please input x, y, z or a tuple (1,0,1)")
        
    # The [0] is to use the transform node instead of shape node
    if d == 1 or d == 3:
        circle = cmds.circle(sections=s, degree=d, normal=axis, 
                         radius=r, name=n, constructionHistory=ch)[0]
    else:
        print('ERROR: The D argument takes only 1 or 3 as values')

    if c is not None:
        ColorOverride(circle, c)
        return


def createJoint(n="joint", r=1, sc=True, c=None):
    joint = cmds.joint(name=n, radius=r, scaleCompensate=sc)

    if c is not None:
        ColorOverride(joint, c)
        return


def createLocator(n="locator", p=[0, 0, 0], c=None):
    locator = cmds.spaceLocator(name=n, position=p)

    if c is not None:
        ColorOverride(locator, c)
        return
    pass


def createGroup(n="group"):
    group = cmds.createNode("transform", name=n)

# Match transformation functions (Match transforms from A to B)

def MatchTransformation(A, B):
    cmds.delete(cmds.parentConstraint(A, B, mo=False))
    pass

def MatchPosition(A, B):
    cmds.delete(cmds.pointConstraint(A, B, mo=False))
    pass

def MatchRotation(A, B):
    cmds.delete(cmds.orientConstraint(A, B, mo=False))
    pass

def MatchScale(A, B):
    cmds.delete(cmds.scaleConstraint(A, B, mo=False))
    pass

def MatchAll(A, B):
    cmds.delete(cmds.parentConstraint(A, B, mo=False))
    cmds.delete(cmds.scaleConstraint(A, B, mo=False))
    pass

# End of script
