# Performance Simulation of Thermoelectric Materials
Thermoelectric materials are able to convert a temperature gradient into electrical energy, or vice-versa. 
It has been reported that the majority of primary energy is wasted as heat. So, the development of thermoelectric devices is essential
to utilize this waste heat and convert it into useful electric power. To continue this research and to direct it towards the realization
of novel thermoelectric materials, simulations that, based on the characteristics of the material, are able to compute the
thermoelectric quantities of such materials are of crucial importance. In particular, the proposed
simulation is focused on 2D materials and, taking their band structure as a starting point, is
able to calculate the Seebeck coefficient $S$, the electric conductivity σ, the thermal electronic
conductivity $\kappa_e$ and the fgure of merit $ZT$, depending on three main parameters: the energy
gap, the chemical potential and on the thermal lattice conductivity.

The simulation can be done based on three different models describing the band structure:
- single-parabolic-band model
- double-parabolic-band model
- double-Dirac-band model

All three models are based on Boltzmann transport theory in the linear response regime in the relaxation-time approximation.

# How to download and the software
## Using Anaconda
### 1. Clone the repository
```
git clone https://github.com/ViolaFerretti/software_and_computing_project.git

```
### 2. Install packages
In the Anaconda Prompt, install the necessary packages in python3: 
- to manage calculations:
```
conda install numpy
conda install scipy
conda install mpmath
conda install pandas
```
- to visualize data
```
conda install matplotlib
```
- to set parameters and perform the simulations
```
conda install -c conda-forge pysimplegui
```
- to test functions:
```
conda install hypothesis
```
### 3. Run the software
Run the software with one of the environments, for example in Spyder.
## Using Windows
### 1. Clone the repository
```
git clone https://github.com/ViolaFerretti/software_and_computing_project.git

```
### 2. Install packages
In the Anaconda Prompt, make sure that you have all the needed packages in python3: 
- to manage calculations:
```
pip install numpy
pip install scipy
pip install matplotlib
pip install mpmath
pip install pandas
```
- to visualize data
```
pip install matplotlib
```
-to set parameters and perform the simulations
```
pip install PySimpleGUI
```
- to test functions:
```
pip install hypothesis
```
### 3. Run the software
```
python3 GUI.py
```
# First part: ZT simulation depending on energy gap and chemical potential
# Second part: ZT simulation depending on energy gap, chemical potential and lattice conductivity
