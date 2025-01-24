# Structural-Optimisation
STSTOP Project - Hanger

### Command to run the files:

step 1: run the mesh file to generate the mesh for the simulation 

$ python 3dhanger.py --res <the resolution of your choice eg. 10> 10 

This creates a .mesh file (here i´ve named it as 3dhanger.mesh)

then once the mesh file is created to run the openCFS for simulation:

$ cfs -t 4 -m 3dhanger.mesh 3dhanger

### Running this will generate the following files which can then be analysed for insights.
-> 3dhanger.cfs (OpenCFS output file which can be viewed in Paraview)
-> 3dhanger.density.xml
-> 3dhanger.plot.dat