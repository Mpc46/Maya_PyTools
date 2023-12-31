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
from modules.build.guides.base.guide_biped import Biped_Guide
from modules.build.guides import (mirror_guide, 
                                  toggle_guide_name, 
                                  toggle_guide_axis,
                                  build_guide)


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
        self.lay_create_guides()
        self.lay_build_from_guides()

    def lay_create_guides(self):
        m.separator(h=10)
        m.text("Build Base joints", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Create Guides", c = lambda x: Biped_Guide("GuideJnt").build())
        m.button(l="Clean", c = lambda x: del_base())
        self.exitLayout
        m.separator(h=10)
        m.button(l="Mirror Guides", c = lambda x: mirror_guide() ) 
        m.separator(h=10)
        m.button(l="Toggle guide Names", c = lambda x: toggle_guide_name() ) 
        m.button(l="Toggle guide Axis", c = lambda x: toggle_guide_axis() ) 

    def lay_build_from_guides(self):
        m.separator(h=10)
        m.text("Build Base joints", h=20, fn="boldLabelFont", rs=True) # Just a tittle
        m.separator(h=10)
        # Layout
        m.rowColumnLayout(nc=2, adj=1)
        # Buttons
        m.button(l="Build Rig", c = lambda x: build_guide())
        m.button(l="Clean", c = lambda x: del_base())
        self.exitLayout
       


# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# ----------------------------------------------------------------------------

def del_base():
    m.delete("Guide")