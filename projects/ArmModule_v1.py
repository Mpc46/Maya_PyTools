'''
/****************************************** ArmModule v 1.5 *************************************************************************/
                                 ________________________________________
                                |                                        |
                                |  Script done by: Luis Felipe Carranza  |
                                |________________________________________|
>> HOW TO USE >>
     This is an autorig module for modular rigs.
     
>> NOTES >> 
Update 15/06/2023 : I began working on the script
Update 19/06/2023 : Hard code some parts of the code that needs debug, IK/FK systems working
Update 19/06/2023 : Ik/Fk switch working!
Update 20/06/2023: Mirror guides working!

>> THANKS >> 
Michael Clavan (Twitter @MichaelClavan) for his contribution in helping me connecting the slider control [17/06/2023]

**************************************************************************************************************************************/
'''

# Libraries #
import maya.cmds as cmds
import maya.mel as mel
import imp
import sys

path = r'D:\Projects\VS Code\Maya\modules'
if path not in sys.path:
    sys.path.append(path)
import modules.misc.Mpc46Module as mpc
imp.reload(mpc) # Python 2.x > python 3.3 forces module reload

# SCRIPT #

# ----------------------------------------------------------------------------------------------------------------
#                                               USER INTERFACE
# ----------------------------------------------------------------------------------------------------------------

def ui():
    # Set up UI basics.
    win = 'ArmModule'
    if (cmds.window(win, exists = 1)):
        cmds.deleteUI(win)
    cmds.window(win, rtf = 1, w = 2, h = 2, t = win, s = 1)
    cmds.columnLayout(adj = 1)

	# Fill the UI with stuff.
    cmds.button (l='Create Arm Guide',c = lambda x: armGuides()) # Button to create guides
    cmds.separator(h=10)
    cmds.floatSliderButtonGrp("radSlider", l=("Jnt Radius"), buttonLabel = "Apply", value=1.0, max=50.0, field=True, vcc=lambda x: radValues() , bc = 'radValues()')
   
    cmds.separator(h=10) # Just a separator to keep things clean
    
    cmds.rowColumnLayout(nc=2, adj=1)
    cmds.button(l="Mirror", c= lambda x: mirrorGuide())
    cmds.button(l="Toggle axis", c= lambda x: toggleRotAxis())
  
    cmds.setParent('..') # Exit the current layout by 1 level.
    
    cmds.separator(h=15) # Just a separator to keep things clean
    
    cmds.button (l="Build rig",h=40, c = lambda x: armBuild()) # Button to build rig
    
    cmds.rowColumnLayout(nc=2, adj = 1)
    
    cmds.button(l="Rebuild", c = lambda x: armReBuild())
    cmds.button(l="Delete", c = lambda x: armDel())
    
    cmds.setParent ('..') # Exit the current layout by 1 level.
    
    cmds.separator(h=15) # Just a separator to keep things clean

    cmds.button (l = "Switch", c = lambda x: switch()) # Button to build rig
    
    # Launch the UI.
    cmds.showWindow (win)
    
# ----------------------------------------------------------------------------------------------------------------
#                                               GUIDES
# ----------------------------------------------------------------------------------------------------------------

