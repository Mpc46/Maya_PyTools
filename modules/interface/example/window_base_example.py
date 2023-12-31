'''
/*****************************************************************************/
                            Window Base Example v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Just an example of a working maya window using a sub-class

>> HOW TO USE >>
	Just run on Maya

>> NOTES >> 
	Update 14/08/2023 : The script was created.

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
        self.layout1()
        m.separator(h=20)
        self.layout2()

    def layout1(self):
        m.columnLayout(adj=1)

        # Fill the UI with stuff.

        # This was of writing button commands only work if this script is ran in global scope.
        m.button(l='Button A', c='func2()')

        # Two ways that will work regardless of scope.
        m.button(l='Button B',
                 c='from Test.PythonTest import pythonTest; pythonTest()')
        m.button(l='Button C', c=lambda x: func2())

        # Some common UI element create commands to use.
        m.button()
        m.button()
        m.textField()
        m.intSlider()
        m.floatSlider()
        m.text(l='Blahhhhh')
        m.textScrollList()

        # Nest a layout with multiple columns
        m.rowColumnLayout(nc=2)
        m.button()
        m.button()
        m.button()
        m.button()

        self.exitLayout

    def layout2(self):
        m.button()
        m.button()
        self.exitLayout

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


def func2():
    print("yes")

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# ----------------------------------------------------------------------------


window = win("Window Tittle").open()
# window.open()
