#Printing the working directory.
import sys
import os
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()  
#Importing the modules we need.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
#Importing all the functions to calculate heat loads due to windows, internal gains, opaque surfaces and latent loads and to find psychrometric data.
import fenestration_functions as func
import IntGains_Inf_Vent_DistrLosses as iv
import FunctionsOpaque as funcOp
import psySI as SI
import latent_functions as lat

#Weather input of Piacenza.
inputs_DF = pd.read_csv("input_weather_Piacenza.csv",sep=";",index_col=0)
inputs_list = func.weather_data_calculator(inputs_DF)

#Input data.
numericalDataDF = pd.read_csv("input_numerical_data.csv",sep=";",index_col= 0)  
dataDF = pd.read_csv("input_data.csv",sep=";",index_col= 0)     
materials_DataFrame = pd.read_csv("resistences_materials.csv",sep=";",index_col= 1)

#Fenestration surfaces calculations.
windows_DF = pd.read_csv("input_fenestration.csv",sep=";",index_col=0) 
windows_DF["Area"] = windows_DF["Height"]*windows_DF["Width"]

#For winter.
inputWalls_DataFrame_winter = pd.read_csv("input_data_walls_winter.csv",sep=";",index_col= 0)
inputDoor_DataFrame_winter = pd.read_csv("input_data_door_winter.csv",sep=";",index_col= 0)
#Calculating the heat transfer coefficients for opaque surfaces in winter.
U_wall_winter = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winter,materials_DataFrame)  
U_door_winter = funcOp.Utot_door_Calculator(inputDoor_DataFrame_winter,materials_DataFrame)  
U_ceiling_winter = numericalDataDF["value"]["U_ceiling"]
#Calculating the heating load due to the opaque surfaces.
QtotOpaque_winter = funcOp.QtotOpaque_winter_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_winter,numericalDataDF["value"]["U_ceiling"],U_door_winter,inputs_list["deltaTheating"])
opaque_DataFrame = pd.read_csv("opaque_DataFrame_modified.csv",sep=",",index_col= 0)
Walls_w = opaque_DataFrame["Q_winter"]["Walls"]
Ceiling_w = opaque_DataFrame["Q_winter"]["Ceiling"]
Doors_w = opaque_DataFrame["Q_winter"]["Doors"]
#Calculating the heating load due to the windows.
Qfen_heating_load = func.Qfen_heating_calculator(windows_DF,inputs_list)
windows_DF["Qheating"]

#For summer.
inputWalls_DataFrame_summer = pd.read_csv("input_data_walls_summer.csv",sep=";",index_col= 0)
inputDoor_DataFrame_summer = pd.read_csv("input_data_door_summer.csv",sep=";",index_col= 0) 
#Calculating the heat transfer coefficients for opaque surfaces in summer.
U_wall_summer = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summer,materials_DataFrame)  
U_door_summer = funcOp.Utot_door_Calculator(inputDoor_DataFrame_summer,materials_DataFrame)  
U_ceiling_summer = numericalDataDF["value"]["U_ceiling"]
#Calculating the cooling load due to the opaque surfaces.
QtotOpaque_summer = funcOp.QtotOpaque_summer_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_summer,numericalDataDF["value"]["U_ceiling"],U_door_summer,dataDF["characteristic"]["colour_roof"],dataDF["characteristic"]["material_roof"],inputs_list["deltaTcooling"],inputs_list["DRcooling"],dataDF["characteristic"]["walls_surface_type"],dataDF["characteristic"]["ceiling_surface_type"],dataDF["characteristic"]["doors_surface_type"])
opaque_DataFrame = pd.read_csv("opaque_DataFrame_modified.csv",sep=",",index_col= 0)
Walls_s = opaque_DataFrame["Qsummer"]["Walls"]
Ceiling_s = opaque_DataFrame["Qsummer"]["Ceiling"]
Doors_s = opaque_DataFrame["Qsummer"]["Doors"]
#Calculating the cooling load due to the windows.
Qfen_cooling_load = func.Qfen_cooling_calculator(windows_DF,inputs_list)
windows_DF["Qcooling"]
#Infiltration, ventilation and distribution losses calculations.
input_data_inf_vent = pd.read_csv("input_inf_vent.csv",sep = ";",index_col=0) 
Output_Inf_Vent = iv.inf_vent_load_calc(input_data_inf_vent)
input_data_distribution = pd.read_csv("input_distribution.csv",sep = ";",index_col=0) 
Losses = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_load,Qfen_cooling_load,QtotOpaque_winter,QtotOpaque_summer,Output_Inf_Vent.iloc[7][0],Output_Inf_Vent.iloc[6][0],Output_Inf_Vent.iloc[8][0])
    
