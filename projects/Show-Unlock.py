# Este script muestra y desbloquea los atributos predefinidos de un objeto o seleccion de objetos
from maya import cmds
from maya import OpenMaya
import maya.cmds as cmds

# Add variable to selection
sel = cmds.ls (sl=True)
size = len(sel)

# Variables to Attributes
axis = ['x', 'y', 'z']
attrs = ['t', 'r', 's']

# Unlock Attributes
for obj in sel :
    for ax in axis:
        for attr in attrs:
            cmds.setAttr(obj+'.'+attr+ax, lock=0, keyable=1)
cmds.setAttr(obj+'.'+"visibility", lock=0, keyable=1)

# 05/10/2022 12:10pm se agrego la opcion de desbloquear y mostrar la visibilidad