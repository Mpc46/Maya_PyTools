'''
/*****************************************************************************/
                                Path v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    String functionality for maya object paths

>> HOW TO USE >>
	This module is meant to be imported into larger scripts.

>> CONTENTS >>
    + generateReprString (Func);
    + rootName (Func);
    + baseName (Func); 
    + namespace (Func); 

>> NOTES >> 
	Update 02/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [02/08/2023]:
        For his awesome course that led me to create this file. 

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------


def generateReprString(cls, name):
    """
    generateReprString [Function]

    Generates the string representation for the __repr__ dunder method.

    Args:
        cls  (str): The cls.__name__ of the class.
        name (str): The node used.

    Returns:
        str: The string representation for the __repr__ special method.

    Example:
        __repr__ = generateReprString(
            self.__class__.__name__,
            self.fullPath
        )
        
        # Output: Dep_Node("sphere_Grp")
    """
    
    return "{cls}('{node}')".format(cls=cls, node=rootName(name))


def rootName(name):
    """
    rootName [Function]

    Strips grouping information from a given full path.

    Args:
        name (str): The name containing group information.

    Returns:
        str: The name without grouping information.

    Example:
        name = "base_GRP|sub_GRP|namespace:sphere_GEO"
        rootName(name)

        # Output: "namespace:sphere_GEO"
    """

    if not name:
        return name

    return name.split("|")[-1]


def baseName(name):
    """
    baseName [Function]

    This function will strip the namespaces and grouping information
    of a name. This is useful when working with full paths but needing
    the base for naming.

    Args:
        name (str): The name containing group information.

    Returns:
        str: The name without grouping or namespace information.

    Example:
        name = "namespace:base_GRP|namespace:sub_GRP|namespace:sphere_GEO"
        baseName(name)

        # Output: "sphere_GEO"
    """

    if not name:
        return name

    return name.split("|")[-1].split(":")[-1]


def namespace(name):
    
    """
    namespace [Function]

    This function will return the namespace if any exists.

    Args:
        name (str): The name containing namespace information.

    Returns:
        str: The namespace.

    Example:
        name = "namespace:base_GRP|namespace:sub_GRP|namespace:sphere_GEO"
        namespace(name)

        # Output: "namespace"
    """

    if not name:
        return name
    
    if name.find(":") != -1:
        return rootName(name).rsplit(":", 1)[0]
