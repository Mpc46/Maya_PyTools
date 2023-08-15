'''
/*****************************************************************************/
                             functions v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    All common needed functions.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> CONTENTS >> 
    + getKeyFromValue [Func]
    + ToCamelCase [Func]

>> NOTES >> 
	Update 12/08/2023 : Start working on the script

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
 
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def getKeyFromValue(dictionary, target_value):
    """
    getKeyFromValue [Function]

    Get a dictionary key from it's value
    key:value

    Args:
        dictionary (dict): The dictionary to use
        target_value (any): the value to get key from

    Returns:
        key: The key value

    Example:
        my_dic = {"one":1, "two":2}
        getKeyFromValue(my_dic, 1)
        Output: "one"
    """
    for key, value in dictionary.items():
        if value == target_value:
            return key
        
    return None  # >>> No key was found for the value


def ToCamelCase(string, splitBy=None):
    """
    ToCamelCase [Function]

    Takes a string and returns a camel case version of it.

    Args:
        string (str): A string to camel case.
        splitBy (str/optional): the parameter to split with.


    Returns:
        str: AStringToCamelCase.
    """
    string_Title = string.title()  # Makes every word upperCase

    if splitBy is not None:
        string_List = string_Title.split(splitBy)  # Creates list
    else:
        string_List = string_Title.split()

    if len(string_List) > 1:
        camelCase = "".join(string_List)  # Merge list into string
        return camelCase
    else:
        return string_Title  # Nothing to Split just return title string
