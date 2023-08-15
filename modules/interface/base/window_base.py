'''
/*****************************************************************************/
                                Window Base v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Maya window UI base class.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Window_Base [Class]

>> NOTES >> 
	Update 14/08/2023 : Start working on the script

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.common import functions
from modules.utils import path

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Window_Base(object):
    """
    Window_Base [Class]

    Base Maya window UI class

    Args:
        title (str): The window title

    Contents:
    - BASIC UI FUNCTIONALITY:
        + open (opens the window) [Method]
        + close (closes the window) [Method]
    """

    # -------------------------------------------------------------------------
    # SPECIAL/MAGIC/DUNDER METHODS

    def __init__(self, window_title, window_name=None):
        self.title = window_title
        self.size = (280, 280)

        if window_name:
            self.name = window_name
        else:
            self.name = functions.ToCamelCase(window_title)

        # self.open()

    def __repr__(self):
        return path.generateReprString(
            self.__class__.__name__,
            self.title)

    # -------------------------------------------------------------------------
    # LAYOUT PROPERTIES

    @property
    def exitLayout(self):
        """ Return to parent Layout"""
        return m.setParent('..')

    @property
    def initialLayout(self):
        """ Simple column Layout. """
        return m.columnLayout(adj=1)

    # -------------------------------------------------------------------------
    # WINDOW UI ACTIONS

    def open(self, **kwargs):
        """
        open [Method]

        You can additionally and optionally add maya commands as arguments. 
        Example: win.open(title="Long Name", iconName='Short Name')
        """
        if (m.window(self.name, exists=1)):
            m.deleteUI(self.name)
        m.window(self.name, widthHeight=self.size,
                 t=self.title, rtf=1, s=1, **kwargs)

        self._build()

        m.showWindow(self.name)

    def close(self):
        if self.name in m.lsUI(windows=1):
            m.deleteUI(self.name, window=True)

    # -------------------------------------------------------------------------
    # WINDOW UI BUILD

    def _build(self):
        self.initialLayout
