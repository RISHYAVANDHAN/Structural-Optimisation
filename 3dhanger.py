from mesh_tool import *
import argparse

parser = argparse.ArgumentParser(description="generate a basic mesh. bulk2d/3d is unit square/cube by default. Further default geometries are cantilever 3x2(x1) and mbb2d (1x0.5) ")
parser.add_argument("--res", help="elements in x-direction", type=int, required = True )
args = parser.parse_args()

# Dimensions of the box (m)
width = 1
height = 5
depth = 10

nx = args.res  
ny = int((height / width) * nx)
nz = int((depth / width) * nx)
mesh = create_3d_mesh(nx, ny, nz, width, height, depth)

y_slope = height / (depth / 2) + 0.1 * width  
solid_gap = 0.025 * height
mech_gap = 0.3 * height  

for e in mesh.elements:
    x, y, z = mesh.calc_barycenter(e)
    
    if z <= depth / 2:
        diagonal_y = z * y_slope 
    else:
        diagonal_y = (depth - z) * y_slope  
    
    if (y < (diagonal_y - mech_gap)):
        e.region = 'solid'
    elif diagonal_y - mech_gap <= y < diagonal_y - solid_gap:
        e.region = 'mech'
    else:
        e.region = 'void'

bottom_nodes = []
top_nodes = []

for i, n in enumerate(mesh.nodes):
    x, y, z = n
    
    if z <= depth / 2:
        diagonal_y = z * y_slope  
    else:
        diagonal_y = (depth - z) * y_slope  

    if y < diagonal_y - mech_gap:
        bottom_nodes.append(i)
    else:
        top_nodes.append(i)

mesh.bc.append(('bottom_nodes', bottom_nodes))
mesh.bc.append(('top_nodes', top_nodes))

f = '3dhanger_' + str(args.res) +'.mesh'
write_ansys_mesh(mesh, f)
print('Mesh file created:', f)

