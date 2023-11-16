# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:08:19 2023

@author: viola
"""

# import necessary modules
from DBM_Dirac import *
from DBM_Parabolic import *
from SBM_Parabolic import *
from plots import * 

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import sys

# define functions to generate GUI

def make_window0():
    """
    Make the initial window of the GUI
    in which the user can enter the configuration file
    
    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    layout = [[sg.Text('Configuration File Path:'), sg.Input(key='-FILE-'), sg.FileBrowse()],
              [sg.Button('Load Configuration'),sg.Button('Next >')]]
    
    window = sg.Window("Thermoelectric materials performance - Configuration",
                       layout,
                       location=(0, 0),
                       finalize=True,
                       element_justification="center")
    
    return window 

def make_window1(): # model selection
    """
    Make the first window of the GUI, where the model is selected.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    layout = [[sg.Text("Thermoelectric materials performance")],
              # select model (DBMD,DBMP, SBMP)
              [sg.Text('Model to apply'), sg.InputText(key='-IN_Model-')], 
              [sg.Button('Next >')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    return window

def make_window2(): # DBMD, dependency on the energy gap and the chemical potential
    """
    Make the window of the GUI to insert parameters for Double-Dirac-Band Model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the energy gap and the chemical potential - Double-Dirac-Band Model")],
              # set energy gap parameters
              [sg.Text('Minimum energy gap'), sg.InputText(key='-IN_delta_min-')], 
              [sg.Text('Maximum energy gap'), sg.InputText(key='-IN_delta_max-')],
              [sg.Text('Energy gap step'), sg.InputText(key='-IN_delta_step-')],
              # set chemical potential parameters
              [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], 
              [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
              [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
              # set thermal lattice conductivity
              [sg.Text('Lattice thermal conductivity'), sg.InputText(key='-IN_rk-')],
              # space for 2D plots
              [sg.Canvas(key='-FIG0-')],
              [sg.Button('< Choose Model'),sg.Button('Show 2D Plots'), sg.Button('Save'), sg.Button('Show 3D Plots >'),sg.Button('Second Part >')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window
    

def make_window2_3d(): # DBMD, 3D plot
    """
    Make the window of the GUI to visualize 3D plots of Double-Dirac-band model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the energy gap and the chemical potential - Double-Dirac-Band Model")],
              [sg.Text('3D plots')],
              # spaces for 3D plots
              [sg.Canvas(key='-FIG1-'),sg.Canvas(key='-FIG2-')],
              [sg.Canvas(key='-FIG3-'),sg.Canvas(key='-FIG4-')],
              [sg.Button('< Prev'),sg.Button('Show 3D Plots'),sg.Button('Save'),sg.Button('Seond Part >')],
              ]
    
    window = sg.Window('3D plots', 
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window 


def make_window3(): # DBMP, dependency on the energy gap and the chemical potential
    """
    Make the window of the GUI to insert parameters for Double-Parabolic-Band Model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the energy gap and the chemical potential - Double-Parabolic-Band Model")],
              # set energy gap parameters
              [sg.Text('Minimum energy gap'), sg.InputText(key='-IN_delta_min-')], 
              [sg.Text('Maximum energy gap'), sg.InputText(key='-IN_delta_max-')],
              [sg.Text('Energy gap step'), sg.InputText(key='-IN_delta_step-')],
              # set chemical potential parameters
              [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], 
              [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
              [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
              # set thermal lattice conductivity
              [sg.Text('Lattice thermal conductivity'), sg.InputText(key='-IN_rk-')],
              # space for 2D plots
              [sg.Canvas(key='-FIG0-')],
              [sg.Button('< Choose Model'),sg.Button('Show 2D Plots'), sg.Button('Save'), sg.Button('Show 3D Plots >'),sg.Button('Second Part >')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window


def make_window3_3d(): # DBMP, 3D plot
    """
    Make the window of the GUI to visualize 3D plots of Double-Parabolic-band model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created
            
    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the energy gap and the chemical potential - Double-Parabolic-Band Model")],
              [sg.Text('3D plots')],
              # spaces for 3D plots
              [sg.Canvas(key='-FIG1-'),sg.Canvas(key='-FIG2-')],
              [sg.Canvas(key='-FIG3-'),sg.Canvas(key='-FIG4-')],
              [sg.Button('< Prev'),sg.Button('Show 3D Plots'), sg.Button('Save'),sg.Button('Second Part >')],
              ]
    
    window = sg.Window('3D plots of the free energy in the different spaces',
                     layout,location=(0, 0),
                     finalize=True,
                     element_justification="center")
    return window 


def make_window4(): # SBMP, dependency on the energy gap and the chemical potential
    """
    Make the window of the GUI to insert parameters for Single-Parabolic-Band Model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the energy gap and the chemical potential - Single-Parabolic-Band Model")],
              # set chemical potential parameters
              [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], 
              [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
              [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
              # set thermal lattice conductivity
              [sg.Text('Lattice thermal conductivity'), sg.InputText(key='-IN_rk-')],
              # space for 2D plots
              [sg.Canvas(key='-FIG0-')],
              [sg.Button('< Choose Model'),sg.Button('Show Plots'), sg.Button('Save'),sg.Button('Second Part >')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    return window 


def make_window5(): # DBMD, dependency on the thermal lattice conductivity
    """
    Make the window of the GUI to insert r_k parameter for Double-Dirac-Band Model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the phonon thermal conductivity - Double-Dirac-Band Model")],
              # set thermal lattice conductivity parameters
              [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], 
              [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
              [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],
              # space for 3D plot
              [sg.Canvas(key='-FIG0-')],
              [sg.Button('< Choose Model'),sg.Button('Show Plot'), sg.Button('Save')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window


def make_window6(): # DBMP, dependency on the thermal lattice conductivity
    """
    Make the window of the GUI to insert r_k parameter for Double-Parabolic-Band Model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the phonon thermal conductivity - Double-Parabolic-Band Model")],
              # set thermal lattice conductivity parameters
              [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], 
              [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
              [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],
              # space for 3D plot
              [sg.Canvas(key='-FIG0-')],
              [sg.Button('< Choose Model'),sg.Button('Show Plot'), sg.Button('Save')],
              ]
    
    window = sg.Window("Thermoelectric materials performance", 
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window 


def make_window7(): # SBMP, dependency on the thermal lattice conductivity
    """
    Make the window of the GUI to insert r_k parameter for Single-Parabolic-Band Model.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created

    """
    
    layout = [[sg.Text("Thermoelectric materials performance: dependency on the phonon thermal conductivity - Single-Parabolic-Band Model")],
              # set thermal lattice conductivity parameters
              [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], 
              [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
              [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],
              # space for 3D plot
              [sg.Canvas(key='-FIG0-')],
              [sg.Button('< Choose Model'), sg.Button('Show Plot'), sg.Button('Save')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window 


def make_window8(): 
    """
    Make the window of the GUI to save data.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created
            
    """
    
    layout = [[sg.Text('Save data')],
              # indicate where to save the data
              [sg.Text('Path of the directory for the txt data file:'), sg.InputText(key='-IN_txt_path-')],
              [sg.Text('Name of the txt file:'), sg.InputText(key='-IN_txt_model'), sg.InputText(key='-IN_txt_part'), sg.InputText(key='-IN_txt_file-')],
              [sg.Button('Save Data'), sg.Button('Done')],
              ]
    
    window = sg.Window('Thermoelectric materials performance - Save data', 
                     layout,
                     location=(0, 0),
                     finalize=True, 
                     element_justification="center")
    
    return window

# define functions to manage operations in GUI windows

def load_configuration(file_path):
    """
    Function that loads the configuration file from a specific path given by the user

    Parameters
    ----------
    file_path : TYPE str
                DESCRIPTION. Path of the configuration file

    Returns
    -------
    Names : TYPE list of str
            DESCRIPTION. List of the names of the values
    Values : TYPE list of floats
             DESCRIPTION. List of the values
    """

    Names = []
    Values = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Ignoring the lines in the configuration file starting with %
                if not line.startswith("%"):
                    values = line.strip().split(",")
                    if len(values) >= 2:
                        Names.append(values[0].strip())
                        Values.append(float(values[1].strip()))

        return Names, Values

    except FileNotFoundError:
        print('File not found:', file_path)
        return [], []      

def user_operations(current_window):
    """
    Manages standard user operations: go back to first window to choose model, save data or close.
    
    Parameters
    ----------
    window : TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
             DESCRIPTION. current window where the user choice are made
       
    """
    
    if event == '< Choose Model': # if user clicks on button '< Choose Model',
        current_window.close() # close current window
        window1.un_hide() # and go back to model selection
   
    elif event == 'Save': # if user clicks on button 'Save',
        current_window.hide() # hide current window
        global window8
        window8 = make_window8() # and open window to save data
        
    
    elif event == sg.WIN_CLOSED: # if user closes window, close the programm
        current_window.close()
        sys.exit()
    
    else:
        pass

def get_inputs_first_part(window): 
    
    """
    Reads the inputs from specific window, for the first part.

    Parameters
    ----------
    window : TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
             DESCRIPTION. window where the inputs to read have been written by the user
    
    Returns
    -------
    TYPE list
    DESCRIPTION. list containing the arrays for the energy gap and the chemical potential and the value of rk
            
    """
        
    inputs = {}
    for key in values:
        if key != '-FIG0-':
            inputs[key] = float(values[key])
    if window == window2 or window == window3: # for double-band models
        delta_min = inputs['-IN_delta_min-'] # minimum energy gap value
        delta_max = inputs['-IN_delta_max-'] # maximum energy gap value
        delta_st = inputs['-IN_delta_step-'] # energy gap step
        delta=np.arange(delta_min, delta_max, delta_st) #create array for energy gap
    else: # for single-band model
        delta = None
    
    eta_min = inputs['-IN_eta_min-'] # minimum chemical potential value
    eta_max = inputs['-IN_eta_max-'] # maximum chemical potential value
    eta_st = inputs['-IN_eta_step-'] # chemical potential step
    eta=np.arange(eta_min, eta_max, eta_st) #create array for chemical potential
    rk = inputs['-IN_rk-'] # thermal lattice conductivity (fixed)   
    
    return [delta, eta, rk] 

def get_inputs_second_part():
    
    """
    Reads the inputs from specific window, for the second part.

    Parameters
    ----------
    window : TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
             DESCRIPTION. window where the inputs to read have been written by the user
        
    Returns
    -------
    rk : TYPE nd.array
       DESCRIPTION. array for thermal lattice conductivity
            
    """
    
    inputs = {}
    for key in values:
        if key != '-FIG0-':
            inputs[key] = float(values[key])
    rk_min = inputs['-IN_rk_min-'] # minimum thermal lattice conductivity value
    rk_max = inputs['-IN_rk_max-'] # maximum thermal lattice conductivity value
    rk_st = inputs['-IN_rk_step-'] # energy thermal lattice conductivity
    rk = np.arange(rk_min, rk_max, rk_st) # create array for thermal lattice consuctivity
    
    return rk

def draw_figure(canvas,
                figure):
    """
    Function that draws the wanted figure in the empty canvas of the window.

    Parameters
    ----------
    canvas: TYPE PySimpleGUI.Canvas(canvas, background_color, size)
            DESCRIPTION. drawable panel on the surface of the PySimpleGUI application window
    figure: TYPE matplotlib.figure.Figure()
            DESCRIPTION. Figure we want to draw on the panel 

    Returns
    -------
    figure_canvas_agg: TYPE FigureCanvasTkAgg(figure, canvas)
                       DESCRIPTION. Figure drawn on the canvas

    """
    figure_canvas_agg = FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    
    return figure_canvas_agg


def delete_fig_agg(fig_agg):
    """
    Function to delete the figure drawn on the canvas.

    Parameters
    ----------
    fig_agg: TYPE FigureCanvasTkAgg(figure, canvas)
             DESCRIPTION. Figure drawn on the canvas

    Returns
    -------
    None.

    """
    fig_agg.get_tk_widget().forget()
    plt.close('all')

def plot_clear_draw(plot, params, figure_canvas, figure):
    """
    Creates plot, clears canvas to plot it.
    
    Parameters
    ----------
    plot : TYPE function to create plot (from plots.py)
           DESCRIPTION. figure containing the plot
    params : TYPE parameters useful for the plotting function
             DESCRIPTION. list of parameters (physical quantities to plot and labels to put on the axis)
    figure_canvas : TYPE PySimpleGUI.Canvas(canvas, background_color, size)
                    DESCRIPTION. drawable panel on the surface of the PySimpleGUI application window to clear  
    figure : TYPE matplotlib.figure.Figure()
             DESCRIPTION. Figure we want to draw on the panel 
            
    """
    
    if plot == plot_anim_3d: # for 3D plots 
        graph = plot(params[0], params[1], params[2], params[3], params[4], params[5], params[6]) # use associated function from plots.py (depending on 7 parameters)
    elif plot == complete_2d_plot: # 2D plots
        graph = plot(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7]) # use associated function from plots.py (depending on 8 parameters)
    if figure_canvas is not None: # clear space and draw plot
        delete_fig_agg(figure_canvas)
    figure_canvas = draw_figure(window[figure].TKCanvas, graph) 
    
def write_txt(model, part, inputs, outputs):
    """
    Saves data associated model and part of interest.

    Parameters
    ----------
    model : TYPE string
            DESCRIPTION. string indicating the used model ('DBMD', 'DBMP', 'SBMP')
    part : TYPE string
           DESCRIPTION. string indicating the part of the study ('1', '2')
    inputs : TYPE list
             DESCRIPTION. list containing input data (energy gap, chemical potential, thermal lattice conductivity)  
    outputs : TYPE list
             DESCRIPTION. list containing output data (thermoelectric quantities)
            
    """
    
    with open(path_to_file, 'w') as f:
        if (part == '1' and (model == 'DBMD' or model == 'DBMP')) or (part == '2'): # inputs = [delta, eta, rk] 
            if part == '1' and (model == 'DBMD' or model == 'DBMP'):
                f.write('delta' + ',' + 'eta' + ',' + 'rk' + ',' + 'sigma' + ',' + 'S' + ',' + 'k_e' + ',' + 'ZT' + '\n')
                inputs[-1] = [inputs[-1]]*np.ones((int(inputs[0].size/inputs[0][0].size), inputs[0][0].size))
            elif part == '2' and (model == 'DBMD' or model == 'DBMP'):
                f.write('delta' + ',' + 'rk' + ',' + 'ZT' + '\n')
            elif part == '2' and model == 'SBMP':
                f.write('eta' + ',' + 'rk' + ',' + 'ZT' + '\n')
            for i in range(len(inputs)): # go through input data
                for j in range(inputs[i][0].size): # go through columns
                    for k in range(int(inputs[i].size/inputs[i][0].size)): # go through rows
                        for i in range(len(inputs)): # write an input data at a time
                            f.write(str(inputs[i][k][j]) + ',')
                        for h in range(len(outputs)):
                            f.write(str(outputs[h][k][j]) + ',')
                        f.write('\n')
        elif part == '1' and model == 'SBMP': # inputs = [eta, rk]
            f.write('eta' + ',' + 'rk' + ',' + 'sigma' + ',' + 'S' + ',' + 'k_e' + ',' + 'ZT' + '\n')
            inputs[-1] = [inputs[-1]]*np.ones(int(inputs[0].size))
            for i in range(len(inputs)): # go through input data
                for j in range(inputs[i].size): # go through array elements
                    for i in range(len(inputs)): # write an input data at a time 
                        f.write(str(inputs[i][j]) + ',')
                    for h in range(len(outputs)): # write an output data at a time
                        f.write(str(outputs[h][j]) + ',')
                    f.write('\n')
        f.close()
        print('Data saved!') 
        
def open_previous_window(previous_window):
    """
    Reopens previous window after the user has save the data.

    Parameters
    ----------
    previous_window : TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
                      DESCRIPTION. previous window, to reopen
            
    """
    
    window8.close() # close current window
    previous_window.un_hide() # reopen previous window
            
# make the first window and set the others windows to none 
window0, window1, window2, window2_3d, window3, window3_3d, window4, window5, window6, window7, window8 = make_window0(), None, None, None, None, None, None, None, None, None, None
# set the figure drawings to None in order to be able to update them each time 
figure_canvas_agg0, figure_canvas_agg1, figure_canvas_agg2, figure_canvas_agg3, figure_canvas_agg4 = None, None, None, None, None
# set the color bar to None in order to be able to update it later
cbar = None


while True:
    
    # read all the events, windows and values entered on the windows
    window, event, values = sg.read_all_windows()
    
    if window==window0:
        if event== sg.WIN_CLOSED : # if user closes window close the programm
            break
        
        elif event == 'Load Configuration':
            
            file_path = values['-FILE-']
            names, load_values=load_configuration(file_path)
            #assigning the values from the configuration file
            #1st part
            delta_1 = np.arange(load_values[0], load_values[1], load_values[2])
            eta_1 = np.arange(load_values[3], load_values[4], load_values[5])
            rk_1 = load_values[6]
            #2nd part
            rk_2 = np.arange(load_values[7], load_values[8], load_values[9])
            print('Configuration done!')
            
        elif event == 'Next >':
            
            window0.hide()
            window1 = make_window1()
    
    if window == window1:
              
        user_operations(window1)
        if event == 'Next >': # if user clicks on the button 'Next >'
            model = (values['-IN_Model-'])
            window1.hide()
            if model == 'DBMD' : # if DBMD is selected,   
                window2 = make_window2() # and open associated window
            elif model == 'DBMP': # if DBMP is selected,  
                window3 = make_window3() # and open associated window
            elif model == 'SBMP': # if SBMP is selected,  
                window4 = make_window4() # and open associated window        
# DBMD               
    if window == window2:
        user_operations(window2)
        
        if event == 'Second Part >': # if user clicks on button 'Next >',  
            window2.hide() # skip/end the first part
            window5 = make_window5() # and go to second part
        else:
            # take input data and compute thermoelectric quantities as outputs
            if all(item is None for item in [delta_1, eta_1, rk_1]): # if load_data file not used in the configuration, get input data
                delta_1, eta_1, rk_1 = get_inputs_first_part(window2)[0], get_inputs_first_part(window2)[1], get_inputs_first_part(window2)[2]
            delta, eta = np.meshgrid(delta_1, eta_1)
            S = create_matrix(S_DBMD, [delta, eta], None)
            sigma = create_matrix(sigma_DBMD, [delta, eta], None)
            ke = create_matrix(ke_DBMD, [delta, eta], None)
            ZT = create_matrix(ZT_DBMD, [delta, eta], rk_1)
            inputs = [delta, eta, rk_1]
            outputs = [sigma, S, ke, ZT]
            if event == 'Show 2D Plots': # if user clicks on  button 'Show 2D Plots', show plot
                plot_clear_draw(complete_2d_plot, [S, sigma, ke, ZT, delta, eta, rk_1, 'TE quantities of 2D Dirac double-band material'], figure_canvas_agg0, '-FIG0-')    
            if event == 'Show 3D Plots >': #if user clicks on button 'Show 3D Plots >',
                window2.hide() # hide current window
                window2_3d = make_window2_3d() # open window to show 3D plot
     
    if window == window2_3d:
        
        user_operations(window2_3d)
            
        if event == '< Prev':  # if user clicks on button '< Prev'
            window2_3d.close() # close current window
            window2.un_hide() # and re-open the previous window
        if event == 'Second Part >': # if user clicks on button 'Next >', 
            window2_3d.hide() # hide current window
            window5 = make_window5() # and open next one to start the second part
        if event == 'Show 3D Plots': # if user wants to visualize 3D plots
            plot_clear_draw(plot_anim_3d, [delta, eta, sigma, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$)'], figure_canvas_agg1, '-FIG1-')
            plot_clear_draw(plot_anim_3d, [delta, eta, S, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$)'], figure_canvas_agg2, '-FIG2-')
            plot_clear_draw(plot_anim_3d, [delta, eta, ke, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)','$\kappa_{e}$($\eta$,$\Delta$)'], figure_canvas_agg2, '-FIG3-')
            plot_clear_draw(plot_anim_3d, [delta, eta, ZT, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)','ZT($\eta$,$\Delta$)'], figure_canvas_agg4, '-FIG4-')
            
    if window == window5:
        
        user_operations(window5)
        # take input data and compute figure of merit as output
        if rk_2 is None: # if load_data file not used in the configuration, get input data
            rk_2 = get_inputs_second_part()
        delta, eta, rk = np.meshgrid(generate_arrays(21)[0], generate_arrays(21)[1], rk_2)
        ZT = create_matrix(ZT_DBMD, [delta, eta, rk], None)
        ZT = find_ZTmax(delta, eta, rk, ZT)
        rk, delta = np.meshgrid(rk_2, generate_arrays(21)[0])    
        inputs = [delta, rk]
        outputs = [ZT]
        if event == 'Show Plot': # if the user wants to visualize data, show plot
            plot_clear_draw(plot_anim_3d, [delta, rk, ZT, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$)'], figure_canvas_agg1, '-FIG0-')

# DBMP   
    if window == window3:
        
        user_operations(window3)
            
        if event == 'Second Part >': # if user clicks on button 'Next >', 
            window3.hide() # skip/end the first part
            window6 = make_window6() # and go to the second part
        else: 
            # take input data and compute thermoelectric quantities as outputs
            if all(item is None for item in [delta_1, eta_1, rk_1]): # if load_data file not used in the configuration, get input data
                delta_1, eta_1, rk_1 = get_inputs_first_part(window3)[0], get_inputs_first_part(window3)[1], get_inputs_first_part(window3)[2]
            delta, eta = np.meshgrid(delta_1, eta_1)
            S = create_matrix(S_DBMP, [delta, eta], None)
            sigma = create_matrix(sigma_DBMP, [delta, eta], None)
            ke = create_matrix(ke_DBMP, [delta, eta], None)
            ZT = create_matrix(ZT_DBMP, [delta, eta], rk_1)
            inputs = [delta, eta, rk_1]
            outputs = [sigma, S, ke, ZT]
            if event == 'Show 2D Plots': #if user clicks on button 'Show 2D plots', show plot
                    plot_clear_draw(complete_2d_plot, [S, sigma, ke, ZT, delta, eta, rk_1, 'TE quantities of 2D Dirac double-band material'], figure_canvas_agg0, '-FIG0-')
            if event == 'Show 3D Plots >': # if user clicks on button 'Show 3D plots >',
                    window3.hide() # hide current window
                    window3_3d = make_window3_3d() # and open window to show 3D plots
        
    if window == window3_3d:
        
            user_operations(window3_3d)
                
            if event =='Second Part >': # if user clicks on button 'Next >'
                window3_3d.hide() #hide current window
                window6 = make_window6() # and open next one to start the second part
            if event == 'Show 3D Plots': # create and show 3D plots
                plot_clear_draw(plot_anim_3d, [delta, eta, sigma, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$)'], figure_canvas_agg1, '-FIG1-')
                plot_clear_draw(plot_anim_3d, [delta, eta, S, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$)'], figure_canvas_agg2, '-FIG2-')
                plot_clear_draw(plot_anim_3d, [delta, eta, ke, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)','$\kappa_{e}$($\eta$,$\Delta$)'], figure_canvas_agg2, '-FIG3-')
                plot_clear_draw(plot_anim_3d, [delta, eta, ZT, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)','ZT($\eta$,$\Delta$)'], figure_canvas_agg4, '-FIG4-')

    if window == window6:
        
        user_operations(window6)
        # take input data and compute figure of merit as output
        if rk_2 is None: # if load_data file not used in the configuration, get input data
            rk_2 = get_inputs_second_part()
        delta, eta, rk = np.meshgrid(generate_arrays(21)[0], generate_arrays(21)[1], rk_2)
        ZT = create_matrix(ZT_DBMD, [delta, eta, rk], None)
        ZT = find_ZTmax(delta, eta, rk, ZT)
        rk, delta = np.meshgrid(rk_2, generate_arrays(51)[0])    
        inputs = [delta, rk]
        outputs = [ZT]
        if event == 'Show Plot': # if the user wants to visualize data, show plot
            plot_clear_draw(plot_anim_3d, [delta, rk, ZT, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$)'], figure_canvas_agg1, '-FIG0-')
                                  
# SBMP                        
    if window == window4:
        
        user_operations(window4) 
        delta = None    
        
        if event =='Second Part >': # if user clicks on button 'Next >',
            window4.hide() # skip/end the first part
            window7 = make_window7() # and go to second part
        else:
            # take input data and compute thermoelectric quantities as outputs
            if all(item is None for item in [eta_1, rk_1]): # if load_data file not used in the configuration, get input data
                eta_1, rk_1 = get_inputs_first_part(window4)[1], get_inputs_first_part(window4)[2]
            eta, rk = np.meshgrid(eta_1, rk_1)
            S = create_matrix(S_SBMP, [eta], None)
            sigma = create_matrix(sigma_SBMP, [eta], None)
            ke = create_matrix(ke_SBMP, [eta], None)
            ZT = create_matrix(ZT_SBMP, [eta], rk)
            inputs = [eta, rk]
            outputs = [sigma, S, ke, ZT]
            if event =='Show Plots': # if user clicks on button 'Show Plots', show plot
                plot_clear_draw(complete_2d_plot, [S, sigma, ke, ZT, delta, eta, rk, 'TE quantities of 2D single-parabolic-band material'], figure_canvas_agg0, '-FIG0-')
                      
    if window == window7:
        
        user_operations(window7)
        # take input data and compute figure of merit as output
        if rk_2 is None: # if load_data file not used in the configuration, get input data
            rk_2 = get_inputs_second_part()
        eta, rk = np.meshgrid(generate_arrays(51)[1], rk_2)
        ZT = create_matrix(ZT_SBMP, [eta, rk], None)
        inputs = [eta, rk]
        outputs = [ZT]
        if event == 'Show Plot': # if the user wants to visualize data, show plot
            plot_clear_draw(plot_anim_3d, [eta, rk, ZT, '$\eta$', '$\kappa_L$', 'ZT($\eta$,$\kappa_l$)', '3D plot: 2D single-parabolic-band material'], figure_canvas_agg1, '-FIG0-')
            
# SAVE DATA  
    if window == window8:

        if event == sg.WIN_CLOSED: # if user closes window,
            window8.close() # close the program
            break
        
        # set parameters to values entered by the user
        path_txt = values['-IN_txt_path-'] # path to save the .txt file
        title_model = values['-IN_txt_model'] # first part of the title: model (DBMD, DBMP, SBMP)
        title_part = values['-IN_txt_part'] # second part of the title: part of the study (1 for 1st part, 2 for 2nd part)
        title_txt = values['-IN_txt_file-'] # third part of the title: additional specification desired by the user
        if event == 'Save Data': # if user wants to save data
            path_to_file = path_txt + title_model + title_part + title_txt + '.txt' # create path to new txt file
            write_txt(title_model, title_part, inputs, outputs) # write data in new txt file 
        if event == 'Done': # if user clicks on button 'Done', reopen previous window
            if title_model == 'DBMD' and title_part == '1':
                open_previous_window(window2)
            if title_model == 'DBMD' and title_part == '2':
                open_previous_window(window5)
            if title_model == 'DBMP' and title_part == '1':
                open_previous_window(window3)
            if title_model == 'DBMP' and title_part == '2':
                open_previous_window(window6)
            if title_model == 'SBMP' and title_part == '1':
                open_previous_window(window4)
            if title_model == 'SBMP' and title_part == '2':
                open_previous_window(window7)
      
window.close()    
    