#Latent result.
QtotLatent = lat.Qtot_latent (input_data_inf_vent, inputs_list)

#Final result.
results_DF = pd.read_csv("results_empty.csv",sep=";",index_col=0)     
results_DF["Heating"] = [QtotOpaque_winter,Qfen_heating_load,0,0,Output_Inf_Vent.iloc[7][0],Losses.iloc[0][0],0,0]
results_DF["Cooling"] = [QtotOpaque_summer,Qfen_cooling_load,0,Output_Inf_Vent.iloc[8][0],Output_Inf_Vent.iloc[6][0],Losses.iloc[1][0],0,QtotLatent]
for column in results_DF.columns.tolist():
        sensible_loads = pd.Series(results_DF[column][0:6])     
        results_DF[column]["Q_sensible_tot"] = sensible_loads.sum()       
print(results_DF)
#Now we show graphically the results. First for winter.
plt.figure()
plt.subplot(2,1,1)
labs = ['Walls','Ceiling','Doors','Windows']
cols = ["b","maroon","goldenrod","g"]
slices = [Walls_w, Ceiling_w, Doors_w, Qfen_heating_load]
plt.pie(slices, labels = labs, colors = cols,
        startangle = 90, shadow = True, explode = (0,0,0,0.1),
        autopct="%1.1f%%"
        )    
plt.title("Opaque surfaces VS Windows in winter!")
plt.show()
#Now we plot the shares of heating load between different exposures.
plt.subplot(2,1,2)
labs = ['East','West','South fixed','South operable']
cols = ["b","maroon","goldenrod","g"]
slices = [windows_DF["Qheating"]["East"], windows_DF["Qheating"]["West"], windows_DF["Qheating"]["South fixed"], windows_DF["Qheating"]["South operable"]]
plt.pie(slices, labels = labs, colors = cols,
        startangle = 90, shadow = True, 
        autopct="%1.1f%%"
        )    
plt.title("Windows different exposures' shares in winter!")
plt.show()

#Now for summer.
plt.figure()
plt.subplot(2,1,1)
labs = ['Walls','Ceiling','Doors','Windows']
cols = ["b","maroon","goldenrod","g"]
slices = [Walls_s, Ceiling_s, Doors_s, Qfen_cooling_load]
plt.pie(slices, labels = labs, colors = cols,
        startangle = 90, shadow = True, explode = (0,0,0,0.1),
        autopct="%1.1f%%"
        )    
plt.title("Opaque surfaces VS Windows in summer!")
plt.show()
#Now we plot the shares of heating load between different exposures.
plt.subplot(2,1,2)
labs = ['East','West','South fixed','South operable']
cols = ["b","maroon","goldenrod","g"]
slices = [windows_DF["Qcooling"]["East"], windows_DF["Qcooling"]["West"], windows_DF["Qcooling"]["South fixed"], windows_DF["Qcooling"]["South operable"]]
plt.pie(slices, labels = labs, colors = cols,
        startangle = 90, shadow = True, 
        autopct="%1.1f%%"
        )    
plt.title("Windows different exposures' shares in summer!")
plt.show()



