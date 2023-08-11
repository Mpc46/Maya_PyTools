import maya.cmds as mc

attrVsDefaultValue = {'sx':1, 'sy':1, 'sz':1, 'rx':0, 'ry':0, 'rz':0, 'tx':0, 'ty':0, 'tz':0}

sel = mc.ls(sl=1)
for obj in sel:
    for attr in attrVsDefaultValue:
        try:
            mc.setAttr('%s.%s'%(obj, attr), attrVsDefaultValue[attr])
        except:
            pass
