'''
/*****************************************************************************/
                            Auto-Rig Window v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Just a simple interface for me to test different functions and modules

>> HOW TO USE >>
	Just run on Maya

>> NOTES >> 
	Update 24/08/2023 : The script was created.

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
from modules.build.guides.base.biped_guide import Biped_Guide
from modules.build.systems.kinematic_system import switch, fk_system, ik_system

# -----------------------------------------------------------------------------
# SETTING UI
# -----------------------------------------------------------------------------


class AutoRig_Window(Window):
    """ Auto rig main window"""
    def __init__(self, WinTittle, window_name=None):
        self.title = WinTittle
        self.name = window_name
        self.size = (280, 280)

        super().__init__(self.title, self.name)

    def _build(self):
        self.initialLayout
        self.lay_test1()
       

    def lay_test1(self):
        m.separator(h=10)
        m.text("Build Base joints", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Test", c= lambda x: Biped_Guide("GuideJnt").build())
        m.button(l="Clean", c= lambda x: del_base())
        self.exitLayout
        m.button(l="mirror", c = lambda x: Biped_Guide("Guide").mirror() ) 

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# ----------------------------------------------------------------------------