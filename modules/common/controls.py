'''
/*****************************************************************************/
                            Common Controls v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Pre-made control curves to use in scripts and scenes.

>> HOW TO USE >>
	This module contents are intended to be imported, referenced or
    inheritance to another class.

>> NOTES >> 
	Update 02/09/2023 : Started to work on the script.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2023. All rights reserved.
    
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------

from maya import cmds as m
from modules.base import Curve

# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------

def gear(name = "gear"):
    points = [[0.21603651945719954, 1.3791639334092862e-16, -0.9999999450684957], 
              [1.3732739104155965e-08, 1.3791639334092862e-16, -1.0], 
              [-0.21603649199172023, 1.3791639334092862e-16, -0.9999999450684957], 
              [-0.16479234607656865, 1.3791639334092862e-16, -0.7752870977708756], 
              [-0.2449291652082523, 1.3791639334092862e-16, -0.7538145018005422], 
              [-0.32238248900073263, 1.3791639334092862e-16, -0.7240829564026557], 
              [-0.4212858022220725, 1.3791639334092862e-16, -0.6614361270186367], 
              [-0.5615744718243212, 1.3791639334092862e-16, -0.8482670952399188], 
              [-0.6677740248751424, 1.3791639334092862e-16, -0.7420676975051386], 
              [-0.7420676837724013, 1.3791639334092862e-16, -0.6677740386078793], 
              [-0.8482670815071806, 1.3791639334092862e-16, -0.5615744855570556], 
              [-0.6614361132858948, 1.3791639334092862e-16, -0.42128581595480996], 
              [-0.7240829426699158, 1.3791639334092862e-16, -0.3223825027334723], 
              [-0.7538144880678022, 1.3791639334092862e-16, -0.24492917894099184], 
              [-0.7752870840381361, 1.3791639334092862e-16, -0.16479235980930768], 
              [-0.9999999313357568, 1.3791639334092862e-16, -0.2212772834749046], 
              [-0.9999999862672607, 1.3791639334092862e-16, -2.6249900909976018e-16], 
              [-0.9999999313357568, 1.3791639334092862e-16, 0.22127728347490364], 
              [-0.7752870840381361, 1.3791639334092862e-16, 0.16479235980930695], 
              [-0.7538144880678022, 1.3791639334092862e-16, 0.24492917894099106], 
              [-0.7240829426699158, 1.3791639334092862e-16, 0.32238250273347174], 
              [-0.6630478603563272, 1.3791639334092862e-16, 0.41967406888438885], 
              [-0.849017585726927, 0.0, 0.560823981337324], 
              [-0.7420676837723974, 0.0, 0.6677740386078822], 
              [-0.6677740248751389, 0.0, 0.74206769750514], 
              [-0.560823967604561, 0.0, 0.849017599459689], 
              [-0.4196740551516422, 0.0, 0.6630478740890717], 
              [-0.3223824890007329, 0.0, 0.7240829564026543], 
              [-0.2449291652082523, 0.0, 0.75381450180054], 
              [-0.16479234607656879, 0.0, 0.7752870977708738], 
              [-0.21603649199172079, 0.0, 0.9999999450684962], 
              [1.3732738828323178e-08, 0.0, 1.0], 
              [0.21603651945719762, 0.0, 0.9999999450684962], 
              [0.16479237354204604, 0.0, 0.7752870977708738], 
              [0.24492919267373026, 0.0, 0.7538145018005402], 
              [0.32238251646621086, 0.0, 0.724082956402654], 
              [0.4212858296875513, 0.0, 0.6614361270186357], 
              [0.5615745381184206, 0.0, 0.8482671340685369], 
              [0.667774013511999, 0.0, 0.7420676586765155], 
              [0.742067672409258, 0.0, 0.667773999779256], 
              [0.8482671478012801, 0.0, 0.5615745243856729], 
              [0.661436140751372, 1.3791639334092862e-16, 0.4212858159548099], 
              [0.724082970135393, 1.3791639334092862e-16, 0.322382502733472], 
              [0.7538145155332788, 1.3791639334092862e-16, 0.24492917894099106], 
              [0.7752871115036131, 1.3791639334092862e-16, 0.16479235980930723], 
              [0.9999999862667116, 1.3791639334092862e-16, 0.22127728347490436], 
              [0.9999999862672607, 1.3791639334092862e-16, 2.912578472088767e-16], 
              [0.9999999862667116, 1.3791639334092862e-16, -0.22127728347490316], 
              [0.7752871115036131, 1.3791639334092862e-16, -0.1647923598093071], 
              [0.7538145155332788, 1.3791639334092862e-16, -0.24492917894099092], 
              [0.724082970135393, 1.3791639334092862e-16, -0.3223825027334711], 
              [0.6630478878218046, 1.3791639334092862e-16, -0.4196740688843877], 
              [0.849017613192404, 1.3791639334092862e-16, -0.5608239813373235], 
              [0.7420677112378746, 1.3791639334092862e-16, -0.6677740386078811], 
              [0.6677740523406147, 1.3791639334092862e-16, -0.7420676975051396], 
              [0.5608239950700369, 1.3791639334092862e-16, -0.8490175994596892], 
              [0.41967408261712014, 1.3791639334092862e-16, -0.6630478740890715], 
              [0.3223825164662114, 1.3791639334092862e-16, -0.724082956402654], 
              [0.24492919267373053, 1.3791639334092862e-16, -0.7538145018005402], 
              [0.16479237354204632, 1.3791639334092862e-16, -0.7752870977708741]]
    
    gear_main = build_ctl_from_points(name, points)
    
    points = [[0.2578851244515095, 1.3791639334092862e-16, -0.44667011428043385], 
              [1.3732738828323178e-08, 1.3791639334092862e-16, -0.5157702214375396], 
              [-0.25788509698603024, 1.3791639334092862e-16, -0.4466701142804341], 
              [-0.4466701005476951, 1.3791639334092862e-16, -0.2578851107187698], 
              [-0.5157702077048, 1.3791639334092862e-16, -4.205638245074571e-16], 
              [-0.4466701005476954, 1.3791639334092862e-16, 0.2578851107187694], 
              [-0.2578850969860305, 1.3791639334092862e-16, 0.4466701142804343], 
              [1.3732738828323178e-08, 1.3791639334092862e-16, 0.5157702214375388], 
              [0.2578851244515087, 1.3791639334092862e-16, 0.4466701142804347], 
              [0.4466701280131736, 1.3791639334092862e-16, 0.25788511071876963], 
              [0.5157702351702783, 1.3791639334092862e-16, 2.353737342947316e-16], 
              [0.44667012801317385, 1.3791639334092862e-16, -0.25788511071876946]]
    
    gear_inner = build_ctl_from_points(n = "gear_circle", cvs = points)
    
    gear_main.mergeCurves(gear_inner)

    return gear_main


def build_ctl_from_points(n = "ctl", cvs = None):
    ctl = Curve(m.circle(n = n, s = len(cvs), normal = [0,1,0]) [0])
    
    pnt = 0

    for i in cvs:
        m.move(i[0], i[1], i[2], '{}.cv[{}]'.format(n, pnt))
        pnt += 1
    
    return ctl

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------

gear()