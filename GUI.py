# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:08:19 2023

@author: viola
"""


from DBM_Dirac import *
from DBM_Parabolic import *
from SBM_Parabolic import *
from plots import plot_anim_3d,subplots_2D_graph,complete_2d_plot,complete_2d_plot_SBM


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg


#root=tk.Tk()
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
    figure_canvas_agg = FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    
    return figure_canvas_agg

def delete_fig_agg(fig_agg):
    """
    Function to delet the figure drawn on the canvas 

    Parameters
    ----------
    fig_agg : TYPE FigureCanvasTkAgg(figure, canvas)
        DESCRIPTION. figure drawn on the canvas

    Returns
    -------
    None.

    """
    fig_agg.get_tk_widget().forget()
    plt.close('all')

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
        [sg.Text("Thermoelectric quantities simulation: dependency on the energy gap and the chemical potential - Double-Dirac-Band Model")],
        [sg.Text('Minimum energy gap'), sg.InputText(key='-IN_delta_min-')], #define Delta range
        [sg.Text('Maximum energy gap'), sg.InputText(key='-IN_delta_max-')],
        [sg.Text('Energy gap step'), sg.InputText(key='-IN_delta_step-')],
        [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], #Define eta range
        [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
        [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
        [sg.Text('Lattice thermal conductivity'), sg.InputText(key='-IN_rk-')],

        
        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show 2D Plots'), sg.Button('Save'), sg.Button('Show 3D Plots>'),sg.Button('Next >')],
        
        ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window2_3d():
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [[sg.Text("Thermoelectric quantities simulation: dependency on the energy gap and the chemical potential - Double-Dirac-Band Model")],
              [sg.Text('3D plots')],
              [sg.Canvas(key='-FIG1-'),sg.Canvas(key='-FIG2-')],
              [sg.Canvas(key='-FIG3-'),sg.Canvas(key='-FIG4-')],
              
              [sg.Button('< Prev'),sg.Button('Show 3D Plots'),sg.Button('Save'),sg.Button('Next >')],
              
              ]

    return sg.Window('3D plots', layout,location=(0, 0),
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
        [sg.Text("Thermoelectric quantities simulation: dependency on the energy gap and the chemical potential - Double-Parabolic-Band Model")],
        [sg.Text('Minimum energy gap'), sg.InputText(key='-IN_delta_min-')], #define Delta range
        [sg.Text('Maximum energy gap'), sg.InputText(key='-IN_delta_max-')],
        [sg.Text('Energy gap step'), sg.InputText(key='-IN_delta_step-')],
        [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], #Define eta range
        [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
        [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
        [sg.Text('Lattice thermal conductivity'), sg.InputText(key='-IN_rk-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show 2D Plots'), sg.Button('Save'), sg.Button('Show 3D Plots >'),sg.Button('Next >')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window3_3d():
    """
    Make the second window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [[sg.Text("Thermoelectric quantities simulation: dependency on the energy gap and the chemical potential - Double-Parabolic-Band Model")],
              [sg.Text('3D plots')],
              [sg.Canvas(key='-FIG1-'),sg.Canvas(key='-FIG2-')],
              [sg.Canvas(key='-FIG3-'),sg.Canvas(key='-FIG4-')],
              
              [sg.Button('< Prev'),sg.Button('Show 3D Plots'), sg.Button('Save'),sg.Button('Next >')],
              
              ]

    return sg.Window('3D plots of the free energy in the different spaces', layout,location=(0, 0),
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
        [sg.Text("Thermoelectric quantities simulation: dependency on the energy gap and the chemical potential - Single-Parabolic-Band Model")],
        [sg.Text('Minimum chemical potential'), sg.InputText(key='-IN_eta_min-')], #Define eta range
        [sg.Text('Maximum chemical potential'), sg.InputText(key='-IN_eta_max-')],
        [sg.Text('Chemical potential step'), sg.InputText(key='-IN_eta_step-')],
        [sg.Text('Lattice thermal conductivity'), sg.InputText(key='-IN_rk-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Prev'),sg.Button('Show Plots'), sg.Button('Save'),sg.Button('Next >')],
    
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
        [sg.Text("Thermoelectric quantities simulation: dependency on the phonon thermal conductivity - Double-Dirac-Band Model")],
        [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], #Define eta range
        [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
        [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Choose Model'),sg.Button('Show Plot'), sg.Button('Save')],
    
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
        [sg.Text("Thermoelectric quantities simulation: dependency on the phonon thermal conductivity - Double-Parabolic-Band Model")],
        [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], #Define eta range
        [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
        [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Choose Model'),sg.Button('Show Plot'), sg.Button('Save')],
    
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
        [sg.Text("Thermoelectric quantities simulation: dependency on the phonon thermal conductivity - Single-Parabolic-Band Model")],
        [sg.Text('Minimum lattice conductivity'), sg.InputText(key='-IN_rk_min-')], #Define eta range
        [sg.Text('Maximum lattice conductivity'), sg.InputText(key='-IN_rk_max-')],
        [sg.Text('Lattice conductivity step'), sg.InputText(key='-IN_rk_step-')],

        [sg.Canvas(key='-FIG0-')],
        [sg.Button('< Choose Model'),sg.Button('Show Plot'), sg.Button('Save')],
    
    ]

    return sg.Window(
        "Thermoelectric quantities simulation",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center")

def make_window8():
    """
    Make the 6th window of the GUI

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    layout = [[sg.Text('Save the data')],
              [sg.Text('Path of the directory for the txt data file:'),sg.InputText(key='-IN_txt_path-')],
              [sg.Text('Name of the txt file:'),sg.InputText(key='-IN_txt_model'),sg.InputText(key='-IN_txt_part'),sg.InputText(key='-IN_txt_file-')],
              [sg.Button('Save txt'),sg.Button('Done')],
              ]

    return sg.Window('Thermoelectric quantities simulation - Save the data', layout, location=(0, 0),
    finalize=True, element_justification="center")


#Make the first window and set the others windows to none 
window1, window2, window2_3d, window3, window3_3d, window4, window5, window6, window7, window8 = make_window1(), None, None, None, None, None, None, None, None, None

#Set the figure drawings to None in order to be able to update them each time 
figure_canvas_agg0 = None
figure_canvas_agg1=None
figure_canvas_agg2=None
figure_canvas_agg3=None
figure_canvas_agg4=None

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
        #window.maximize()
        if event=='< Choose Model':
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
            rk=(float(values['-IN_rk-']))
            
            delta=np.arange(delta_min, delta_max, delta_st)
            eta=np.arange(eta_min,eta_max,eta_st)
            
            #choose data viualization
            #2D
            if event=='Show 2D Plots':
                fig2D = complete_2d_plot(S_DBMD,sigma_DBMD,ke_DBMD,ZT_DBMD,delta,eta,rk,'TE quantities of 2D Dirac double-band material')
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg0)
                #figure_canvas_agg0 = 
                draw_figure(window['-FIG0-'].TKCanvas, fig2D) 
            
            #3D    
            if event=='Show 3D Plots >':
                window2.hide()
                window2_3d=make_window2_3d()
                print('here')
    
            if event=='Save':
                window2.hide()
                window8=make_window8()
        
        
                    
    if window == window2_3d:
            if event=='< Prev':
                window2_3d.close()
                window2.un_hide()
            
            elif event=='Next >':
                window2_3d.hide()
                window5 = make_window5()
            
            elif event== sg.WIN_CLOSED : # if user closes window close the programm
                window2_3d.close()
                break
            #print('here')
            
            else:
                delta, eta = np.meshgrid(np.arange(delta_min,delta_max,delta_st), np.arange(eta_min,eta_max,eta_st))
                                
                vectorized_function = np.vectorize(sigma_DBMD)
                output = vectorized_function(delta,eta)
                sigma1=output.astype(float)
                fig_3D_sigma=plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$)',0)
                
                vectorized_function = np.vectorize(S_DBMD)
                output = vectorized_function(delta,eta)
                S1=output.astype(float)
                fig_3D_S=plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$)',0)
                
                vectorized_function = np.vectorize(ke_DBMD)
                output = vectorized_function(delta,eta)
                ke1=output.astype(float)
                fig_3D_ke=plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)','$\kappa_{e}$($\eta$,$\Delta$)',0)
                    
                vectorized_function = np.vectorize(ZT_DBMD)
                output = vectorized_function(delta,eta,rk)
                ZT1=output.astype(float)
                fig_3D_ZT=plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)','ZT($\eta$,$\Delta$)',0)
                                
                if figure_canvas_agg1 is not None:
                    delete_fig_agg(figure_canvas_agg1)
                if figure_canvas_agg2 is not None:
                    delete_fig_agg(figure_canvas_agg2)
                if figure_canvas_agg3 is not None:
                    delete_fig_agg(figure_canvas_agg3)
                if figure_canvas_agg4 is not None:
                    delete_fig_agg(figure_canvas_agg4)
                       
                figure_canvas_agg1 = draw_figure(window['-FIG1-'].TKCanvas, fig_3D_sigma) 
                figure_canvas_agg2 = draw_figure(window['-FIG2-'].TKCanvas, fig_3D_S) 
                figure_canvas_agg3 = draw_figure(window['-FIG3-'].TKCanvas, fig_3D_ke) 
                figure_canvas_agg4 = draw_figure(window['-FIG4-'].TKCanvas, fig_3D_ZT) 

                if event=='Save':
                    window2_3d.hide()
                    window8=make_window8()
        
    if window==window5:
        if event=='< Choose Model':
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
            print(ZTmax)
            
            rk1,delta1=np.meshgrid(np.arange(rk_min,rk_max,rk_step),np.linspace(0.002,15,npoint))
            
            fig_3D_ZT_rk=plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$)',1)
            
            if figure_canvas_agg1 is not None:
                delete_fig_agg(figure_canvas_agg1)
            
            figure_canvas_agg1 = draw_figure(window['-FIG0-'].TKCanvas, fig_3D_ZT_rk) 
            
            if event=='Save':
                window5.hide()
                window8=make_window8()

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
            rk=(float(values['-IN_rk-']))
            
            delta=np.arange(delta_min, delta_max, delta_st)
            eta=np.arange(eta_min,eta_max,eta_st)
            
            #choose data viualization
            #2D
            if event=='Show 2D Plots':
                fig2D = complete_2d_plot(S_DBMP,sigma_DBMP,ke_DBMP,ZT_DBMP,delta,eta,rk,'TE quantities of 2D Dirac double-band material')
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg0)
                figure_canvas_agg0 = draw_figure(window['-FIG0-'].TKCanvas, fig2D) 
                
            #3D 
            if event=='Show 3D Plots >':
                window3.hide()
                window3_3d=make_window3_3d()
                print('here')
                
            if event=='Save':
                window3.hide()
                window8=make_window8()
            
    if window == window3_3d:
            if event=='< Prev':
                window3_3d.close()
                window3.un_hide()
            
            elif event=='Next >':
                window3_3d.hide()
                window6 = make_window6()
            
            elif event== sg.WIN_CLOSED : # if user closes window close the programm
                window3_3d.close()
                break
            #print('here')
            
            else:
                delta, eta = np.meshgrid(np.arange(delta_min,delta_max,delta_st), np.arange(eta_min,eta_max,eta_st))
                
                vectorized_function = np.vectorize(sigma_DBMP)
                output = vectorized_function(delta,eta)
                sigma1=output.astype(float)
                fig_3D_sigma=plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '$\sigma$($\eta$,$\Delta$)',0)
                
                vectorized_function = np.vectorize(S_DBMP)
                output = vectorized_function(delta,eta)
                S1=output.astype(float)
                fig_3D_S=plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', 'S($\eta$,$\Delta$)',0)
                
                vectorized_function = np.vectorize(ke_DBMP)
                output = vectorized_function(delta,eta)
                ke1=output.astype(float)
                fig_3D_ke=plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)', '$\kappa_{e}$($\eta$,$\Delta$)',0)
                    
                vectorized_function = np.vectorize(ZT_DBMP)
                output = vectorized_function(delta,eta,rk)
                ZT1=output.astype(float)
                fig_3D_ZT=plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)', 'ZT($\eta$,$\Delta$)',0)
                
                if figure_canvas_agg1 is not None:
                    delete_fig_agg(figure_canvas_agg1)
                if figure_canvas_agg2 is not None:
                    delete_fig_agg(figure_canvas_agg2)
                if figure_canvas_agg3 is not None:
                    delete_fig_agg(figure_canvas_agg3)
                if figure_canvas_agg4 is not None:
                    delete_fig_agg(figure_canvas_agg4)
                       
                figure_canvas_agg1 = draw_figure(window['-FIG1-'].TKCanvas, fig_3D_sigma) 
                figure_canvas_agg2 = draw_figure(window['-FIG2-'].TKCanvas, fig_3D_S) 
                figure_canvas_agg3 = draw_figure(window['-FIG3-'].TKCanvas, fig_3D_ke) 
                figure_canvas_agg4 = draw_figure(window['-FIG4-'].TKCanvas, fig_3D_ZT) 
                
                if event=='Save':
                    window3_3d.hide()
                    window8=make_window8()
        
    if window==window6:
        if event=='< Choose Model':
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
            
            fig_3D_ZT_rk=plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '$ZT_{max}$($\Delta$,$\kappa_{L}$)',1)
            
            if figure_canvas_agg1 is not None:
                delete_fig_agg(figure_canvas_agg1)
            figure_canvas_agg1 = draw_figure(window['-FIG0-'].TKCanvas, fig_3D_ZT_rk) 
            
            if event=='Save':
                window6.hide()
                window8=make_window8()
# SBMP                        
    if window == window4:
        if event=='< Choose Model':
            window4.close()
            window1.un_hide()
        
        elif event=='Next >':
            window4.hide()
            window7 = make_window7()
        
        elif event== sg.WIN_CLOSED : # if user closes window close the programm
            window3.close()
            break
        
        else:
        
            #set values to the entered user values
            eta_min=(float(values['-IN_eta_min-']))
            eta_max=(float(values['-IN_eta_max-']))
            eta_st=(float(values['-IN_eta_step-']))
            rk=(float(values['-IN_rk-']))
            
            eta=np.arange(eta_min,eta_max,eta_st)
            
            if event=='Show Plots':
                fig2D = complete_2d_plot_SBM(S_SBMP,sigma_SBMP,ke_SBMP,ZT_SBMP,eta,rk,'TE quantities of 2D single-parabolic-band material')
        
                if figure_canvas_agg0 is not None:
                        delete_fig_agg(figure_canvas_agg0)
                figure_canvas_agg0 = draw_figure(window['-FIG0-'].TKCanvas, fig2D) 
            
            if event=='Save':
                window4.hide()
                window8=make_window8()
                
    if window==window7:
        if event=='< Choose Model':
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
            
            fig_3D_ZT_rk=plot_anim_3d(eta, rk, ZT1, '$\eta$', '$\kappa_L$', 'ZT($\eta$,$\kappa_l$)', '3D plot: 2D single-parabolic-band material',1)
            
            if figure_canvas_agg1 is not None:
                delete_fig_agg(figure_canvas_agg1)
            figure_canvas_agg1 = draw_figure(window['-FIG0-'].TKCanvas, fig_3D_ZT_rk) 
            
            if event=='Save':
                window7.hide()
                window8=make_window8()
            
    if window==window8:
        if event== sg.WIN_CLOSED : # if user closes window close the programm
            window8.close()
            break
        
        else:
            
            
            path_txt=values['-IN_txt_path-']
            title_model=values['-IN_txt_model']
            title_part=values['-IN_txt_part']
            title_txt=values['-IN_txt_file-']
            
            # if title_txt=='DBMD' or title_text=='DBMP':
            #     #save eta,delta,TE quantities
            # if title_txt=='SBMP':
            #     #save eta,ZT,TE quantities
            
            path_to_file= path_txt + title_model + title_part + title_txt + '.txt'
            
            if event=='Save txt':
            #create a new txt file on the desired path
                with open(path_to_file, 'w') as f:
                    print('ok')
                    
                    if title_model=='DBMD':
                        if title_part=='1':
                            delta=np.arange(delta_min,delta_max,delta_st)
                            eta=np.arange(eta_min,eta_max,eta_st)
                            f.write('r$_k$='+str(rk)+'\n')
                            f.write('$\delta$'+','+'$\eta$'+','+'$\sigma$'+'S'+'$\kappa_e$'+'ZT'+"\n")
                            f.write('\n')
                            for i in range(delta.size):
                                for j in range(eta.size):
                                    f.write(str(delta[i])+','+str(eta[j])+','+str(sigma_DBMD(delta[i],eta[j]))+','+str(S_DBMD(delta[i],eta[j]))+','+str(ke_DBMD(delta[i],eta[j]))+','+str(ZT_DBMD(delta[i],eta[j],1))+ "\n")
                            f.close()
                            print('done')
                        
                        elif title_part=='2':
                            rk1=np.arange(rk_min,rk_max,rk_step)
                            delta1=np.linspace(0.002,15,npoint)
                            f.write('$r_k$'+','+'$\delta$'+','+'ZT$_{max}$'+"\n")
                            f.write('\n')
                            for i in range(rk1.size):
                                
                                for j in range(delta1.size):
                                    
                                    f.write(str(rk1[i])+','+str(delta1[j])+','+str(ZTmax[j][i])+ "\n")
                            f.close()
                            
                    
                    if title_model=='DBMP':
                        if title_part=='1':
                            delta=np.arange(delta_min,delta_max,delta_st)
                            eta=np.arange(eta_min,eta_max,eta_st)
                            f.write('r$_k$='+str(rk)+'\n')
                            f.write('$\delta$'+','+'$\eta$'+','+'$\sigma$'+'S'+'$\kappa_e$'+'ZT'+"\n")
                            f.write('\n')
                            for i in range(delta.size):
                                for j in range(eta.size):
                                    f.write(str(delta[i])+','+str(eta[j])+','+str(sigma_DBMP(delta[i],eta[j]))+','+str(S_DBMP(delta[i],eta[j]))+','+str(ke_DBMP(delta[i],eta[j]))+','+str(ZT_DBMP(delta[i],eta[j],1))+ "\n")
                            f.close()
                            print('done')
                        if title_part=='2':
                            rk1=np.arange(rk_min,rk_max,rk_step)
                            delta1=np.linspace(0.002,15,npoint)
                            f.write('$r_k$'+','+'$\delta$'+','+'ZT$_{max}$'+"\n")
                            f.write('\n')
                            for i in range(rk1.size):
                                for j in range(delta1.size):
                                    f.write(str(rk1[i])+','+str(delta1[j])+','+str(ZTmax[j][i])+ "\n")
                            f.close()
                            
                            
                    if title_model=='SBMP':
                        if title_part=='1':
                            eta=np.arange(eta_min,eta_max,eta_st)
                            f.write('r$_k$='+str(rk)+'\n')
                            f.write('$\eta$'+','+'$\sigma$'+'S'+'$\kappa_e$'+'ZT'+"\n")
                            f.write('\n')
                            for j in range(eta.size):
                                f.write(str(eta[j])+','+str(sigma_SBMP(eta[j]))+','+str(S_SBMP(eta[j]))+','+str(ke_SBMP(eta[j]))+','+str(ZT_SBMP(eta[j],1))+ "\n")
                            f.close()
                            
                        if title_part=='2':
                            eta=np.linspace(-10,10,npoint)
                            rk=np.arange(rk_min,rk_max,rk_step)
                            f.write('$\eta$'+','+'r$_k$'+'ZT'+"\n")
                            f.write('\n')
                            for i in range(eta.size):
                                for j in range(rk.size):
                                    f.write(str(eta[i])+','+str(rk[j])+','+str(ZT_SBMP(eta[i],1))+ "\n")
                            f.close()
            
            elif event=='Done':
                if title_model=='DBMD':
                    if title_part=='1':
                        window8.close()
                        window2.un_hide()
                    if title_part=='2':
                        window8.close()
                        window5.un_hide()
                if title_model=='DBMP':
                    if title_part=='1':
                        window8.close()
                        window3.un_hide()
                    if title_part=='2':
                        window8.close()
                        window6.un_hide()
                if title_model=='SBMP':
                    if title_part=='1':
                        window8.close()
                        window4.un_hide()
                    if title_part=='2':
                        window8.close()
                        window7.un_hide()
                    

    

window.close()    
    