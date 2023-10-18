# Performance Simulation of Thermoelectric Materials
Thermoelectric materials are able to convert a temperature gradient into electrical energy, or vice-versa. 
It has been reported that the majority of primary energy is wasted as heat. So, the development of thermoelectric devices is essential
to utilize this waste heat and convert it into useful electric power. To continue this research and to direct it towards the realization
of novel thermoelectric materials, simulations that, based on the characteristics of the material, are able to compute the
thermoelectric quantities of such materials are of crucial importance. In particular, the proposed
simulation is focused on 2D materials and, taking their band structure as a starting point, is
able to calculate the Seebeck coefficient $S$, the electric conductivity $\sigma$, the thermal electronic
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
git clone https://github.com/ViolaFerretti/Thermoelectric_Quantities_Simulation.git

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
git clone https://github.com/ViolaFerretti/Thermoelectric_Quantities_Simulation.git

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
# Thermoelectric quantities simulation
## Model selection
### Single-parabolic-band model
The single parabolic band model assumes that only one band participates in the charge transport. This assumption can be justied in materials with relatively large band gaps (with respect to the targeted operational temperature range). SPB modeling has been employed successfully
in many material systems like $Mg_2(Si,Sn)$, $ZnSb$, $Bi_2Te_3$ and $PbTe$. A single band is, of course,
not enough to capture the complete picture of the material when more than one majority carrier
band and/or minority carrier bands are contributing substantially to charge transport. 
However, in the case of a highly doped sample single-parabolic-band model is a correct description over the entire
temperature range.

To apply this model, write "SBMP" (the first three letter distinguish between Single-Band Model and Double-Band Model, and the last one selects the approximation, being either Parabolic or of Dirac type) in the first window of the graphic interface. 

### Double-parabolic-band model
The single-band model is not sufficient to describe moderately or lightly doped materials, for
which a double-band model is required, being the simplest and, in most cases, sufficient improvement. A very promising class of materials, is that of members of $Mg_2X$ (with $X = Si$, $Ge$, $Sn$)
and their solid solutions, which can be correctly described by the double-parabolic-band model.

To apply this model, write "DBMP" in the first window of the graphic interface. 

### Double-Dirac-band model
A lot of research efforts and grants have especially been invested on the 2D materials whose electronic structure can be modeled by the Dirac Hamiltonian, or the so-called 2D Dirac materials.
Dirac matter is any material where the low-energy excitation spectrum can be described by the
Dirac equation ($E \propto k$) rather than the more usual quadratic dispersion ($E \propto k^2$
), considered
in the two previous models. The examples of 2D Dirac materials include graphene, silicene,
germanene, transition metal dichalcogenides (TMDs), and hexagonal boron nitride. Some of
them possess excellent electronic and thermal properties, and some recent findings may indicate
the possibilities of 2D Dirac materials as good thermoelectrics.

To apply this model, write "DBMD" in the first window of the graphic interface. 

## First part: energy gap and chemical potential
## Second part: the role of lattice conductivity
