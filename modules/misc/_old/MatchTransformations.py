from maya import cmds
from maya import OpenMaya

#spaguetti to test
JntCOG = cmds.joint(name="%s_Bone_COG" % ("char"))
CtlCOG = cmds.circle(d=3, s=8, nr=(0,1,0), r=10, n="%s_Ctrl_Root" % ("char"))[0]

#script

def MatchTransformation(A,B):
    Parentcons = cmds.parentConstraint(A, B, mo=False)
    cmds.delete(Parentcons)
    pass

def MatchPosition(A,B):
    Pointcons = cmds.pointConstraint(A, B, mo=False)
    cmds.delete(Pointcons)
    pass

def MatchRotation(A,B):
    Orientcons = cmds.orientConstraint(A, B, mo=False)
    cmds.delete(Orientcons)
    pass

def MatchScale(A,B):
    Scalecons = cmds.scaleConstraint(A, B, mo=False)
    cmds.delete(Scalecons)
    pass

def MatchAll(A,B):
    Parentcons = cmds.parentConstraint(A, B, mo=False)
    Scalecons = cmds.scaleConstraint(A, B, mo=False)
    cmds.delete(Parentcons, Scalecons)
    pass

MatchPosition(CtlCOG,JntCOG)