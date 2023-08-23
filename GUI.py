# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:08:19 2023

@author: viola
"""

import PySimpleGUI as sg
from DBM_Dirac import *
from DBM_Parabolic import *
from SBM_Parabolic import *
from plots import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")

def draw_figure(canvas,
                figure):
    """
    Function that draws the wanted figure in the empty canvas of the window

    Parameters
    ----------
    canvas : TYPE PySimpleGUI.Canvas(canvas, background_color, size)
        DESCRIPTION. drawable panel on the surface of the PySimpleGUI application window
    figure : TYPE matplotlib.figure.Figure()
        DESCRIPTION. figure we want to draw on the panel 

    Returns
    -------
    figure_canvas_agg : TYPE FigureCanvasTkAgg(figure, canvas)
        DESCRIPTION. figure drawn on the canvas

    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# window 1 = the role of  delta and eta
# window 2 = 2D plots
# window 3 = plots
# window 4 = the role of rk 
# window 5 = 3D plot
# window 6 = try another model or end
# if try another model: clear canvas, window 1
def make_window1(): #select model
    """
    Make the first window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text('Model to apply'), sg.InputText(key='-IN_Model-')], #2P,2D,1P
               
        [sg.Button('Next >')],
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")



def make_window2(): # DBMD, the role of delta and eta
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text("Dependency on the energy gap and the chemical potential")],
        [sg.Text("Dirac Double Band Model")],
        [sg.Text('Minimum energy gap'), sg.InputText(key='-IN_delta_min-')], #define Delta range
        [sg.Text('Maximum energy gap'), sg.InputText(key='-IN_delta_max-')],
        [sg.Text('Energy gap step'), sg.InputText(key='-IN_delta_step-')],
        [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], #Define eta range
        [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
        [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],

        [sg.Canvas(key='-FIG0-'),sg.Canvas(key='-FIG1-'),sg.Canvas(key='-FIG2-'),sg.Canvas(key='-FIG3-'),sg.Canvas(key='-FIG4-')],
        [sg.Button('< Prev'),sg.Button('Show 2D Plots'), sg.Button('Show 3D Plots'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window3(): # DBMP, the role of delta and eta
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text("Dependency on the energy gap and the chemical potential")],
        [sg.Text("Double-Parabolic-Band Model")],
        [sg.Text('Minimum energy gap'), sg.InputText(key='-IN_delta_min-')], #define Delta range
        [sg.Text('Maximum energy gap'), sg.InputText(key='-IN_delta_max-')],
        [sg.Text('Energy gap step'), sg.InputText(key='-IN_delta_step-')],
        [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], #Define eta range
        [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
        [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
        
        [sg.Canvas(key='-FIG0-'),sg.Canvas(key='-FIG1-'),sg.Canvas(key='-FIG2-'),sg.Canvas(key='-FIG3-'),sg.Canvas(key='-FIG4-')],
        [sg.Button('< Prev'),sg.Button('Show 2D Plots'), sg.Button('Show 3D Plots'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")


def make_window4(): # SBMP, the role of delta and eta
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text("Dependency on the energy gap and the chemical potential")],
        [sg.Text("Single-Parabolic-Band Model")],
        [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], #Define eta range
        [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
        [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
        
        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show Plots'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window5(): # the role of rk
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text("Dependency on the phonon thermal conductivity")],
        [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], #Define eta range
        [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
        [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show Plot'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window6(): # the role of rk
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text("Dependency on the phonon thermal conductivity")],
        [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], #Define eta range
        [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
        [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show Plot'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window7(): # the role of rk
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [
        [sg.Text("Thermoelectric quantities simulation")],
        [sg.Text("Dependency on the phonon thermal conductivity")],
        [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], #Define eta range
        [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
        [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show Plot'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

#Make the first window and set the others windows to none 
window1, window2, window3, window4, window5, window6, window7 = make_window1(), None, None, None, None, None, None

#Set the figure drawings to None in order to be able to update them each time 
figure_canvas_agg0 = None
figure_canvas_agg_3d0=None
figure_canvas_agg_3d1=None
figure_canvas_agg_3d2=None
figure_canvas_agg_3d3=None
figure_canvas_agg_chem_pot=None
figure_canvas_agg_init_c=None
figure_canvas_agg = None
#set the color bar to None in order to be able to update it later
cbar=None

while True:
    
    #read all the events, windows and values entered on the windows
    window,event,values = sg.read_all_windows()
    
    if window==window1:
              
        if event== sg.WIN_CLOSED : # if user closes window close the programm
            break
        
        elif event == 'Next >': #if user goes on the button show plots
            
        
            model=(values['-IN_Model-'])
            
            
            if model=='DBMD' :
                window1.hide()
                window2 = make_window2()
            
            elif model=='DBMP':
                window1.hide()
                window3 = make_window3()
            
            elif model=='SBMP':
                window1.hide()
                window4 = make_window4()              
# DBMD               
    if window == window2:
        if event=='< Prev':
            window2.close()
            window1.un_hide()
        
        elif event=='Next >':
            window2.hide()
            window5 = make_window5()
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window2.close()
            break
        
        else:
            #set values to the entered user values
            delta_min=(float(values['-IN_delta_min-']))
            delta_max=(float(values['-IN_delta_max-']))
            eta_min=(float(values['-IN_eta_min-']))
            eta_max=(float(values['-IN_eta_max-']))
            delta_st=(float(values['-IN_delta_step-']))
            eta_st=(float(values['-IN_eta_step-']))
            
            #choose data viualization
            #2D
            if event=='Show 2D Plots':
                fig2D = complete_2d_plot(S_DBMD,sigma_DBMD,ke_DBMD,ZT_DBMD,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st,'TE quantities of 2D Dirac double-band material')
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg0)
                        figure_canvas_agg0 = draw_figure(window["-FIG0-"].TKCanvas, fig2D) 
                
            #3D    
            elif event=='Show 3D Plots':
                npoint=51
                #delta_min=window2.delta_min
                delta, eta = np.meshgrid(np.arange(delta_min,delta_max,delta_st), np.arange(eta_min,eta_max,eta_st))
                #print(ok)
                vectorized_function = np.vectorize(sigma_DBMD)
                output = vectorized_function(delta,eta)
                sigma1=output.astype(float)
                fig_3D_sigma=plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$) of 2D double-band Dirac material')
                
                vectorized_function = np.vectorize(S_DBMD)
                output = vectorized_function(delta,eta)
                S1=output.astype(float)
                fig_3D_S=plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$) of 2D double-band Dirac material')
                
                vectorized_function = np.vectorize(ke_DBMD)
                output = vectorized_function(delta,eta)
                ke1=output.astype(float)
                fig_3D_ke=plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)', '$\kappa_{e}$($\eta$,$\Delta$) of 2D double-band Dirac material')
                    
                vectorized_function = np.vectorize(ZT_DBMD)
                output = vectorized_function(delta,eta,1)
                ZT1=output.astype(float)
                fig_3D_ZT=plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)', 'ZT($\eta$,$\Delta$) 2D double-band Dirac material')
                
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg_3d0)
                        delete_fig_agg(figure_canvas_agg_3d1)
                        delete_fig_agg(figure_canvas_agg_3d2)
                        delete_fig_agg(figure_canvas_agg_3d3)
                        figure_canvas_agg_3d0 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_sigma) 
                        figure_canvas_agg_3d1 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_S) 
                        figure_canvas_agg_3d2 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_ke) 
                        figure_canvas_agg_3d3 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_ZT) 
             
        
        
    if window==window5:
        if event=='< Prev':
            window5.close()
            window1.un_hide()
        
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window5.close()
            break
        
        else:
            rk_min=(float(values['-IN_rk_min-']))
            rk_max=(float(values['-IN_rk_max-']))
            rk_step=(float(values['-IN_rk_step-']))
            
            npoint=21
            delta, eta, rk=np.meshgrid(np.linspace(0.002,15,npoint),np.linspace(0.002,15,npoint),np.arange(rk_min,rk_max,rk_step))   
            ZT_vectorized_function = np.vectorize(ZT_DBMD)
            ZT_output = ZT_vectorized_function(delta,eta,rk)
            ZT1=ZT_output.astype(float) #3d matrix
            ZTmax=np.amax(ZT1,axis=1) #2d matrix delta,rk 10x10
            
            
            rk1,delta1=np.meshgrid(np.arange(rk_min,rk_max,rk_step),np.linspace(0.002,15,npoint))
            
            plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$) of 2D double-band Dirac material')
#DBMP   
    if window == window3:
        
        if event=='< Prev':
            window3.close()
            window1.un_hide()
        
        elif event=='Next >':
            window3.hide()
            window6 = make_window6()
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window3.close()
            break
        
        else:
            #set values to the entered user values
            delta_min=(float(values['-IN_delta_min-']))
            delta_max=(float(values['-IN_delta_max-']))
            eta_min=(float(values['-IN_eta_min-']))
            eta_max=(float(values['-IN_eta_max-']))
            delta_st=(float(values['-IN_delta_step-']))
            eta_st=(float(values['-IN_eta_step-']))
            
            #choose data viualization
            #2D
            if event=='Show 2D Plots':
                fig2D = complete_2d_plot(S_DBMP,sigma_DBMP,ke_DBMP,ZT_DBMP,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st,'TE quantities of 2D Dirac double-band material')
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg0)
                        figure_canvas_agg0 = draw_figure(window["-FIG0-"].TKCanvas, fig2D) 
                
            #3D    
            if event=='Show 3D Plots':
                #npoint=51
                #delta_min=window2.delta_min
                delta, eta = np.meshgrid(np.arange(delta_min,delta_max,delta_st), np.arange(eta_min,eta_max,eta_st))
                #print(ok)
                vectorized_function = np.vectorize(sigma_DBMP)
                output = vectorized_function(delta,eta)
                sigma1=output.astype(float)
                fig_3D_sigma=plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
                
                vectorized_function = np.vectorize(S_DBMP)
                output = vectorized_function(delta,eta)
                S1=output.astype(float)
                fig_3D_S=plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
                
                vectorized_function = np.vectorize(ke_DBMP)
                output = vectorized_function(delta,eta)
                ke1=output.astype(float)
                fig_3D_ke=plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
                    
                vectorized_function = np.vectorize(ZT_DBMP)
                output = vectorized_function(delta,eta,1)
                ZT1=output.astype(float)
                fig_3D_ZT=plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
                
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg_3d0)
                        delete_fig_agg(figure_canvas_agg_3d1)
                        delete_fig_agg(figure_canvas_agg_3d2)
                        delete_fig_agg(figure_canvas_agg_3d3)
                        figure_canvas_agg_3d0 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_sigma) 
                        figure_canvas_agg_3d1 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_S) 
                        figure_canvas_agg_3d2 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_ke) 
                        figure_canvas_agg_3d3 = draw_figure(window["-FIG1-"].TKCanvas, fig3D_ZT) 
             
        
    if window==window6:
        if event=='< Prev':
            window6.close()
            window1.un_hide()
        
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window5.close()
            break
        
        else:
            rk_min=(float(values['-IN_rk_min-']))
            rk_max=(float(values['-IN_rk_max-']))
            rk_step=(float(values['-IN_rk_step-']))
            
            npoint=21
            delta, eta, rk=np.meshgrid(np.linspace(0.002,15,npoint),np.linspace(0.002,15,npoint),np.arange(rk_min,rk_max,rk_step))   
            ZT_vectorized_function = np.vectorize(ZT_DBMP)
            ZT_output = ZT_vectorized_function(delta,eta,rk)
            ZT1=ZT_output.astype(float) #3d matrix
            ZTmax=np.amax(ZT1,axis=1) #2d matrix delta,rk 10x10
            
            
            rk1,delta1=np.meshgrid(np.arange(rk_min,rk_max,rk_step),np.linspace(0.002,15,npoint))
            
            plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$) of 2D double-parabolic-band material')
        
    
# SBMP                        
    if window == window4:
        if event=='< Prev':
            window4.close()
            window1.un_hide()
        
        elif event=='Next >':
            window4.hide()
            window7 = make_window7()
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window3.close()
            break
        
        
        if event=='Show Plots':
            #set values to the entered user values
            eta_min=(float(values['-IN_eta_min-']))
            eta_max=(float(values['-IN_eta_max-']))
            eta_st=(float(values['-IN_eta_step-']))
            
            fig2D = complete_2d_plot_SBM(S_SBMP,sigma_SBMP,ke_SBMP,ZT_SBMP,eta_min,eta_max,eta_st,'TE quantities of 2D single-parabolic-band material')
        
        if figure_canvas_agg0 is not None:
                delete_fig_agg(figure_canvas_agg0)
                figure_canvas_agg0 = draw_figure(window["-FIG0-"].TKCanvas, fig2D) 
            
            
    if window==window7:
        if event=='< Prev':
            window7.close()
            window1.un_hide()
        
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window7.close()
            break
        
        else:
            rk_min=(float(values['-IN_rk_min-']))
            rk_max=(float(values['-IN_rk_max-']))
            rk_step=(float(values['-IN_rk_step-']))
            
            npoint=51
            eta,rk = np.meshgrid(np.linspace(-10,10,npoint), np.arange(rk_min,rk_max,rk_step))
            vectorized_function = np.vectorize(ZT_SBMP)
            output = vectorized_function(eta,rk)
            ZT1=output.astype(float)
            plot_anim_3d(eta, rk, ZT1, '$\eta$', '$\kappa_L$', 'ZT($\eta$,$\kappa_l$)', '3D plot: 2D single-parabolic-band material')
    
    
    