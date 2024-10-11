# Uranium Fission Decay Simulator
A Python-based graphical simulation tool that visualizes uranium fission decay. In this simulation, you can specify the number and layout of uranium atoms, and initiate a neutron chain reaction to observe fission decay. Customize the arrangement of uranium atoms with adjustable shapes, spacing, and radius, while the simulation tracks and displays the number of active neutrons and collisions.

## Features
- Layout Customization: Choose between random, grid, or circular layouts for uranium atoms. Control the grid spacing or circle radius using sliders for enhanced customization.
- Dynamic Neutron Tracking: View the number of active neutrons and total collisions in real-time as the simulation progresses.
- Modern GUI: A clean and user-friendly interface with adjustable controls and live data display, built with tkinter and ttk styling.
## Layout Options
1. Random: Uranium atoms are scattered randomly across the canvas.
2. Grid: Atoms are placed in a grid layout, with adjustable spacing.
3. Circle: Atoms are arranged in a circular pattern, with a configurable radius.
## Requirements
- Python 3.x
- tkinter (included with Python standard library)
## Setup and Running Instructions
1. Clone the repository or download the source code:

Copy code:
```
git clone <repository-url>
cd uranium-fission-simulator
```
2. Set up a virtual environment to isolate dependencies:

Copy code:
```
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```
3. Run the simulator:

Copy code:
```
python fission_simulator.py
```
## Note
The simulator uses the standard tkinter library, which comes pre-installed with Python. No additional packages are required.