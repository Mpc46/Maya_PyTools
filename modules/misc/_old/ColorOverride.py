# Cambiar el color del shape de un objeto

from maya import cmds
from maya import OpenMaya


Ctrls = cmds.ls (sl=True)
ColorIndex = {"Blue":6 ,"Red":13, "Green":14, "Yellow":17, "Cyan":18}

def ColorOverride (ctrl, index):
    for ctr in Ctrls:
        shape = cmds.listRelatives(ctrl, shapes=True)[0]
    try:
        cmds.setAttr(shape + ' .overrideEnabled', 1)
        cmds.setAttr(shape + ' .overrideColor', index)
    except:
        print("Ctr: %s, Shape: %s --- overrideEnabled failed!" % (ctr, shape))
        
Ctrls = (cmds.ls (sl=True))

ColorOverride(Ctrls, ColorIndex["Green"])