# Create the guides for the arm module
def armGuides():
    if cmds.objExists("Guides"): # If a guide already exists do nothing, else create a guide
        sys.stdout.write ("ERROR: There's already a Guide group!")
        pass
    else:
        #names
        guideName = "_Guide"
        guidetype = "L_Jnt_"
        
        shoulderGuideName = "{}shoulder{}".format(guidetype, guideName)
        elbowGuideName = "{}elbow{}".format(guidetype, guideName)
        wristGuideName = "{}Wrist{}".format(guidetype, guideName) # HAY UN ERROR QUE SOLO FUNCIONA SI TIENE UNA MAYUSCULA WTF?
        
        #Create Arm joints
        guideColor = "cyan" # the color of the guide joints
        mpc.createJoint(n="{}".format(shoulderGuideName), c=guideColor)
        mpc.createJoint(n="{}".format(elbowGuideName), c=guideColor)
        mpc.createJoint(n="{}".format(wristGuideName), c=guideColor)
        
        # Positioning
        cmds.move(0.568, 4.792, -0.052, shoulderGuideName) # Translate shoulder guide joint
        cmds.setAttr("{}.jointOrientY".format(shoulderGuideName), 2) # Rotate shoulder guide
        cmds.setAttr("{}.tx".format(elbowGuideName), 0.882) # Translate elbow guide 
        cmds.setAttr("{}.jointOrientY".format(elbowGuideName), -2) # Rotate elbow guide
        cmds.setAttr("{}.tx".format(wristGuideName), 0.753) # Translate wrist guide 
        
        # Tyding up
        armGuideOfsName = "L_Ofs_arm_Guide" # just to avoid typos
        mpc.createGroup(n=armGuideOfsName)
        
        mpc.MatchTransformation(shoulderGuideName, armGuideOfsName)
        cmds.parent(shoulderGuideName, armGuideOfsName)
        
        mpc.createGroup(n="Guides")
        cmds.parent(armGuideOfsName, "Guides")
        cmds.addAttr("Guides", ln="rad", nn="Jnt Radius", attributeType='float', defaultValue=1.0, hidden=True)
        
        cmds.select(cl=1)
        return

def radValues():
    #cmds.connectControl("radSlider", "joint1.radius") # Deprecated cause it had issues with updating
    jntSel = cmds.ls("*_Jnt_*_Guide")
    jntList = []
    
    # Clean the messy maya list and turned it into a nice list [WITHOUT THE (u"jnt")]
    for jnt in jntSel:
        jntList.append(str(jnt))
    
    cmds.connectControl("radSlider", "Guides.rad")
        
    # Change the radiuses 
    for jnt in jntList:
        rad = cmds.getAttr("Guides.rad") 
        cmds.setAttr("{}.radius".format(jnt), rad)

def mirrorGuide():
    
    allGuides = cmds.listRelatives("Guides", ad=True)
    toMirror = []
    mirrored = []
    
    for i in allGuides: # Appends items to list to further use
        if "L_" in i:
            toMirror.append(str(i))
    
    for i in toMirror: # Finds  the sides and duplicates them
        if "_Ofs_" in i:
            cmds.duplicate(i, rc=True)        
            
    for i in toMirror: # Replace L with R
        if "L_" in i:
            newname = i.replace("L_", "R_")
            cmds.rename(i, newname)
            
    allGuides = cmds.listRelatives("Guides", ad=True)
    
    for i in allGuides:
        if "Guide1" in i:
            newname = i.replace("Guide1", "Guide")
            cmds.rename(i, newname)
        elif "R_" in i:
            mirrored.append(str(i))
                    
    tempGrp = "tempoMirror"        
    mpc.createGroup(n=tempGrp)
    
    for ofs in mirrored:
        if "_Ofs_" in ofs:
            cmds.parent(ofs, tempGrp)
    
    cmds.setAttr("{}.scaleX".format(tempGrp), -1)
    
    for ofs in mirrored:
        if "_Ofs_" in ofs:
            cmds.parent(ofs, "Guides")

    cmds.delete(tempGrp) # We don't need it
    
    pass

def toggleRotAxis(): # Toggle axis for better positioning!
    objs = cmds.listRelatives("Guides", ad=True)
    
    for i in objs:
       if cmds.objectType(i, isType="joint"):
           if cmds.getAttr("{}.displayLocalAxis".format(i)) == True:
                cmds.setAttr("{}.displayLocalAxis".format(i), 0)
           else:
                cmds.setAttr("{}.displayLocalAxis".format(i), 1)
    
    pass

# ----------------------------------------------------------------------------------------------------------------
#                                               BUILD
# ----------------------------------------------------------------------------------------------------------------

