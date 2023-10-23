# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:08:19 2023

@author: viola
"""

# import necessary modules
from DBM_Dirac import *
from DBM_Parabolic import *
from SBM_Parabolic import *
from plots import plot_anim_3d,subplots_2D_graph,complete_2d_plot,complete_2d_plot_SBM

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg

# define functions to generate GUI
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
              [sg.Button('< Prev'),sg.Button('Show 2D Plots'), sg.Button('Save'), sg.Button('Show 3D Plots>'),sg.Button('Next >')],
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
              [sg.Button('< Prev'),sg.Button('Show 3D Plots'),sg.Button('Save'),sg.Button('Next >')],
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
              [sg.Button('< Prev'),sg.Button('Show 2D Plots'), sg.Button('Save'), sg.Button('Show 3D Plots >'),sg.Button('Next >')],
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
              [sg.Button('< Prev'),sg.Button('Show 3D Plots'), sg.Button('Save'),sg.Button('Next >')],
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
              [sg.Button('< Prev'),sg.Button('Show Plots'), sg.Button('Save'),sg.Button('Next >')],
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
              [sg.Button('< Choose Model'),sg.Button('Show Plot'), sg.Button('Save')],
              ]
    
    window = sg.Window("Thermoelectric materials performance",
                     layout,
                     location=(0, 0),
                     finalize=True,
                     element_justification="center")
    
    return window 


def make_window8(): # save data
    """
    Make the window of the GUI to save data.

    Returns
    -------
    window: TYPE PySimpleGUI.Window(title, layout, location, finalize, element_justification)
            DESCRIPTION. Window created
            
    """
    
    layout = [[sg.Text('Save the data')],
              # indicate where to save the data
              [sg.Text('Path of the directory for the txt data file:'),sg.InputText(key='-IN_txt_path-')],
              [sg.Text('Name of the txt file:'),sg.InputText(key='-IN_txt_model'),sg.InputText(key='-IN_txt_part'),sg.InputText(key='-IN_txt_file-')],
              [sg.Button('Save txt'),sg.Button('Done')],
              ]
    
    window = sg.Window('Thermoelectric materials performance - Save the data', 
                     layout, location=(0, 0),
                     finalize=True, 
                     element_justification="center")
    
    return window


# make the first window and set the others windows to none 
window1, window2, window2_3d, window3, window3_3d, window4, window5, window6, window7, window8 = make_window1(), None, None, None, None, None, None, None, None, None

# set the figure drawings to None in order to be able to update them each time 
figure_canvas_agg0 = None
figure_canvas_agg1 = None
figure_canvas_agg2 = None
figure_canvas_agg3 = None
figure_canvas_agg4 = None

# set the color bar to None in order to be able to update it later
cbar = None

while True:
    
    # read all the events, windows and values entered on the windows
    window, event, values = sg.read_all_windows()
    
    if window == window1:
              
        if event == sg.WIN_CLOSED: # if user closes window,
            window1.close() # close the program
            break
        
        elif event == 'Next >': # if user clicks on the button 'Next >'
            
            model = (values['-IN_Model-'])
                       
            if model == 'DBMD' : # if DBMD is selected,   
                window1.hide() # hide current window
                window2 = make_window2() # and open associated window
            
            elif model == 'DBMP': # if DBMP is selected,  
                window1.hide() # hide current window
                window3 = make_window3() # and open associated window
            
            elif model == 'SBMP': # if SBMP is selected,  
                window1.hide() # hide current window
                window4 = make_window4() # and open associated window        
# DBMD               
    if window == window2:
        
        if event == '< Choose Model': # if user clicks on button '< Choose Model',
            window2.close() # close current window
            window1.un_hide() # and go back to model selection
        
        elif event == 'Next >': # if user clicks on button 'Next >',  
            window2.hide() # skip/end the first part
            window5 = make_window5() # and go to second part
        
        elif event == sg.WIN_CLOSED : # if user closes window, close the programm
            window2.close()
            break
        
        else:
            # set parameters to the values entered by the user
            delta_min = (float(values['-IN_delta_min-'])) # minimum energy gap value
            delta_max = (float(values['-IN_delta_max-'])) # maximum energy gap value
            eta_min = (float(values['-IN_eta_min-'])) # minimum chemical potential value
            eta_max = (float(values['-IN_eta_max-'])) # maximum chemical potential value
            delta_st = (float(values['-IN_delta_step-'])) # energy gap step
            eta_st = (float(values['-IN_eta_step-'])) # chemical potential step
            rk = (float(values['-IN_rk-'])) # thermal lattice conductivity (fixed)
            
            # create arrays of energy gap and chemical potential
            delta=np.arange(delta_min, delta_max, delta_st)
            eta=np.arange(eta_min,eta_max,eta_st)
            
            # choose data viualization
            if event == 'Show 2D Plots': # if user clicks on  button 'Show 2D Plots',
                fig2D = complete_2d_plot(S_DBMD, sigma_DBMD, ke_DBMD, ZT_DBMD, delta, eta, rk, 'TE quantities of 2D Dirac double-band material') # create 2D plots
                if figure_canvas_agg0 is not None: # clear space for 2D plots
                        delete_fig_agg(figure_canvas_agg0)
                draw_figure(window['-FIG0-'].TKCanvas, fig2D) # and show 2D plots
              
            if event == 'Show 3D Plots >': #if user clicks on button 'Show 3D Plots >',
                window2.hide() # hide current window
                window2_3d = make_window2_3d() # open window to show 3D plots
        
            
            # save data
            if event == 'Save': # if user clicks on button 'Save',
                window2.hide() # hide current window
                window8 = make_window8() # and open window to save data
 
                    
    if window == window2_3d:
        
            if event == '< Prev':  # if user clicks on button '< Prev'
                window2_3d.close() # close current window
                window2.un_hide() # and re-open the previous window
            
            elif event == 'Next >': # if user clicks on button 'Next >', 
                window2_3d.hide() # hide current window
                window5 = make_window5() # and open next one to start the second part
            
            elif event == sg.WIN_CLOSED: # if user closes window,
                window2_3d.close() # close the program
                break
            
            else: # if user wants to visualize 3D plots
                delta, eta = np.meshgrid(np.arange(delta_min, delta_max, delta_st), np.arange(eta_min, eta_max, eta_st)) # create meshgrid from the arrays of energy gap and chemical potential
                
                # calculate and plot electrical conductivity sigma
                vectorized_function = np.vectorize(sigma_DBMD) # vectorize function
                output = vectorized_function(delta,eta) # vectorize output
                sigma1 = output.astype(float)
                fig_3D_sigma = plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$)', 0) # create 3D plot of sigma
                
                # calculate and plot Seebeck coefficient S
                vectorized_function = np.vectorize(S_DBMD) # vectorize function
                output = vectorized_function(delta,eta) # vectorize output
                S1 = output.astype(float)
                fig_3D_S = plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$)', 0) # create 3D plot of S
                
                # calculate and plot thermal electronic conductivity k_e
                vectorized_function = np.vectorize(ke_DBMD) # vectorize function
                output = vectorized_function(delta,eta) # vectorize output
                ke1 = output.astype(float)
                fig_3D_ke = plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)','$\kappa_{e}$($\eta$,$\Delta$)', 0) # create 3D plot of k_e
                
                # calculate and plot figure of merit ZT
                vectorized_function = np.vectorize(ZT_DBMD) # vectorize function
                output = vectorized_function(delta,eta,rk) # vectorize output
                ZT1 = output.astype(float)
                fig_3D_ZT = plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)','ZT($\eta$,$\Delta$)', 0) # create 3D plot of ZT
                
                # clear spaces for 3D plots                
                if figure_canvas_agg1 is not None:
                    delete_fig_agg(figure_canvas_agg1)
                if figure_canvas_agg2 is not None:
                    delete_fig_agg(figure_canvas_agg2)
                if figure_canvas_agg3 is not None:
                    delete_fig_agg(figure_canvas_agg3)
                if figure_canvas_agg4 is not None:
                    delete_fig_agg(figure_canvas_agg4)
                
                # show 3D plots
                figure_canvas_agg1 = draw_figure(window['-FIG1-'].TKCanvas, fig_3D_sigma) 
                figure_canvas_agg2 = draw_figure(window['-FIG2-'].TKCanvas, fig_3D_S) 
                figure_canvas_agg3 = draw_figure(window['-FIG3-'].TKCanvas, fig_3D_ke) 
                figure_canvas_agg4 = draw_figure(window['-FIG4-'].TKCanvas, fig_3D_ZT) 

                if event == 'Save': # if user clicks on button 'Save',
                    window2_3d.hide() # hide current window
                    window8 = make_window8() # and open window to save data
        
    if window == window5:
        if event == '< Choose Model': # if user clicks on button '< Choose Model',
            window5.close() # close current window
            window1.un_hide() # and re-open window to select the model
        
        elif event == sg.WIN_CLOSED : # if user closes window, 
            window5.close() # close the program
            break
        
        else: # if the user wants to visualize data
            # set parameters to the values entered by the user
            rk_min = (float(values['-IN_rk_min-'])) # minimum value of thermal lattice conductivity
            rk_max = (float(values['-IN_rk_max-'])) # maximum value of thermal lattice conductivity
            rk_step = (float(values['-IN_rk_step-'])) # thermal lattice conductivity step
            
            npoint = 31 # number of point to consider for energy gap and chemical potentail arrays 
            delta, eta, rk = np.meshgrid(np.linspace(0.002, 15, npoint), np.linspace(0.002, 15, npoint), np.arange(rk_min, rk_max, rk_step)) # create meshgrid from arrays of energy gap, chemical potential and thermal lattice conductivity
            
            # calculate figure of merit ZT
            ZT_vectorized_function = np.vectorize(ZT_DBMD) # vectorize function
            ZT_output = ZT_vectorized_function(delta,eta,rk) # vectorize output
            ZT1 = ZT_output.astype(float) 
            ZTmax = np.amax(ZT1,axis=1) # keep maximum values of ZT wrt chemical potential (2D matrix delta x rk)
            
            # plot figure of merit ZT
            rk1,delta1 = np.meshgrid(np.arange(rk_min, rk_max, rk_step), np.linspace(0.002, 15, npoint)) # create meshgrid from arrays of energy gap and thermal lattice conductivity
            fig_3D_ZT_rk = plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', 1) # create 3D plot
            
            if figure_canvas_agg1 is not None: # clear space for 3D plot
                delete_fig_agg(figure_canvas_agg1)
            
            figure_canvas_agg1 = draw_figure(window['-FIG0-'].TKCanvas, fig_3D_ZT_rk) # show 3D plot
            
            if event =='Save': # if user clicks on button 'Save',
                window5.hide() # hide current window
                window8 = make_window8() # and open window to save data

# DBMP   
    if window == window3:
        
        if event == '< Prev': # if user clicks on button '< Choose Model',
            window3.close() # close current window
            window1.un_hide() # and go back to model selection
        
        elif event == 'Next >': # if user clicks on button 'Next >', 
            window3.hide() # skip/end the first part
            window6 = make_window6() # and go to the second part
        
        elif event == sg.WIN_CLOSED : # if user closes window, 
            window3.close() # close the program
            break
        
        else:
            # set parameters to the values entered by the user
            delta_min = (float(values['-IN_delta_min-'])) # minimum energy gap value
            delta_max = (float(values['-IN_delta_max-'])) # maximum energy gap value
            eta_min = (float(values['-IN_eta_min-'])) # minimum chemical potential value
            eta_max = (float(values['-IN_eta_max-'])) # maximum chemical potential value
            delta_st = (float(values['-IN_delta_step-'])) # energy gap step
            eta_st = (float(values['-IN_eta_step-'])) # chemical potential step
            rk = (float(values['-IN_rk-'])) # thermal lattice conductivity (fixed)
            
            # create arrays of energy gap and chemical potential
            delta = np.arange(delta_min, delta_max, delta_st)
            eta = np.arange(eta_min, eta_max, eta_st)
            
            # choose data viualization
            if event == 'Show 2D Plots': #if user clicks on button 'Show 2D plots',
                fig2D = complete_2d_plot(S_DBMP, sigma_DBMP, ke_DBMP, ZT_DBMP, delta, eta, rk, 'TE quantities of 2D Dirac double-band material') # create 2D plots
                if figure_canvas_agg0 is not None: # clear space for 2D plots
                        delete_fig_agg(figure_canvas_agg0)
                figure_canvas_agg0 = draw_figure(window['-FIG0-'].TKCanvas, fig2D) #and show 2D plots
                
            if event == 'Show 3D Plots >': # if user clicks on button 'Show 3D plots >',
                window3.hide() # hide current window
                window3_3d = make_window3_3d() # and open window to show 3D plots
                
            if event == 'Save': # is user clicks on button 'Save',
                window3.hide() # hide current window
                window8 = make_window8() # and open window to save data
            
    if window == window3_3d:
        
            if event =='< Prev': # is user clicks on button '< Prev'
                window3_3d.close() # close current window
                window3.un_hide() #and re-open previous window
            
            elif event =='Next >': # if user clicks on button 'Next >'
                window3_3d.hide() #hide current window
                window6 = make_window6() # and open next one to start the second part
            
            elif event == sg.WIN_CLOSED : # if user closes window 
                window3_3d.close() # close the program
                break
            
            else:
                delta, eta = np.meshgrid(np.arange(delta_min,delta_max,delta_st), np.arange(eta_min,eta_max,eta_st)) # create meshgrid from the arrays of energy gap and chemical potential
                
                #calculate and plot electrical conductivity sigma
                vectorized_function = np.vectorize(sigma_DBMP) # vectorize function
                output = vectorized_function(delta,eta) # vectorize output
                sigma1 = output.astype(float)
                fig_3D_sigma = plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$)', 0) # create 3D plot of sigma
                
                #calculate and plot Seebeck coefficient S
                vectorized_function = np.vectorize(S_DBMP) # vectorize function
                output = vectorized_function(delta,eta) # vectorize output
                S1 = output.astype(float)
                fig_3D_S = plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$)', 0) # create 3D plot of S
                
                #calculate and plot thermal electronic conductivity k_e
                vectorized_function = np.vectorize(ke_DBMP) # vectorize function
                output = vectorized_function(delta,eta) # vectorize output
                ke1 = output.astype(float)
                fig_3D_ke = plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)', '$\kappa_{e}$($\eta$,$\Delta$)', 0) # create 3D plot of k_e
                    
                #calculate and plot figure of merit ZT
                vectorized_function = np.vectorize(ZT_DBMP) # vectorize function
                output = vectorized_function(delta,eta,rk) # vectorize output
                ZT1 = output.astype(float)
                fig_3D_ZT = plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)', 'ZT($\eta$,$\Delta$)', 0) # create 3D plot of ZT
                
                # clear spaces for 3D plots
                if figure_canvas_agg1 is not None:
                    delete_fig_agg(figure_canvas_agg1)
                if figure_canvas_agg2 is not None:
                    delete_fig_agg(figure_canvas_agg2)
                if figure_canvas_agg3 is not None:
                    delete_fig_agg(figure_canvas_agg3)
                if figure_canvas_agg4 is not None:
                    delete_fig_agg(figure_canvas_agg4)
                
                # show 3D plots
                figure_canvas_agg1 = draw_figure(window['-FIG1-'].TKCanvas, fig_3D_sigma) 
                figure_canvas_agg2 = draw_figure(window['-FIG2-'].TKCanvas, fig_3D_S) 
                figure_canvas_agg3 = draw_figure(window['-FIG3-'].TKCanvas, fig_3D_ke) 
                figure_canvas_agg4 = draw_figure(window['-FIG4-'].TKCanvas, fig_3D_ZT) 
                
                if event == 'Save': # if user clicks on button 'Save',
                    window3_3d.hide() # hide current window
                    window8 = make_window8() # and open window to save data
        
    if window == window6:
        
        if event == '< Choose Model': #if user clicks on button '< Choose Model',
            window6.close() # close current window
            window1.un_hide() # and re-open window to select the model
        
        
        elif event == sg.WIN_CLOSED: # if user closes window,
            window6.close() # close the programm
            break
        
        else: # if user wants to visualize data
            # set parameters to the values entered by the user
            rk_min = (float(values['-IN_rk_min-'])) # minimum value of thermal lattice conductivity
            rk_max = (float(values['-IN_rk_max-'])) # maximum value of thermal lattice conductivity
            rk_step = (float(values['-IN_rk_step-'])) # thermal lattice conductivity step
            
            npoint = 21 # number of point to consider for energy gap and chemical potential arrays
            delta, eta, rk = np.meshgrid(np.linspace(0.002, 15, npoint), np.linspace(0.002, 15, npoint), np.arange(rk_min, rk_max, rk_step)) # create meshgrid  from arrays of energy gap, chemical potential and thermal lattice conductivity
            
            # calculate figure of merit ZT
            ZT_vectorized_function = np.vectorize(ZT_DBMP) # vectorize function
            ZT_output = ZT_vectorized_function(delta,eta,rk) # vectorize output
            ZT1 = ZT_output.astype(float) 
            ZTmax = np.amax(ZT1, axis=1) # keep maximum values of ZT wrt to chemical potential (2D matrix delta x rk)
            
            # plot figure of merit ZT
            rk1, delta1 = np.meshgrid(np.arange(rk_min, rk_max, rk_step), np.linspace(0.002, 15, npoint)) # create meshgrid from arrays of energy gap and chemical potential
            fig_3D_ZT_rk = plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', 1)  # create 3D plot
            
            if figure_canvas_agg1 is not None: # clear space for 3D plot
                delete_fig_agg(figure_canvas_agg1)
            
            figure_canvas_agg1 = draw_figure(window['-FIG0-'].TKCanvas, fig_3D_ZT_rk) # show 3D plot
            
            if event =='Save': # if user clicks on button 'Save',
                window6.hide() # hide current window
                window8 = make_window8() # and open window to save data
# SBMP                        
    if window == window4:
        
        if event =='< Choose Model': # if user clicks on button '< Choose Model',
            window4.close() # close current window
            window1.un_hide() # and go back to model selection
        
        elif event =='Next >': # if user clicks on button 'Next >',
            window4.hide() # skip/end the first part
            window7 = make_window7() # and go to second part
        
        elif event == sg.WIN_CLOSED: # if user closes window,
            window4.close() # close the program
            break
        
        else:
            #set parameters to the values entered by the user 
            eta_min = (float(values['-IN_eta_min-'])) # minimum chemical potential value 
            eta_max = (float(values['-IN_eta_max-'])) # maximum chemical potential value
            eta_st = (float(values['-IN_eta_step-'])) # chemical potential step
            rk = (float(values['-IN_rk-'])) # thermal lattice conductivity (fixed)
            
            eta = np.arange(eta_min, eta_max, eta_st) # create array of chemical potential
            
            if event =='Show Plots': # if user clicks on button 'Show Plots'
                fig2D = complete_2d_plot_SBM(S_SBMP, sigma_SBMP, ke_SBMP, ZT_SBMP, eta, rk, 'TE quantities of 2D single-parabolic-band material') # create 2D plots
        
                if figure_canvas_agg0 is not None: # clear space for 2D plots
                        delete_fig_agg(figure_canvas_agg0)
                figure_canvas_agg0 = draw_figure(window['-FIG0-'].TKCanvas, fig2D) # show 2D plots
            
            if event =='Save': # if user clicks on button 'Save',
                window4.hide() # hide current window
                window8 = make_window8() # and open window to save data
                
    if window == window7:
        if event == '< Choose Model': # if user clicks on button '< Choose Model',
            window7.close() # close current window
            window1.un_hide() # and re-open window to select model
        
        
        elif event == sg.WIN_CLOSED : # if user closes window,
            window7.close() # close the program
            break
        
        else: # if the user wants to visualize data
            # set parameters to the values entered by the user
            rk_min = (float(values['-IN_rk_min-'])) # minimum value of thermal lattice conductivity
            rk_max = (float(values['-IN_rk_max-'])) # maximum value of thermal lattice conductivity
            rk_step = (float(values['-IN_rk_step-'])) # thermal lattice conductivity step
            
            npoint = 51 # number of points to consider for energy gap array
            eta,rk = np.meshgrid(np.linspace(-10, 10, npoint), np.arange(rk_min, rk_max, rk_step)) # create meshgrid from arrays of energy gap and thermal lattice conductivity
            
            # calculate figure of merit ZT
            vectorized_function = np.vectorize(ZT_SBMP) # vectorize function
            output = vectorized_function(eta, rk) # vectorize output
            ZT1 = output.astype(float)
            
            fig_3D_ZT_rk = plot_anim_3d(eta, rk, ZT1, '$\eta$', '$\kappa_L$', 'ZT($\eta$,$\kappa_l$)', '3D plot: 2D single-parabolic-band material', 1) # plot ZT
            
            if figure_canvas_agg1 is not None: # clear space for ZT plot
                delete_fig_agg(figure_canvas_agg1)
            figure_canvas_agg1 = draw_figure(window['-FIG0-'].TKCanvas, fig_3D_ZT_rk) # show ZT plot
            
            if event == 'Save': # if user clicks on button 'Save',
                window7.hide() # hide current window
                window8 = make_window8() # and open window to save data
            
    if window == window8:
        
        if event== sg.WIN_CLOSED : # if user closes window,
            window8.close() # close the program
            break
        
        else: # if user wants to save data
            # set parameters to values entered by the user
            path_txt = values['-IN_txt_path-'] # path to save the .txt file
            title_model = values['-IN_txt_model'] # first part of the title: model (DBMD, DBMP, SBMP)
            title_part = values['-IN_txt_part'] # second part of the title: part of the study (1 for 1st part, 2 for 2nd part)
            title_txt = values['-IN_txt_file-'] # third part of the title: additional specification desired by the user
            
            # create path to new file
            path_to_file = path_txt + title_model + title_part + title_txt + '.txt'
            
            if event == 'Save txt': # if user clicks on button 'Save txt',
                # create a new txt file on the desired path
                with open(path_to_file, 'w') as f:
                    #print('ok')
                    
                    if title_model == 'DBMD': # save data for DBMD model
                        if title_part == '1': # for 1st part of the study
                            # arrays for energy gap and chemical potential
                            delta = np.arange(delta_min, delta_max, delta_st) 
                            eta = np.arange(eta_min, eta_max, eta_st)
                            
                            # write on txt file
                            f.write('r$_k$=' + str(rk) + '\n') # the value of the fixed thermal lattice conductivity
                            f.write('$\delta$' + ',' + '$\eta$' + ',' + '$\sigma$' + 'S' + '$\kappa_e$' + 'ZT' + "\n") # titles of the columns
                            f.write('\n')
                            # write values in associated columns
                            for i in range(delta.size):
                                for j in range(eta.size):
                                    f.write(str(delta[i]) + ',' + str(eta[j]) + ',' + str(sigma_DBMD(delta[i], eta[j])) + ',' + str(S_DBMD(delta[i], eta[j])) + ',' + str(ke_DBMD(delta[i], eta[j])) + ',' + str(ZT_DBMD(delta[i], eta[j], 1)) + "\n")
                            f.close()
                            print('done')
                        
                        elif title_part == '2': # for 2nd part of the study
                            # arrays for thermal lattice conductivity and energy gap
                            rk1 = np.arange(rk_min, rk_max, rk_step)
                            delta1 = np.linspace(0.002, 15, npoint)
                            
                            # write on txt file
                            f.write('$r_k$' + ',' + '$\delta$' + ',' + 'ZT$_{max}$' + "\n") # titles of the columns
                            f.write('\n')
                            # write values in associated columns
                            for i in range(rk1.size):
                                for j in range(delta1.size):
                                    f.write(str(rk1[i]) + ',' + str(delta1[j]) + ',' + str(ZTmax[j][i]) + "\n")
                            f.close()
                            print('done')
                            
                    
                    if title_model == 'DBMP': # save data for DBMP model
                        if title_part == '1': # for 1st part of the study
                            # arrays for energy gap and chemical potential
                            delta = np.arange(delta_min, delta_max, delta_st)
                            eta = np.arange(eta_min, eta_max, eta_st)
                            
                            # write on txt file
                            f.write('r$_k$=' + str(rk) + '\n') # the value of the fixed thermal lattice conductivity
                            f.write('$\delta$' + ',' + '$\eta$' + ',' + '$\sigma$' + 'S' + '$\kappa_e$' + 'ZT' + "\n") # titles of the columns
                            f.write('\n')
                            # write values in associated columns
                            for i in range(delta.size):
                                for j in range(eta.size):
                                    f.write(str(delta[i]) + ',' + str(eta[j]) + ',' + str(sigma_DBMP(delta[i], eta[j])) + ',' + str(S_DBMP(delta[i], eta[j])) + ',' + str(ke_DBMP(delta[i], eta[j])) + ',' + str(ZT_DBMP(delta[i], eta[j], 1)) + "\n")
                            f.close()
                            print('done')
                            
                        if title_part == '2': # for 2nd part of the study
                            # arrays for thermal lattice conductivity and energy gap
                            rk1 = np.arange(rk_min, rk_max, rk_step)
                            delta1 = np.linspace(0.002, 15, npoint)
                            
                            # write on txt file
                            f.write('$r_k$' + ',' + '$\delta$' + ',' + 'ZT$_{max}$' + "\n") # titles of the columns
                            f.write('\n')
                            # write values in associated columns
                            for i in range(rk1.size):
                                for j in range(delta1.size):
                                    f.write(str(rk1[i]) + ',' + str(delta1[j]) + ',' + str(ZTmax[j][i]) + "\n")
                            f.close()
                            print('done')
                            
                            
                    if title_model == 'SBMP': # save data for SBMP model
                        if title_part == '1': # for 1st part of the study
                            eta = np.arange(eta_min, eta_max, eta_st) # array for chemical potential
                            
                            # write on txt file
                            f.write('r$_k$=' + str(rk) + '\n') # the value of the fixed thermal lattice conductivity
                            f.write('$\eta$' + ',' + '$\sigma$' + 'S' + '$\kappa_e$' + 'ZT' + "\n") # titles of the columns
                            f.write('\n')
                            # write values in associated columns
                            for j in range(eta.size):
                                f.write(str(eta[j]) + ',' + str(sigma_SBMP(eta[j])) + ',' + str(S_SBMP(eta[j])) + ',' + str(ke_SBMP(eta[j])) + ',' + str(ZT_SBMP(eta[j], 1)) + "\n")
                            f.close()
                            print('done')
                            
                        if title_part == '2': # for 2nd part of the study
                            # arrays for chemical potential and thermal lattice conductivity 
                            eta = np.linspace(-10, 10, npoint)
                            rk = np.arange(rk_min, rk_max, rk_step)
                            
                            # write on txt file
                            f.write('$\eta$' + ',' + 'r$_k$' + 'ZT' + "\n") # titles of the columns
                            f.write('\n')
                            # write values in associated columns
                            for i in range(eta.size):
                                for j in range(rk.size):
                                    f.write(str(eta[i]) + ',' + str(rk[j]) + ',' + str(ZT_SBMP(eta[i], 1)) + "\n")
                            f.close()
                            print('done')
                            
            elif event == 'Done': # if user clicks on button 'Done'
                # go back to the previous page
                if title_model == 'DBMD': 
                    if title_part == '1':
                        window8.close()
                        window2.un_hide()
                    if title_part == '2':
                        window8.close()
                        window5.un_hide()
                        
                if title_model == 'DBMP':
                    if title_part == '1':
                        window8.close()
                        window3.un_hide()
                    if title_part == '2':
                        window8.close()
                        window6.un_hide()
                        
                if title_model == 'SBMP':
                    if title_part=='1':
                        window8.close()
                        window4.un_hide()
                    if title_part == '2':
                        window8.close()
                        window7.un_hide()
                    
window.close()    
    