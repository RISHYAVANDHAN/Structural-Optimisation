# Structural-Optimisation
STSTOP Project - Hanger

### Command to run the files:

$ python 3dhanger_run_res.py

This is enough to run the file, make sure you run in CMD and not Powershell, OpenCFS is not supported in Powershell.


## Install CFS

### Windows

Go to OpenCFS website to download the software, then
We assume to install to the root of the user's directory

C:\Users\<me>\openCFS

Then add to in your users environment variables

PYTHONPATH with the value C:\Users\<me>\openCFS\share\python
CFS with value C:\Users\<me>\openCFS\share\python
CFS_QUIET with the value 1

Add to your PATH the value  C:\Users\<me>\bin
Create a directory binin your user home and add the .bat files from "Windows .bat files"
We need Python and later it needs to be exactly Python 3.12 from https://www.python.org/downloads/ so better install it right now. 
This python works better than Anaconda, make sure it is in your path.

Test in cmd by calling python if it is the proper version.

Also in cmd call pip install numpy matplotlib h5py lxml Pillow scipy vtk (scipy and vtk are not that important)
A test for python is to call in cmd the command create_mesh --res 20 --type bulk2d
A test for cfs is to call in cmd the command cfs --version

### macOS

If there is an error which does not allow mac to install the software then follow the steps below;
1. Go to System Settings -> Privact and Security
2. Scroll down till the heading Security -> open anyways (it is a prompt which has a button to override apple security block on unauthorized application or software installation)

You need homebre installed from https://brew.sh/
Unpack openCFS, e.g. to /Users/<ME>/openCFS
Edit the hidden file .zshrc and add the following lines (where $HOME has automatically the value /Users/<ME>

export PATH=$PATH:$HOME/openCFS/bin:$HOME/openCFS/share/python
export PYTHONPATH=$PYTHONPATH:$HOME/openCFS/share/python
export CFS_QUIET=1

Make sure you have the proper python packages installed the "tests" from above work.

### Paraview
Install a latest Paraview from https://www.paraview.org/download/

### Run CFS

### Command Line Options

Get the availble options via cfs --help. You are encouraged to experiments with the options.

An example for calling cfs is cfs -m cantilever2d_20.mesh mech2d_cholmod. The name of the simulation is mech2d_cholmod and the generated output files will start with mech2d_cholmod. As no input xml problem file is given, cfs looks for mech2d_cholmod.xml.

If you want to keep the result files, (e.g. the .info.xml files) to compare them, use the following schema:

cfs -m cantilever2d_20.mesh -p mech2d_cholmod.xml problem. Now all generated output files start with problem.

An easy way to visualize a mesh file, e.g. what are the names of named nodes and where are they, ... is by the following option:
cfs -g -m cantilever2d_20.mesh mech2d_cholmod
A .cfs output file is generated but the simulation is omitted, the file content is the mesh. This way the settings in the <pde> section of the problem xml file are not read. 

##Save Disk Space
CFS++ may generate large output files, especially when performing optimization and doing parameter studies. The following steps save a lot output.
In the simulation part in <storeResults> have in <nodeResult> and <elemResult> no region output
Remove the hdf5 output writer
In the optimization part use for <commit> a large stride, e.g. 9999
