'''
/****************************************** PropIt v 2.0 ***************************************************************************/
                                 ________________________________________
                                |                                        |
                                |  Script done by: Luis Felipe Carranza  |
                                |________________________________________|
>> HOW TO USE >>
     To use the script first you have to select a mesh or meshes, enter the prop's name and the script will do the rest. 

>> NOTES >> 
Update 07/10/2022 : Se añadio una ventana para que el usuario ponga el nombre del prop
Update 11/10/2022 : El script ahora busca el centro de los meshes, pone los controles ahi, hace el skin y crea las layers.

>> CONTACT >>
    luisf.carranza@outlook.com ←or→ https://mpc46.carrd.co
    Copyright (C) 2023 Luis Carranza. All rights reserved.

**************************************************************************************************************************************/
'''

from maya import cmds
from maya import OpenMaya

#// GLOBAL VARIABLES //
sel = cmds.ls(sl=True, l=True)

#// MODULES //
def MatchTransformation(A,B):
    Parentcons = cmds.parentConstraint(A, B, mo=False)
    cmds.delete(Parentcons)
    pass

def ColorOverride (ctrl, index):
    for ctr in Ctrls:
        shape = cmds.listRelatives(ctrl, shapes=True)[0]
    try:
        cmds.setAttr(shape + ' .overrideEnabled', 1)
        cmds.setAttr(shape + ' .overrideColor', index)
    except:
        print("Ctr: %s, Shape: %s --- overrideEnabled failed!" % (ctr, shape))
pass

def PolyPivot(selection, Ctr):
    meshes = (selection)
    TempGeo = cmds.duplicate(meshes, rr=True)
    
    if(len(selection) == 0):
         print("Selecciona al menos una geometria!")
         
    elif(len(selection) == 1):
         objCenter = cmds.objectCenter(TempGeo, gl=True)
         cmds.xform(TempGeo, pivots = objCenter)
         TempCons = cmds.parentConstraint(TempGeo, Ctr)
         cmds.delete(TempGeo, TempCons)
         
    else:
        NewGeo = cmds.polyUnite(TempGeo, centerPivot=True)
        TempCons = cmds.parentConstraint(NewGeo, Ctr)
        cmds.delete(TempGeo, NewGeo, TempCons)
pass

#// SCRIPT //
result = cmds.promptDialog(
                title='PropIt',
                message='Enter Prop Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)

char = cmds.promptDialog(q=True,text=True)

# Create Groups
GrpCtrls = cmds.createNode("transform", n="%s_Grp_Ctrls" % (char))
OfstCOG = cmds.createNode("transform", n="%s_Ofst_COG" % (char))
ConsCOG = cmds.createNode("transform", n="%s_Cons_COG" % (char))
AnimCOG = cmds.createNode("transform", n="%s_Con_COG_Anim" % (char))
GrpJnts = cmds.createNode("transform", n="%s_Grp_Bones" % (char))
OfstJnts = cmds.createNode("transform", n="%s_Ofst_COG_Bones" % (char))
GrpRig = cmds.createNode("transform", n="%s_Grp_rig" % (char))

# Create controls
CtlRoot = cmds.circle(d=3, s=8, nr=(0,1,0), r=8, n="%s_Ctrl_Root" % (char))[0]
CtlCOG = cmds.circle(d=3, s=8, nr=(0, 1, 0), r=5, n="%s_Ctrl_COG" % (char))[0]

#Hierarchy Controls
cmds.parent(CtlCOG, AnimCOG)
cmds.parent(AnimCOG, ConsCOG)
cmds.parent(ConsCOG, OfstCOG)
cmds.parent(OfstCOG, CtlRoot)

#create joints
JntCOG = cmds.joint(name="%s_Bone_COG" % (char))

#hierarchyMain
cmds.parent(JntCOG, OfstJnts)
cmds.parent(OfstJnts, GrpJnts)
cmds.parent(CtlRoot, GrpCtrls)
cmds.parent(GrpCtrls,GrpJnts, GrpRig)

#Crear Atributos control
AGB = cmds.addAttr(CtlRoot, ln="GlobalScale", nn="Global Scale", attributeType='float', defaultValue=1.0, keyable=True)
AVN = cmds.addAttr(CtlRoot, ln="Version", nn="Version", attributeType='float',defaultValue=1, keyable=True,)

Ctrls = ("%s_Ctrl_Root" %(char), "%s_Ctrl_COG" %(char))
axis = ("X", "Y", "Z")

# Conectar Global Scale
for ax in axis:
    cmds.connectAttr("%s_Ctrl_Root.GlobalScale" % (char), "%s_Ctrl_Root.scale" % (char) + ax)
    cmds.connectAttr(char + "_Ctrl_Root.GlobalScale", char + "_Grp_Bones.scale" + ax)
 
# bloquear escalas
for ctr in Ctrls:
    for ax in axis:
        cmds.setAttr(ctr + '.scale' + ax, lock=True, keyable=False)
    cmds.setAttr(ctr + '.visibility', lock=True, keyable=False)


#Colocar el COG al centro de la geometria
PolyPivot(sel, OfstCOG)
MatchTransformation(OfstCOG, OfstJnts)

#JOINT CONSTRAIN
cmds.parentConstraint(CtlCOG, JntCOG, maintainOffset=True)

#Create Display Layers
GeoLayer = cmds.createDisplayLayer(n="Layer_%s_Geo" %(char))
JntLayer = cmds.createDisplayLayer(n="Layer_%s_Bones" %(char))
CtrLayer = cmds.createDisplayLayer(n="Layer_%s_Ctrls" %(char))

#Skin prop and add geo to geo Layer
for obj in sel:
    cmds.skinCluster(obj, JntCOG, tsb=True, n="%s_Sc_01" % (char))
    cmds.editDisplayLayerMembers(GeoLayer, obj)
    continue

#Add Layer Members
cmds.editDisplayLayerMembers(JntLayer, JntCOG)
for ctr in Ctrls:
    cmds.editDisplayLayerMembers(CtrLayer, ctr)
    continue

# To avoid Display Layer override on controls
cmds.disconnectAttr("Layer_%s_Ctrls.drawInfo" %(char), "%s_Ctrl_RootShape.drawOverride" %(char))
cmds.disconnectAttr("Layer_%s_Ctrls.drawInfo" %(char), "%s_Ctrl_COGShape.drawOverride" %(char))

#override Color for controls
ColorIndex = {"Blue":6 ,"Red":13, "Green":14, "Yellow":17, "Cyan":18}
ColorOverride(CtlRoot, ColorIndex["Yellow"])
ColorOverride(CtlCOG, ColorIndex["Green"])