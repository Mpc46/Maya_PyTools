'''
/*****************************************************************************/
                            Window Base Example v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Just a simple interface for me to test different functions and modules

>> HOW TO USE >>
	Just run on Maya

>> NOTES >> 
	Update 16/08/2023 : The script was created.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''
# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.interface import Window_Base as Window
from modules.build.systems.kinematic_system import switch, fk_system, ik_system

# -----------------------------------------------------------------------------
# SETTING UI
# -----------------------------------------------------------------------------


class win(Window):

    def __init__(self, WinTittle, window_name=None):
        self.title = WinTittle
        self.name = window_name
        self.size = (280, 280)

        super().__init__(self.title, self.name)

    def _build(self):
        self.initialLayout
        self.lay_test1()
        self.lay_test2()
        self.lay_test3()
        self.lay_test4()

    def lay_test1(self):
        m.separator(h=10)
        m.text("Build Base joints", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Test", c= lambda x: build_arm())
        m.button(l="Clean", c= lambda x: del_base())
        
        self.exitLayout

    def lay_test2(self):
        m.separator(h=10)
        m.text("Create switch", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Test", c= lambda x: switch(joints_base))
        m.button(l="Clean", c= lambda x: del_switch())
        
        self.exitLayout
    
    def lay_test3(self):
        m.separator(h=10)
        m.text("Create FK", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Test", c= lambda x: fk_system(joints_base))
        m.button(l="Clean", c= lambda x: del_switch())
        
        self.exitLayout
    
    def lay_test4(self):
        m.separator(h=10)
        m.text("Create IK", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Test", c= lambda x: ik_system(joints_base))
        m.button(l="Clean", c= lambda x: del_switch())
        
        self.exitLayout

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# ----------------------------------------------------------------------------

def build_arm():
    m.joint(n="L_Shoulder", p=(0.568, 4.792, -0.052), o=(0, 2, 0))
    m.joint(n="L_Elbow", r=True, p=(4.41, 0, 0), o=(0, -4, 0))
    m.joint(n="L_Wrist", r=True, p=(3.765, 0, 0))
    m.select(cl=True)

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# ----------------------------------------------------------------------------


joints_base = ["L_Shoulder", "L_Elbow", "L_Wrist"]
def del_base():
    m.delete(joints_base)
    return None

def del_switch():
    m.delete(joints_base)
    m.delete("L_Wrist_switch_CTL_OFF_GRP")
    m.delete("L_Shoulder_IK")
    m.delete("L_Shoulder_FK")
    return None


# window = win("Testing kinematics")
# window.open()
