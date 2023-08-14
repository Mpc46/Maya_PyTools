'''
/*****************************************************************************/
                            Window Base Example v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Small description of what does this script or module does.

>> HOW TO USE >>
	Input instructions on how to use

>> CONTENTS >> 
    + file

>> NOTES >> 
	Update 14/08/2023 : The script was created.

/*****************************************************************************/
'''
# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.interface import Window_Base as Window

# -----------------------------------------------------------------------------
# SETTING UI
# -----------------------------------------------------------------------------

class win(Window):

    def __init__(self, window_name, WinTittle="win2"):
        self.name = window_name
        self.title = WinTittle
        self.size = (280, 280)

        super().__init__(window_name, WinTittle)

    
    def _build(self):
        m.columnLayout(adj=1)
        self.layout1()
        m.separator(h=20)
        self.layout2()

    def layout1(self):
        m.rowColumnLayout(nc=2)
        m.button(l="I AM")
        m.button(l="SO FUCKING")
        self.exitLayout
        m.columnLayout(adj=1)
        m.button(l="TIRED")
        m.button(l="HAHAHA")
        self.exitLayout

    def layout2(self):
        m.columnLayout(adj=1)
        m.button()
        m.button()
        m.textField()
        m.intSlider()
        m.floatSlider()
        m.text(l='Blahhhhh')
        m.textScrollList()
        self.exitLayout        

window = win("Window Tittle")
window.open()