# Build rig from guides   
def armBuild():
    guideName = "Guide"
    guides = cmds.ls('*_{}'.format(guideName))
    
    for guide in guides:
        guideParent = cmds.listRelatives(guide, c=1)
       
        cmds.select (cl = 1) # clear the selection that happens when you run the script
        
        # Rename joints
        jntName = guide.replace('{}'.format(guideName),'Bnd')
        
        #create joints or groups
        if "Jnt" in guide:
            jnt = mpc.createJoint(n=jntName, c="green")
            
            # Match transforms from guide            
            mpc.MatchTransformation(guide, jntName)
            cmds.makeIdentity (jntName, a = 1, t =1, r = 1, s = 1) #freeze transforms
            
            # Search and apply joint radius to new joints
            rad = cmds.getAttr("{}.radius".format(guide))
            cmds.setAttr("{}.radius".format(jntName), rad)
            
            # Recreate hierarchy  
            if guideParent:
                try:
                    jntParent = guideParent[0].replace("_Guide",'_Bnd')
                    cmds.parent (jnt, jntParent)
                except:
                    sys.stdout.write ('An error has been occured and we do not know how to fix it')
                    
        elif "Ofs" in guide:
            grp = mpc.createGroup(n=jntName)
            
            mpc.MatchTransformation(guide, jntName)
                        
            if guideParent:
                try:
                    jntParent = guideParent[0].replace("_Guide",'_Bnd')
                    cmds.parent (jnt, jntParent)
                except:
                    sys.stdout.write ('An error has been occured and we do not know how to fix it')
        continue            
    
    cmds.setAttr("Guides.visibility", 0) # Hides the guides from viewport
    
    # For the moment I'm gonna hard code it, I'll fix it later 17/06/2023 14:40
    mpc.createGroup(n="Rig")
    mpc.createGroup(n="L_Grp_arm_Jnts")
    mpc.createGroup(n="Joints")
    mpc.MatchTransformation("L_Ofs_arm_Bnd", "L_Grp_arm_Jnts")
    cmds.parent("L_Ofs_arm_Bnd", "L_Grp_arm_Jnts")
    cmds.parent("L_Grp_arm_Jnts", "Joints")
    cmds.parent("Joints", "Rig")
    
    cmds.select (cl = 1) # Clear Selection


# Delete the created rig and unhides the guides
def armDel():
    try:
        cmds.delete("Rig")
        cmds.setAttr("Guides.visibility", 1) # Unhides the guides from viewport
    except:
        sys.stdout.write ("I cannot delete something that doesn't exist")
    
    return
# Delete and build the rig
def armReBuild():
    try:
        armDel()
        armBuild()
    except:
        sys.stdout.write ("I cannot rebuild something that doesn't exist")

# ----------------------------------------------------------------------------------------------------------------

