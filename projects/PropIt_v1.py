'''
Script basico para generar rigs para props de manera automatizada, es importante que remplazes la variable "prop" con el nombre del prop
Este script es bastante sucio y poco optimizado, pero funciona c:

Update 07/10/2022 : Se añadio una ventana para que el usuario ponga el nombre del prop
'''

from maya import cmds
from maya import OpenMaya

result = cmds.promptDialog(
                title='Rename Object',
                message='Enter Name:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)

char = cmds.promptDialog(q=True,text=True)

# Create Groups
GrpCtrls = cmds.group (em=True, n=char+"_Grp_Ctrls")
OfstCOG = cmds.group (em=True, n=char+"_Ofst_COG")
ConsCOG = cmds.group (em=True, n=char+"_Cons_COG")
GrpJnts = cmds.group (em=True, n=char+"_Grp_Bones")
GrpRig = cmds.group (em=True, n=char+"_Grp_rig")

# Create controls
CtlRoot = cmds.circle(d=3, s=8, nr=(0,1,0), r=8, n= char+"_Ctrl_Root")
CtlCOG = cmds.circle(d=3, s=8, nr=(0, 1, 0), r=5, n= char+"_Ctrl_COG")

#Hierarchy Controls
cmds.parent(CtlCOG[0], ConsCOG)
cmds.parent(ConsCOG, OfstCOG)
cmds.parent(OfstCOG, CtlRoot)


#create joints
JntCOG = cmds.joint(name=char+"_Bone_COG")

#hierarchyMain
cmds.parent(JntCOG, GrpJnts)
cmds.parent(CtlRoot, GrpCtrls)
cmds.parent(GrpCtrls,GrpJnts, GrpRig)

cmds.parentConstraint(CtlCOG, JntCOG, maintainOffset=True)

#Crear Atributos control
AGB = cmds.addAttr(CtlRoot, ln="GlobalScale", nn="Global Scale", attributeType='float', defaultValue=1.0, keyable=True)
AVN = cmds.addAttr(CtlRoot, ln="Version", nn="Version", attributeType='float',defaultValue=1, keyable=True,)

Ctrls = (char+"_Ctrl_Root", char+"_Ctrl_COG")
axis = ("X", "Y", "Z")

# Conectar Global Scale
for ax in axis:
    cmds.connectAttr(char + "_Ctrl_Root.GlobalScale", char + "_Ctrl_Root.scale" + ax)
    cmds.connectAttr(char + "_Ctrl_Root.GlobalScale", char + "_Grp_Bones.scale" + ax)
 
# bloquear escalas
for ctr in Ctrls:
    for ax in axis:
        cmds.setAttr(ctr + '.scale' + ax, lock=True, keyable=False)
    cmds.setAttr(ctr + '.visibility', lock=True, keyable=False)
 
#override Color for controls
for ctr in Ctrls:
    shape = cmds.listRelatives(ctr, shapes=True)[0]
    try:
        cmds.setAttr(shape + ' .overrideEnabled', 1)
        cmds.setAttr(shape + ' .overrideColor', 17)
    except:
        print("Ctr: %s, Shape: %s --- overrideEnabled failed!" % (ctr, shape))