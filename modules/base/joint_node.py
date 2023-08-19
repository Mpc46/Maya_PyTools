'''
/*****************************************************************************/
                            Joint Node v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Class based approach to work with joints and their properties.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + Joint [Class] (Inherits from Dag_Node)

>> NOTES >> 
	Update 11/08/2023 : Started to work on the script.
    Update 12/08/2023 : Added joint label functionality.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.

/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.base import Dag_Node
from modules.common.functions import getKeyFromValue
from modules.common.names import JOINT_LABEL_DICT

# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


class Joint(Dag_Node):
    """
    Joint [Class] (Inherits from: Dag_Node)

    Class based way of calling the information that we need to deal 
    with Maya joints in a clean Python way.
    """

    def __init__(self, node, **kwargs):

        Dag_Node.__init__(self, node)

        if node and kwargs:
            self.create(**kwargs)

        elif not kwargs and not self.exists():  # If only name given.
            self.create("joint")

    # -------------------------------------------------------------------------
    # DRAW STYLE

    @property
    def drawStyle(self):
        """ Returns joint Draw Style. """
        drawStyle = self.a.drawStyle.get()

        return drawStyle

    def setDrawStyle(self, value):
        """
        setDrawStyle of the joint

        0 = "Bone", 
        1 = "Multi-child as Box", 
        2 = "None"

        Args:
            value (int): The drawStyle to set.

        Returns:
            int: DrawStyle
        """
        if self.exists():
            if isinstance(value, int) and (value in range(0, 3)):
                self.a.drawStyle.set(value)
            else:
                raise ValueError(
                    ">>> Value should be an integer (0, 1 or 2)")

        return self.drawStyle

    # -------------------------------------------------------------------------
    # RADIUS

    @property
    def radius(self):
        radius = m.getAttr(self.node + ".radius")

        return radius

    def setRadius(self, value):
        if isinstance(value, (float, int)):
            m.setAttr(self.node + ".radius", value)
        else:
            raise ValueError(
                ">>> The passed value needs to be an int or float")

        return self.radius

    # -------------------------------------------------------------------------
    # JOINT ORIENTATION

    @property
    def jointOrient(self):
        """
        The joint orientation values

        Returns:
            list: The orient values [X, Y, Z]
        """
        orientX = self.a.jointOrientX.get()
        orientY = self.a.jointOrientY.get()
        orientZ = self.a.jointOrientZ.get()

        # If I don't unpack them, it will be a tuple inside a list.
        orient = [orientX, orientY, orientZ]

        return orient

    def setJointOrient(self, *args):
        """
        Set the joint orientation.
        If less tham 3 values passed, the rest will be 0.

        Returns:
            Obj: The joint new orientation

        Example:
           jnt.setJointOrient(40, 30)
           Output: [40, 30, 0]
        """
        if self.exists():
            if len(args) > 3 or len(args) == 0:
                raise ValueError(">>> You need to type 1, 2, or 3 values!")

            self.a.jointOrient.set(
                args[0] if len(args) >= 1 else 0,
                args[1] if len(args) >= 2 else 0,
                args[2] if len(args) == 3 else 0
            )

            return self.jointOrient

        else:
            print(">>> You cannot setOrient of an object that doesn't exist!")

    # -------------------------------------------------------------------------
    # JOINT LABEL

    @property
    def label(self):
        """
        Returns:
            list: [sideName, typeName, labelVisibility]
        """
        side = self.a.side.get()
        type = self.a.type.get()
        if type == 18:
            type = self.a.otherType.get()
            typeName = type

        drawLabel = self.a.drawLabel.get()

        sideName = getKeyFromValue(JOINT_LABEL_DICT["side"], side)
        typeName = getKeyFromValue(JOINT_LABEL_DICT["type"], type)

        if typeName == None:  # If key not in dictionary
            typeName = self.a.otherType.get()  # Get the custom labelType

        return [sideName, typeName, drawLabel]

    def setLabel(self, side, type, vis):
        """
        set the Label of the joint

        Args:
            side (str/int): The label side (ex: Left)
            type (str/int): The label side (ex: Head)
            vis (bool): The label visibility

        Returns:
            list: The joint label
        """
        self.setLabelSide(side)
        self.setLabelType(type)
        self.setLabelVis(vis)

        return self.label

    # ---- SIDE ------

    @property
    def labelSide(self):
        return self.label[0]

    def setLabelSide(self, side=0):
        if isinstance(side, int) and side in range(0, 4):
            side = side
        elif isinstance(side, str):
            side = side.lower()
            if side in JOINT_LABEL_DICT["side"]:
                side = JOINT_LABEL_DICT["side"][side]
        else:
            raise ValueError(
                ">>> side: {} is not defined".format(side)
            )

        self.a.side.set(side)

        return self.labelSide

    # ---- TYPE ------

    @property
    def labelType(self):
        return self.label[1]

    def setLabelType(self, type=0):
        if isinstance(type, int) and type in range(0, 30):
            if type != 18:
                type = type
            else:
                raise ValueError(
                    ">>> You did not entered a valid type number")
        elif isinstance(type, str):
            type = type
            if type.lower() in JOINT_LABEL_DICT["type"]:
                type = JOINT_LABEL_DICT["type"][type.lower()]
                self.a.type.set(type)
            else:
                self.a.type.set(18)
                typeName = type
                self.a.otherType.set(typeName, typ="string")
        else:
            raise ValueError(
                ">>> type: {} is not defined".format(type)
            )

        return self.labelType

    # ---- VISIBILITY ------

    @property
    def labelVis(self):
        return self.label[2]

    def setLabelVis(self, value=1):
        if type(value) == bool:
            value = value
        elif type(value) == int and value in range(0, 2):
            value = value
        else:
            raise ValueError(">>> You did not enter a valid value.")

        self.a.drawLabel.set(value)

        return self.labelVis

    