# switch
def switch():
    
    def duplicateJnts(toDuplicate, oldSuffix, newSuffix, rad=1, c=None):
        cmds.duplicate(toDuplicate, rc=True)
        
        sel = cmds.ls("*_{}1".format(oldSuffix))
        
        objs = [] # the original objects wthat we duplicated
        jnts = [] # a new list with new names
        
        for obj in sel:
            objs.append(str(obj))
    
        for obj in objs:
            jntNewName = obj.replace("{}1".format(oldSuffix), newSuffix)
            cmds.rename(obj, jntNewName)
            jnts.append(jntNewName)

        for jnt in jnts:
            try:
                oriRad = cmds.getAttr("{}.radius".format(jnt))
                NewRad = oriRad * rad
                cmds.setAttr("{}.radius".format(jnt), float(NewRad))
                if c is not None:
                    mpc.ColorOverride(jnt, c)
            except:
                continue
    
    # ----------------------------------------------------------------------------------------------------------------
    
    def fkBuild(r=3):
        # hard code stuff cause Im in a hurry
        mpc.createGroup(n="Controls")
        mpc.createGroup(n="L_Grp_arm_Ctrls")
        cmds.parent("L_Grp_arm_Ctrls", "Controls")
        cmds.parent("Controls", "Rig")
        
        # End hard code stuff
        fKList = cmds.ls("*_FK")
        fks = []
        
        for i in fKList:
            fks.append(str(i))
        
        for fk in fks:
            if "Jnt" in fk:
                jntParent = cmds.listRelatives(fk, c=1)
                                
                jntRad = cmds.getAttr("{}.radius".format(fk))
                rad = jntRad * r # Multiplies the given radius to create control radius
                
                # Renaming and setting names
                ctlName = fk.replace("Jnt", "Ctl")
                ofsName = ctlName.replace("Ctl", "Ofs") # still code
                ofsName = ofsName + "ctrl"
                
                # Creating control and ofset group
                ctl = mpc.createCircle(n=ctlName, a='x', r=rad, c="blue")
                Ofs = mpc.createGroup(n=ofsName)
                
                #parenting and creating final constrain
                cmds.parent(ctlName, ofsName)
                mpc.MatchTransformation(fk, ofsName) # this thing 
                cmds.parentConstraint(ctlName, fk)
                
                """ if jntParent: # Recreate the hierarchy 
                    try:
                        fkParent = jntParent[0].replace("_Guide",'_Bnd')
                        cmds.parent (fk, fkParent)
                    except:
                        sys.stdout.write ('An error has been occured and we do not know how to fix it') """
        
        # Hard code hierarchy 19/06/2023 14:18
        cmds.parent("L_Ofs_Wrist_FKctrl", "L_Ctl_elbow_FK")
        cmds.parent("L_Ofs_elbow_FKctrl", "L_Ctl_shoulder_FK")
        cmds.parent("L_Ofs_shoulder_FKctrl", "L_Grp_arm_Ctrls")
        
        return    
    
    def ikBuild(r=3):
        # Hard coded for now 19/06/2023 14:40
        jntRad = cmds.getAttr("{}.radius".format("L_Jnt_Wrist_IK"))
        rad = jntRad * r # Multiplies the given radius to create control radius
        
        ikh = cmds.ikHandle(sj= "L_Jnt_shoulder_IK", ee="L_Jnt_Wrist_IK", n="L_Ikh_Wrist_IK")
        mpc.createGroup(n="L_Ofs_Wrist_IKCtrl")
        ctlIkh = mpc.createCircle(n="L_Ctl_Wrist_IK", a='x', r=rad, c="red")
        
        cmds.parent("L_Ctl_Wrist_IK", "L_Ofs_Wrist_IKCtrl")
        mpc.MatchTransformation("L_Jnt_Wrist_IK", "L_Ofs_Wrist_IKCtrl")
        
        cmds.parent("L_Ikh_Wrist_IK", "L_Ctl_Wrist_IK")
        cmds.parent("L_Ofs_Wrist_IKCtrl", "L_Grp_arm_Ctrls")
        
        cmds.setAttr("L_Ikh_Wrist_IK.visibility", 0) # hides Ikh

        pass
    
    # ----------------------------------------------------------------------------------------------------------------

    def blend():
        switchName = "L_Ctl_arm_switch"
        switchOfs = switchName.replace("Ctl", "Ofs")
        
        mpc.createCircle(n=switchName, c="yellow")
        mpc.createGroup(n=switchOfs)
        cmds.addAttr(switchName, ln="switch", nn=r"Ik/FK switch", attributeType='float', min=0, max=1, k=True)
        
        cmds.parent(switchName, switchOfs)
        mpc.MatchTransformation("L_Jnt_Wrist_Bnd", switchOfs)
        
        cmds.parent(switchOfs, "Controls")
        
        jntsDef = cmds.ls ("*_Bnd")
        jnts = []        
        for jnt in jntsDef:
            if "Jnt" in jnt:
                jnts.append(str(jnt))

        fkDef =  cmds.ls ("*_FK")
        fks = []
        for fk in fkDef:
            if "Jnt" in fk:
                fks.append(str(fk))
        
        ikDef =  cmds.ls ("*_IK")
        iks = []
        for ik in ikDef:
            if "Jnt" in ik:
                iks.append(str(ik))
                
        print(jntsDef, jnts)
        print(fkDef, fks)
        print(ikDef, iks)
        
        for jnt in jnts:
            blendTra = jnt.replace("Jnt", "blend")
            blendTra = blendTra + "_TRA"
            blendRot = jnt.replace("Jnt", "blend")
            blendRot = blendRot + "_ROT"
            
            cmds.createNode("blendColors", n=blendTra)
            cmds.createNode("blendColors", n=blendRot)

            cmds.connectAttr("{}.switch".format(switchName), "{}.blender".format(blendTra))
            cmds.connectAttr("{}.switch".format(switchName), "{}.blender".format(blendRot))
            
            # Connect blend colors with joints
            cmds.connectAttr("{}.output".format(blendTra), "{}.t".format(jnt))
            cmds.connectAttr("{}.output".format(blendRot), "{}.r".format(jnt))
    
        # Connect blend colors with joints
        for fk in fks:
            blendTra = fk.replace("Jnt", "blend")
            blendTra = blendTra + "_TRA"
            blendTra = blendTra.replace("FK", "Bnd")
                
            blendRot = fk.replace("Jnt", "blend")
            blendRot = blendRot + "_ROT"
            blendRot = blendRot.replace("FK", "Bnd")
                
            cmds.connectAttr("{}.t".format(fk), "{}.color1.".format(blendTra))
            cmds.connectAttr("{}.r".format(fk), "{}.color1.".format(blendRot))
        
        for ik in iks:
            blendTra = ik.replace("Jnt", "blend")
            blendTra = blendTra + "_TRA"
            blendTra = blendTra.replace("IK", "Bnd")
                
            blendRot = ik.replace("Jnt", "blend")
            blendRot = blendRot + "_ROT"
            blendRot = blendRot.replace("IK", "Bnd") 
                       
            cmds.connectAttr("{}.t".format(ik), "{}.color2.".format(blendTra))
            cmds.connectAttr("{}.r".format(ik), "{}.color2.".format(blendRot))
        
        # Creating reverse node
        rvName = switchName.replace("Ctl", "Rv")
        cmds.createNode("reverse", n=rvName)
        cmds.connectAttr("{}.switch".format(switchName), "{}.inputX".format(rvName))       
        
        # Visibility connections    
        cmds.connectAttr("{}.switch".format(switchName), "L_Ofs_arm_FK.visibility")
        cmds.connectAttr("L_Ofs_arm_FK.visibility", "L_Ofs_shoulder_FKctrl.visibility")
        
        cmds.connectAttr("{}.outputX".format(rvName), "L_Ofs_arm_IK.visibility")
        cmds.connectAttr("L_Ofs_arm_IK.visibility", "L_Ofs_Wrist_IKCtrl.visibility")
        
        pass
        
    # ----------------------------------------------------------------------------------------------------------------
        
    # Duplicating joint chains
    duplicateJnts(toDuplicate = "*_Ofs_arm_Bnd", oldSuffix = "Bnd", newSuffix = "FK", rad = 0.8, c="blue") # FKs
    duplicateJnts(toDuplicate = "*_Ofs_arm_Bnd", oldSuffix = "Bnd", newSuffix = "IK", rad = 0.5, c="red") # IKs
    
    # Build stuff
    fkBuild(r=3)
    ikBuild(r=4)
    blend()
    
    # Finishing function
    cmds.select (cl = 1) # Clear Selection

    pass

ui()

#sys.stdout.write ('Success!')
