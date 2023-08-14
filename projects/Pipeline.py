'''
/****************************************** Pipeline v 2.5 ***************************************************************************/
                                 ________________________________________
                                |                                        |
                                |  Script done by: Luis Felipe Carranza  |
                                |________________________________________|
>> HOW TO USE >>
    The buttons are in the same order that need to be pressed for the script to work. 
    The script will find animations, copy them to the controls, bake them into the joints and export the resulting animation to
    a file or multiple files, depending on the number of individual objects found on scene.
    
>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.

**************************************************************************************************************************************/
'''
# Libraries
import maya.cmds as cmds
import maya.mel as mel
import sys

# ----------------------------------------------------------------------------------------------------------------
#                                               SETTING UI
# ----------------------------------------------------------------------------------------------------------------

def ui():
    # Set up UI basics.
    win = 'Pipeline'

    if (cmds.window(win, exists=1)):
        cmds.deleteUI(win)
    cmds.window(win, rtf=1, w=280, h=150, t=win, s=1)
    cmds.columnLayout(adj=1)
    
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    
    # --- Create tab for exporting ---
    tab1 = cmds.columnLayout(adj=1) # Start of this tab
    cmds.separator(h=20)
    cmds.button(l="Export", h=75, c=lambda x: copyAnim()) # This button will export the joints into Fbx's
    cmds.setParent('..') # End of this tab

    # --- Create tab for settings ---
    tab2 = cmds.columnLayout(adj=1) # Start of this tab
    cmds.text("Set Animation range", h=20, fn="boldLabelFont", rs=True) # Just a tittle
    cmds.rangeControl("animRange", height=25, visible=True) # A range control for the animation range
    cmds.separator(h=20) # Separator to keep it tidy
    cmds.text("Set objects to export", h=20, fn="boldLabelFont", rs=True) # Just a tittle
    for obj in animObjs:
        objName = obj#.split("_")[0]
        cmds.checkBox("{}".format(objName), l="{}".format(objName), value=True)
    cmds.separator(h=20) # Separator to keep it tidy
    # Checkboxes to get more granular control of the script.
    cmds.checkBox("delSrcObj", label='Delete source animated objects', value=True) # If checked the proxy geo will be deleted
    cmds.checkBox("bakeAnim", label='Bake Animation to joints', value=False) # If checked it will bake animation into the joints
    cmds.separator(h=20) # Separator to keep it tidy
    # Menu list of available formats to export as.
    cmds.optionMenu("Format", label='Format')
    cmds.menuItem(label='FBX')
    cmds.menuItem(label='Maya Ascii')
    cmds.menuItem(label='Maya Binary')
    cmds.setParent('..') # End of this tab

    # --- Create tabs ---
    cmds.tabLayout(tabs, edit=True, tabLabel=((tab1, 'Export'), (tab2, 'Settings')))

    # Launch the UI.
    cmds.showWindow(win)

# ----------------------------------------------------------------------------------------------------------------
#                                               GLOBAL VARIABLES
# ----------------------------------------------------------------------------------------------------------------

# Global variables
allObjs = cmds.ls(type="transform")  # Fetches all the objects on scene
animObjs = []  # Empty list to assign objects with animation curves
ctlObj = []  # Empty list to assign controls if the "geo" has anim curves
path = cmds.file(q = 1, sn = 1) # Scene path

# ----------------------------------------------------------------------------------------------------------------
#                                               SCRIPT FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------

def getAniObjs():
    for i in allObjs:
        animCrv = cmds.listConnections(i, type="animCurve") # Checks if the object has animations
        if animCrv:
            if i not in animObjs: # It will check if obj already on list
                animObjs.append(str(i)) # If obj not in list it will add it.
            else:
                continue # If obj already exist it will continue
    if animObjs:
        sys.stdout.write ('Success! {} animated objects found on scene.'.format(len(animObjs)))  
        sys.stdout.write("\n") # Create an empty line
    else:
        sys.stdout.write ('Error! No animated objects found on scene.')           
    for obj in allObjs:
        if "_cnt" in obj: # It will search for controls in the scene
            if "Root_" in obj:
                if obj not in ctlObj:
                    ctlObj.append(str(obj)) # Add the control into a list
            else:
                continue
        else:
            pass

