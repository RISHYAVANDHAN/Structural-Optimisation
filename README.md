# Structural-Optimisation

STSTOP Project - Hanger

## Running the Project

### Command to run the files:

```bash
# Generate mesh files with different resolutions
python 3dhanger.py --res <10,50,100>
```

Run the command with different values separately to generate three mesh files of different resolutions.

```bash
# Run the resolution script
python 3dhanger_run_res.py
```

**Important:** Make sure you run these commands in CMD and not PowerShell, as OpenCFS is not supported in PowerShell.

## Installation Guide

### Installing OpenCFS

#### Windows

1. Download the OpenCFS software from the official website
2. Install to the root of your user directory: `C:\Users\<me>\openCFS`
3. Add the following environment variables:
   - `PYTHONPATH` with value `C:\Users\<me>\openCFS\share\python`
   - `CFS` with value `C:\Users\<me>\openCFS\share\python`
   - `CFS_QUIET` with value `1`
4. Add `C:\Users\<me>\bin` to your PATH
5. Create a directory `bin` in your user home and add the .bat files from "Windows .bat files"
6. Install Python 3.12 from https://www.python.org/downloads/ (Note: This specific version works better than Anaconda)
7. Ensure Python is in your PATH by testing in cmd: `python --version`
8. Install required packages:
   ```bash
   pip install numpy matplotlib h5py lxml Pillow scipy vtk
   ```
   (Note: scipy and vtk are not critical)

#### Testing the Installation

- Test Python: Run `create_mesh --res 20 --type bulk2d` in cmd
- Test OpenCFS: Run `cfs --version` in cmd

#### macOS

If you encounter an error during installation:
1. Go to System Settings → Privacy and Security
2. Scroll down to the "Security" heading and click "Open Anyway" to override Apple's security block

Installation steps:
1. Install Homebrew from https://brew.sh/
2. Unpack OpenCFS to `/Users/<ME>/openCFS`
3. Edit the hidden `.zshrc` file and add the following lines:
   ```bash
   export PATH=$PATH:$HOME/openCFS/bin:$HOME/openCFS/share/python
   export PYTHONPATH=$PYTHONPATH:$HOME/openCFS/share/python
   export CFS_QUIET=1
   ```
4. Install the required Python packages as listed in the Windows section

### Installing Paraview

Download and install the latest version of Paraview from https://www.paraview.org/download/

## Running CFS

### Command Line Options

Get the available options via `cfs --help`. You are encouraged to experiment with these options.

Example commands:
- Basic simulation: `cfs -m cantilever2d_20.mesh mech2d_cholmod`
  - This looks for `mech2d_cholmod.xml` as the problem file
  - Output files will start with `mech2d_cholmod`

- To keep result files for comparison: `cfs -m cantilever2d_20.mesh -p mech2d_cholmod.xml problem`
  - Output files will start with `problem`

- To visualize a mesh file: `cfs -g -m cantilever2d_20.mesh mech2d_cholmod`
  - Generates a `.cfs` output file with mesh visualization
  - Skips the simulation (the settings in the `<pde>` section of the problem xml file are not read)

## Saving Disk Space

CFS++ may generate large output files, especially when performing optimization and parameter studies. To save disk space:

1. In the simulation part in `<storeResults>`:
   - Have no region output in `<nodeResult>` and `<elemResult>`
2. Remove the HDF5 output writer
3. In the optimization part, use a large stride for `<commit>`, e.g., 9999
