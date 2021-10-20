import bpy

def eqGenerate(functions):
    eq = '0'
    while len(functions):
        f = functions.pop(0)
        eq = f(eq)
    return eq

bpy.ops.object.delete(use_global=False, confirm=False)

functions = [
#    level=
    lambda z: z + '0.2',
#    slopping=
    lambda z: z + '+(y+1)/2*1.2',
#    stopping=
    lambda z: z+'+max(0,-y-1+1/40)*40*20*(x*x)',
#    centering=
    lambda z: z + '+(x*x)',
#    standing=
    lambda z: 'min(('+z+'),10-10*(x*x+y*y)/2)',
]

bpy.ops.mesh.primitive_z_function_surface(
                    equation=eqGenerate(functions),
                    div_x=100,
                    div_y=800,
                    size_x=2,
                    size_y=2)                    
bpy.context.object.name = "Egg Dispenser" 
bpy.ops.transform.resize(value=(0.5, 0.5, 1))
bpy.ops.transform.resize(value=(0.001, 0.001, 0.001))
bpy.ops.transform.resize(value=(60, 400, 10))
#bpy.ops.object.modifier_add(type='REMESH')
#bpy.context.object.modifiers["Remesh"].voxel_size = 0.001
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.003
