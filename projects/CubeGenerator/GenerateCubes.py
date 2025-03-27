'''
/*****************************************************************************/
                            Project v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    PARA HACER CUBOS :3

>> HOW TO USE >>
    Importa y corre desde Maya

>> NOTES >> 
	Update 25/03/2025 : Started to work on the script.

>> CONTACT >>
    luisf.carranza@outlook.com
    Copyright (C) 2025. All rights reserved.
    
/*****************************************************************************/
'''

# -----------------------------------------------------------------------------
# LIBRARIES AND MODULES
# -----------------------------------------------------------------------------
from maya import cmds as m
import random, string

# -----------------------------------------------------------------------------
# GLOBAL VARIABLES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# SCRIPT FUNCTIONS
# -----------------------------------------------------------------------------
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def createGrps():
    name = randomword(6)
    ctl = m.createNode("transform", n="CTL")
    jnt = m.createNode("transform", n="JNT")
    geo = m.createNode("transform", n="GEO")
    rig = m.createNode("transform", n="%s_Grp_rig" % (name))

    m.parent(ctl, rig)
    m.parent(jnt, rig)
    m.parent(geo, rig)
    
    return geo

def generarCubos(numCubos, geoGrp):
    for i in range(numCubos):
        # Posicioniento raro
        x = float(random.randrange(-12, 12))
        y = float(random.randrange(-12, 12))
        z = float(random.randrange(-12, 12))
        #nombre
        nombre = randomword(6) + "_Geo"
        cube = m.polyCube(n = nombre)
        m.move(x,y,z, cube)
        m.rotate(x,y,z, cube)
        # Jerarquia
        offGrp = m.createNode("transform", n = nombre + "_Ofs")
        con = m.parentConstraint(cube, offGrp, mo=False)
        m.delete(con)
        m.parent(cube, offGrp)
        m.parent(offGrp, geoGrp)

# -----------------------------------------------------------------------------
# EXECUTE SCRIPT
# -----------------------------------------------------------------------------
geoGrp = createGrps()
generarCubos(50, geoGrp)
