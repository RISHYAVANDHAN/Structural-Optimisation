from mesh_tool import *
import argparse

parser = argparse.ArgumentParser(description="generate a basic mesh. bulk2d/3d is unit square/cube by default. Further default geometries are cantilever 3x2(x1) and mbb2d (1x0.5) ")
parser.add_argument("--res", help="elements in x-direction", type=int, required = True )
args = parser.parse_args()

# Dimensions of the box (m)
width = 1
height = 5
depth = 10

# Resolution of the mesh
nx = args.res  # Higher resolution for smooth transitions
ny = int((height / width) * nx)
nz = int((depth / width) * nx)
mesh = create_3d_mesh(nx, ny, nz, width, height, depth)

# Define the slope (diagonal lines extend symmetrically from both sides)
y_slope = height / (depth / 2) + 0.1 * width  # Slope defining the diagonal
threshold1 = 0.025 * height  # Thickness for solid region
threshold2 = 0.3 * height  # Thickness for mech region
#top_limit_x = 0.3 * width
#top_limit_y = 1.1 * height

# Assign regions to elements based on the symmetric upward diagonal
for e in mesh.elements:
    x, y, z = mesh.calc_barycenter(e)
    
    # Calculate the y-position of the diagonals for the upward slope
    if z <= depth / 2:
        diagonal_y = z * y_slope  # Left slope rises toward the center
    else:
        diagonal_y = (depth - z) * y_slope  # Right slope rises toward the center

    # Apply the top limit to the diagonal
    """
    if diagonal_y > top_limit_y:
        diagonal_y = top_limit_y
        """
    if (y < (diagonal_y - threshold2)):
        e.region = 'solid'
    elif diagonal_y - threshold2 <= y < diagonal_y - threshold1:
        e.region = 'mech'
    else:
        e.region = 'void'

# Define node sets for boundary conditions
bottom_nodes = []
top_nodes = []

for i, n in enumerate(mesh.nodes):
    x, y, z = n
    
    # Calculate the y-position of the diagonals for the upward slope
    if z <= depth / 2:
        diagonal_y = z * y_slope  # Left slope rises toward the center
    else:
        diagonal_y = (depth - z) * y_slope  # Right slope rises toward the center

    # Apply the top limit to the diagonal
    """
    if diagonal_y > top_limit_y:
        diagonal_y = top_limit_y
    """

    if y < diagonal_y - threshold2:
        bottom_nodes.append(i)
    else:
        top_nodes.append(i)

# Add boundary conditions to the mesh
mesh.bc.append(('bottom_nodes', bottom_nodes))
mesh.bc.append(('top_nodes', top_nodes))
# Write the mesh for OpenCFS
f = '3dhanger.mesh'
write_ansys_mesh(mesh, f)
print('Mesh file created:', f)

# cfs -m mesh3dmt.mesh -p mech3d.xml -g mountm