def copyAnim():  # Search from the entire objs if some objects match name
    amount = 0
    cmds.progressWindow(title='Exporting animation',
					progress=amount,
                    max=len(ctlObj))
    
    start = int(cmds.playbackOptions(query=True, min = 1)) # Anim range start time
    end = int(cmds.playbackOptions(query=True, max = 1)) # Anim range end time
    timeRange = (start, end) # Range of animation to export
    checkBoxDelSrc = cmds.checkBox("delSrcObj", query=True, value=True) #   Checks checkbox value
    checkBoxBake = cmds.checkBox("bakeAnim", query=True, value=True)
    
    # Pair controls and Geo proxy to copy the animations
    for ctl in ctlObj:
        ctlName = ctl.split(":")
        for geo in animObjs:
            checkBox_Anim = cmds.checkBox("{}".format(geo), query=True, value=True) #   Checks checkbox value
            if checkBox_Anim == True: # If is selected to export
                geoName = geo.split("_") # Split the string to check later
                if ctlName[0] == geoName[0]: # Check if they have similar strings
                    cmds.copyKey(geo, an="objects", t=timeRange) # Copy the animation key
                    cmds.pasteKey(ctl) # Paste the animation key to the control
                    # --- Delete Source Object ----
                    if checkBoxDelSrc == True: # If checkbox checked
                        parent = cmds.listRelatives(geo, pa=True, ap=True) # Get the parent of the objects
                        cmds.delete(geo) # After checkong the parents, delete everything
                        kid = cmds.listRelatives(parent[0], c=True)
                        if kid is None: # If theres no object inside parent group
                            cmds.delete(parent[0]) # delete parent group
                # --- Bake joint animation ----    
                AllJnts = [jnt for jnt in cmds.ls(type='joint')]                                                    
                for jnt in AllJnts:
                    if geoName[0] in jnt: # Matches geo with joint
                        jntPar = cmds.listRelatives(jnt, parent=True)
                        cmds.parent(jnt, w=True)
                        cons = cmds.ls(type="constraint") # Checks if there are constrains and disable them
                        for con in cons:
                            if jnt.split(":")[0] in con.split(":")[0]: # Just delete neccessary constraints
                                cmds.delete(con) # Batch delete the constraints         
                        if checkBoxBake == True: # Checks if bake is enable 
                            bakeAnimation(jnt=jnt) # Copy keyframes
                        else:
                            if cmds.listConnections(ctl, type="animCurve") is not None: # if animation exists
                                if ctlName[0] in jnt: # Matches control with joint
                                    cmds.copyKey(ctl, t=timeRange) # Copy the animation key
                                    cmds.pasteKey(jnt) # Paste the animation key to the control
                        # --- Export animation ---- 
                        exportFbx(jnt=jnt)
                        cmds.parent(jnt, jntPar)
                else:
                    continue  
        amount += 1
        cmds.progressWindow(edit=True, progress=amount)
    cmds.progressWindow(endProgress=1) # Close the progress bar

def bakeAnimation(jnt=''):
        animatable = cmds.listAnimatable(ctlObj) # Animatable objects
        for attr in animatable:
            Animkey = cmds.keyframe(attr, query=1, keyframeCount=True) # how many keys in attribute
            if Animkey > 0:
                tempo = cmds.keyframe(attr, query=1, index=(0, Animkey), timeChange=True) # Time of keyframe
                value = cmds.keyframe(attr, query=1, index=(0, Animkey), valueChange=True) # Value of keyframe on attribute
                for i in range(0, Animkey):
                    if jnt in attr: # Checks if the jnt and control are the same before procceding
                        currentTime = tempo[i] # The current keyframe
                        val = value[i] # The value of the current atribute on current time
                        cleanAttr = attr.partition(".")[-1] # Iw will only shopw the attribute name
                        print("atribute name {}, time to keyframe {}, attribute value{}".format(cleanAttr, currentTime, val))
                        cmds.currentTime(currentTime)
                        cmds.setAttr("{}.{}".format(jnt, cleanAttr), val) # Set the value to joint
                        cmds.setKeyframe(str(jnt), at=str(cleanAttr), t=currentTime) # Add the corresponding keyframe

def exportFbx(jnt):
    sceneName = path.split('/')[-1] # The path were the scene is saved
    item = cmds.optionMenu("Format", q=True, value=True)
    if "Root" in jnt:
        if ":" in jnt:
            jntName = jnt.replace(":", "_") # To avoid writing error, the string is replace
            newPath = path.replace(sceneName, "{}".format(jntName)) # adding the name on the path
            cmds.select(jnt) # We need to select what we need to export
            if "FBX" in item: # For FBX Only
                mel.eval("FBXResetExport")  # Reset options.
                mel.eval("FBXProperty Export|IncludeGrp|Animation -v true") # Include animation on export
                mel.eval("FBXProperty Export|IncludeGrp|Animation|ExtraGrp|RemoveSingleKey -v false") # Default True
                mel.eval("FBXProperty Export|IncludeGrp|CameraGrp|Camera -v false") # Do not export cameras
                mel.eval('FBXExport -f "{}.fbx" -s'.format(newPath)) # '-s' for selected.
            elif 'Maya Ascii' in item: # For Ma Only
                cmds.file("{}.ma".format(newPath), force=True, options="v=0;", type="mayaAscii", es=True)
            elif 'Maya Binary' in item: # For Mb Only
                cmds.file("{}.mb".format(newPath), force=True, options="v=0;", type="mayaBinary", es=True)
            cmds.select(cl=True) # Clear Selection     

# ----------------------------------------------------------------------------------------------------------------
#                                               EXECUTE SCRIPT
# ----------------------------------------------------------------------------------------------------------------

getAniObjs() # Get animated Objects on scene
ui() # Executing the UI