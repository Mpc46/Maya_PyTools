'''
/*****************************************************************************/
                            Code Snippets v 1.0
                     ________________________________________
                    |                                        |
                    |  Author: Luis Felipe Carranza          |
                    |________________________________________|

>> DESCRIPTION >>
    Test script for our Dag_Node to test functionality.

>> HOW TO USE >>
	Set up a scene with two empty groups inside:
        CTRL_GRP
        MODEL_GRP
    Populate the model_grp with polyspheres with different positions.
    Run the code in Maya.
 
>> NOTES >> 
	Update 04/08/2023 : Start working on the script

>> THANKS >> 
    Nick Hughes [04/08/2023]:
        For his awesome course that led me to create this file. 
 
/*****************************************************************************/
'''
from maya import cmds

def dag_snippets():
    from modules.base import Dag_Node

    CTRL_GRP = Dag_Node("CTRL_GRP")
    MODEL_GRP = Dag_Node("MODEL_GRP")

    # rocks = [Dag_Node(i) for i in m.ls(sl=1)]
    rocks = [i for i in MODEL_GRP.children]

    for num, rock in enumerate(rocks):
        ctrl = Dag_Node(cmds.circle(n="rock_CTRL"+str(num+1), r=1.5)[0])
        ctrl.parentTo(CTRL_GRP)
        ctrl.moveTo(rock)

        ctrl.createOffset()
        ctrl.setColor("yellow")

        ctrl.parentConstraint(rock)
        ctrl.scaleConstraint(rock)

def attribute_snippets():
    #######
    ####### Setting controllers in the scene to hidden
    #######


    from modules.base import Dag_Node as Dag

    main = Dag("teapot_CTRL")
    main.a.add(ln="hide_on_playback", nn="Hide on Playback", at="long", min=0, max=1, dv=1, k=1)

    for ctrl in [Dag(i) for i in m.ls("*", typ="nurbsCurve")]:
        main.a.hide_on_playback >> ctrl.a.hideOnPlayback


    #######
    ####### Setting controllers in the scene to hidden
    #######


    def changeColourIntensity(value=1.1, materials=None):
        """ Takes a value and multiples the current colour assigned shader RGB setting. """
        mtls = materials if materials else [Dag(i) for i in m.ls(sl=1)]
        for mtl in mtls:
            mtl.a.colorR.set( mtl.a.colorR.get() * value )
            mtl.a.colorG.set( mtl.a.colorG.get() * value )
            mtl.a.colorB.set( mtl.a.colorB.get() * value )

def mesh_snippets():
    #######
    ####### Update mesh
    #######

    from modules.base import Mesh, Dag_Node as Dag

    meshes = [Mesh(i) for i in m.ls(sl=1)]

    for mesh in meshes:
        if not Dag(mesh.name.replace("__OLD", "")).exists():
            print("NOT EXISTING: ", mesh.name.replace("__OLD", ""))
            continue

        newMesh = Mesh(mesh.name.replace("__OLD", ""))

        # Copy weights

        if mesh.skinCluster:
            mesh.copyWeightsTo(newMesh)

        # Copy deformers

        if mesh.deformers:
            mesh.addDeformersTo(newMesh)

        # Update blends

        if mesh.blendShapes:
            mesh.blendShape.reconnectBlendShapeTo(newMesh)

        # Copy materials

        if mesh.materials:
            mesh.addMaterialsTo(newMesh)