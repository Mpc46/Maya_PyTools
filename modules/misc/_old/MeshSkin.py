from maya import cmds
from maya import OpenMaya

sel = cmds.ls(sl=True, l=True)

#Spaguetti code to test module!
#JntCOG = cmds.joint(name="%s_Bone_COG" % ("char"))

def SkinMesh(mesh, jnts):
    cmds.skinCluster(mesh, jnts, tsb=True)
pass

SkinMesh(sel, 'char_Bone_COG')