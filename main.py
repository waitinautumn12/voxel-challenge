from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.06, exposure=3)
scene.set_directional_light((0.2, 0.2, 0.8), 0.1, (0.2, 0.2, 0.8))
scene.set_background_color((0.3, 0.4, 0.6))

@ti.kernel
def initialize_voxels():
    for i, j in ti.ndrange((-44, 50), (0, 10)):
        for k in ti.ndrange(8):
            scene.set_voxel(vec3(i, k, j), 1, vec3(0.5, 0.45, 0.3))
        

    for i, j in ti.ndrange((-64, -44), (0, 10)):
        for k in ti.ndrange(4):
            scene.set_voxel(vec3(i, k, j), 1, vec3(0.5, 0.45, 0.3))
    
    for i, j in ti.ndrange((50, 70), (0, 10)):
        for k in ti.ndrange(4):
            scene.set_voxel(vec3(i, k, j), 1, vec3(0.5, 0.45, 0.3))


    for i, j in ti.ndrange((-40, 50), (10, 20)):
        # H
        if (i == -40 and 10 < j < 17) or (-40 < i <= -36 and (j == 13)) or (i == -36  and 10 < j < 17):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.1, 0.8, 0.1))

        # E
        if (i == -32 and 10 < j < 17) or (-32 < i <= -28 and (j == 11 or j == 13 or j == 16)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.2, 0.7, 0.1))

        # L
        if (i == -24 and 10 < j < 17) or (-24 < i <= -20 and (j == 11)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.3, 0.6, 0.1))
        
        # L
        if (i == -16 and 10 < j < 17) or (-16 < i <= -12 and (j == 11)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.4, 0.5, 0.06))

        # O
        if (i == -8 and 11 < j < 16) or (-8 < i <= -5 and (j == 11 or j == 16)) or(i == -4 and 11 < j < 16):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.5, 0.5, 0))

        # T
        if (i == 6 and 10 < j < 17) or (3 < i <= 8 and (j == 16)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.5, 0.5, 0))

        # A
        if (i == 12 and 10 < j < 14) or (i == 13 and 13 < j < 16) or (i == 14 and j == 16) or (i == 15 and 13 < j < 16) or (i == 16 and 10 < j < 14) or (12 < i <= 16 and (j == 12)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.4, 0.5, 0.06))

        # I
        if (i == 21 and 11 < j < 16) or (19 < i <= 22 and (j == 11 or j == 16)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.3, 0.6, 0.1))

        # C
        if (i == 26 and 11 < j < 16) or (26 < i <= 30 and (j == 11 or j == 16)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.2, 0.7, 0.1))

        # H
        if (i == 34 and 10 < j < 17) or (34 < i <= 38 and (j == 13)) or (i == 38  and 10 < j < 17):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.1, 0.8, 0.1))

        # I
        if (i == 44 and 11 < j < 16) or (42 < i <= 45 and (j == 11 or j == 16)):
            scene.set_voxel(vec3(i, j, 5), 1, vec3(0.1, 0.8, 0.1))

initialize_voxels()
scene.finish()