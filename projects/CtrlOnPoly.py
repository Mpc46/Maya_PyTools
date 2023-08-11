from maya import cmds

sel = cmds.ls(sl=True, l=True)

#Spaguetti code to test module!
CtlCOG = cmds.circle(d=3, s=8, nr=(0,1,0), r=10, n="%s_Ctrl_Part" % ("char"))[0]
OfstCOG = cmds.createNode("transform", n="%s_Ofst_Part" % ("char"))
ConsCOG = cmds.createNode("transform", n="%s_Cons_Part" % ("char"))
JntPart = cmds.joint(n="%s_Cons_Part" % ("char"))

cmds.parent(CtlCOG, ConsCOG)
cmds.parent(ConsCOG, OfstCOG)

# THE MODULE
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
        
PolyPivot(sel, OfstCOG)