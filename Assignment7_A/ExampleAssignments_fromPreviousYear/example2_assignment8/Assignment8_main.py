import sys
import os
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

#importing all functions:
import fenestration_functions as func
import IntGains_Inf_Vent_DistrLosses as iv
import FunctionsOpaque as funcOp
import psySI as SI
import latent_functions as lat

#Weather Inputs:
inputs_DF = pd.read_csv("input_weather_Piacenza.csv",sep=";",index_col=0)
inputs_list = func.weather_data_calculator(inputs_DF)   #deltaT, DR, latitude calculation


#BASECASE:
#WALL: wood_bevel, wood_fiber, com_brick, glass_fiber (70%), wood_stud_2.4 (30%), gypsum
#WINDOWS: 5c, wood frame, DrapesLightOpen, Fcl 0,4
#Type of construction: average

# Opaque surfaces Calculation:
numericalDataDF = pd.read_csv("input_numerical_data.csv",sep=";",index_col= 0)   #numerical data(Uceiling, dimensions)
dataDF = pd.read_csv("input_data.csv",sep=";",index_col= 0)     #string
materials_DataFrame = pd.read_csv("resistences_materials.csv",sep=";",index_col= 1)             #materials and resistances
inputWalls_DataFrame_winter = pd.read_csv("input_data_walls_winter.csv",sep=";",index_col= 0)   #layers of wall winter case
inputWalls_DataFrame_summer = pd.read_csv("input_data_walls_summer.csv",sep=";",index_col= 0)   #layers of wall summer case
inputDoor_DataFrame_winter = pd.read_csv("input_data_door_winter.csv",sep=";",index_col= 0)     #layers of door winter case
inputDoor_DataFrame_summer = pd.read_csv("input_data_door_summer.csv",sep=";",index_col= 0)     #layers of door summer case
    
U_wall_winter = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winter,materials_DataFrame)    #calculation of U wall winter
U_wall_summer = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summer,materials_DataFrame)    #calculation of U wall summer  
U_door_winter = funcOp.Utot_door_Calculator(inputDoor_DataFrame_winter,materials_DataFrame)     #calculation of U door winter
U_door_summer = funcOp.Utot_door_Calculator(inputDoor_DataFrame_summer,materials_DataFrame)     #calculation of U door summer

print "\nThis is the value of Uwall_winter: " + str(U_wall_winter) + "  W/(m^2 * K)"
print "This is the value of Udoor_winter: " + str(U_door_winter)+ "  W/(m^2 * K)"
print "This is the value of Uceiling: " + str(numericalDataDF["value"]["U_ceiling"]) + "  W/(m^2 * K)"
QtotOpaque_winter = funcOp.QtotOpaque_winter_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_winter,numericalDataDF["value"]["U_ceiling"],U_door_winter,inputs_list["deltaTheating"])
print "\tThis is the opaque heating load: " + str(QtotOpaque_winter) + " W\n"

print "\nThis is the value of Uwall_summer: " + str(U_wall_summer) + "  W/(m^2 * K)"
print "This is the value of Udoor_summer: " + str(U_door_summer) + "  W/(m^2 * K)"
print "This is the value of Uceiling: " + str(numericalDataDF["value"]["U_ceiling"]) + "  W/(m^2 * K)"
QtotOpaque_summer = funcOp.QtotOpaque_summer_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_summer,numericalDataDF["value"]["U_ceiling"],U_door_summer,dataDF["characteristic"]["colour_roof"],dataDF["characteristic"]["material_roof"],inputs_list["deltaTcooling"],inputs_list["DRcooling"],dataDF["characteristic"]["walls_surface_type"],dataDF["characteristic"]["ceiling_surface_type"],dataDF["characteristic"]["doors_surface_type"])
print "\tThis is the opaque cooling load: " + str(QtotOpaque_summer) + " W\n"


#Fenestration surfaces Calculation:
windows_DF = pd.read_csv("input_fenestration.csv",sep=";",index_col=0)    #windows description
windows_DF["Area"] = windows_DF["Height"]*windows_DF["Width"]             #windows area calculation

Qfen_heating_load = func.Qfen_heating_calculator(windows_DF,inputs_list)  #Q window heating
print 'The total amount of the heating load for the windows is '+str(Qfen_heating_load)+' W.'
Qfen_cooling_load = func.Qfen_cooling_calculator(windows_DF,inputs_list)  #Q window cooling
print 'The total amount of the cooling load for the windows is '+str(Qfen_cooling_load)+' W.'


#Infiltration, Ventilation and Distribution losses Calculation:
input_data_inf_vent = pd.read_csv("input_inf_vent.csv",sep = ";",index_col=0)
Output_Inf_Vent = iv.inf_vent_load_calc(input_data_inf_vent)

input_data_distribution = pd.read_csv("input_distribution.csv",sep = ";",index_col=0)  #input data to read from the distribution table
Losses = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_load,Qfen_cooling_load,QtotOpaque_winter,QtotOpaque_summer,Output_Inf_Vent.iloc[7][0],Output_Inf_Vent.iloc[6][0],Output_Inf_Vent.iloc[8][0])

#Latent results
QtotLatent = lat.Qtot_latent (input_data_inf_vent, inputs_list)

#Final Results
results_DF = pd.read_csv("results_empty.csv",sep=";",index_col=0)     #put all the results in a data frame
results_DF["Heating"] = [QtotOpaque_winter,Qfen_heating_load,0,0,Output_Inf_Vent.iloc[7][0],Losses.iloc[0][0],0,0]
results_DF["Cooling"] = [QtotOpaque_summer,Qfen_cooling_load,0,Output_Inf_Vent.iloc[8][0],Output_Inf_Vent.iloc[6][0],Losses.iloc[1][0],0,QtotLatent]
for column in results_DF.columns.tolist():
    sensible_loads = pd.Series(results_DF[column][0:6])
    results_DF[column]["Q_sensible_tot"] = sensible_loads.sum() #total sensible heat
print "Here is given a table with all the results:\n"
print results_DF   
    
    
#WORST CASE (--)
#WALL: wood_bevel, wood_fiber, com_brick, concrete_heavyweight (70%), wood_stud_2.4 (30%), gypsum
#WINDOWS: 1a, Aluminium frame, RollerDarkOpaque, Fcl 0,3
#Type of construction: leaky
    
# Opaque surfaces Calculation:
inputWalls_DataFrame_winterWorst = pd.read_csv("input_data_walls_winter--.csv",sep=";",index_col= 0)   #layers of wall winter case
inputWalls_DataFrame_summerWorst = pd.read_csv("input_data_walls_summer--.csv",sep=";",index_col= 0)   #layers of wall summer case
    
U_wall_winterWorst = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winterWorst,materials_DataFrame)    #calculation of U wall winter
U_wall_summerWorst = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summerWorst,materials_DataFrame)    #calculation of U wall summer  

print "\nThis is the value of Uwall_winter (--): " + str(U_wall_winterWorst) + "  W/(m^2 * K)"
QtotOpaque_winterWorst = funcOp.QtotOpaque_winter_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_winterWorst,numericalDataDF["value"]["U_ceiling"],U_door_winter,inputs_list["deltaTheating"])
print "\tThis is the opaque heating load (--): " + str(QtotOpaque_winterWorst) + " W\n"

print "\nThis is the value of Uwall_summer (--): " + str(U_wall_summerWorst) + "  W/(m^2 * K)"
QtotOpaque_summerWorst = funcOp.QtotOpaque_summer_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_summerWorst,numericalDataDF["value"]["U_ceiling"],U_door_summer,dataDF["characteristic"]["colour_roof"],dataDF["characteristic"]["material_roof"],inputs_list["deltaTcooling"],inputs_list["DRcooling"],dataDF["characteristic"]["walls_surface_type"],dataDF["characteristic"]["ceiling_surface_type"],dataDF["characteristic"]["doors_surface_type"])
print "\tThis is the opaque cooling load (--): " + str(QtotOpaque_summerWorst) + " W\n"


#Fenestration surfaces Calculation:
windows_DFWorst = pd.read_csv("input_fenestration_1.csv",sep=";",index_col=0)    #windows description
windows_DFWorst["Area"] = windows_DFWorst["Height"]*windows_DFWorst["Width"]             #windows area calculation

Qfen_heating_loadWorst = func.Qfen_heating_calculator(windows_DFWorst,inputs_list)  #Q window heating
print 'The total amount of the heating load for the windows (--) is '+str(Qfen_heating_loadWorst)+' W.'
Qfen_cooling_loadWorst = func.Qfen_cooling_calculator(windows_DFWorst,inputs_list)  #Q window cooling
print 'The total amount of the cooling load for the windows (--) is '+str(Qfen_cooling_loadWorst)+' W.'


#Infiltration, Ventilation and Distribution losses Calculation:
input_data_inf_ventWorst = pd.read_csv("input_inf_vent_1.csv",sep = ";",index_col=0)
Output_Inf_VentWorst = iv.inf_vent_load_calc(input_data_inf_ventWorst)

LossesWorst = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_loadWorst,Qfen_cooling_loadWorst,QtotOpaque_winterWorst,QtotOpaque_summerWorst,Output_Inf_VentWorst.iloc[7][0],Output_Inf_VentWorst.iloc[6][0],Output_Inf_VentWorst.iloc[8][0])

#Latent results
QtotLatentWorst = lat.Qtot_latent (input_data_inf_ventWorst, inputs_list)

#Final Results
results_DFWorst = pd.read_csv("results_empty.csv",sep=";",index_col=0)     #put all the results in a data frame
results_DFWorst["Heating"] = [QtotOpaque_winterWorst,Qfen_heating_loadWorst,0,0,Output_Inf_VentWorst.iloc[7][0],LossesWorst.iloc[0][0],0,0]
results_DFWorst["Cooling"] = [QtotOpaque_summerWorst,Qfen_cooling_loadWorst,0,Output_Inf_VentWorst.iloc[8][0],Output_Inf_VentWorst.iloc[6][0],LossesWorst.iloc[1][0],0,QtotLatentWorst]
for column in results_DFWorst.columns.tolist():
    sensible_loads = pd.Series(results_DFWorst[column][0:6])
    results_DFWorst[column]["Q_sensible_tot"] = sensible_loads.sum() #total sensible heat
print results_DFWorst


#BETTER CASE (+)
#WALL: wood_bevel, wood_fiber, com_brick, mineral_fiber (80%), wood_stud_2.4 (20%), air_space_40, gypsum
#WINDOWS: 17c, Insulated Fiberglass/Vinyl frame, DrapesLightClosed, Fcl 0,6
#Type of construction: average

# Opaque surfaces Calculation:
inputWalls_DataFrame_winterBetter = pd.read_csv("input_data_walls_winter+.csv",sep=";",index_col= 0)   #layers of wall winter case
inputWalls_DataFrame_summerBetter = pd.read_csv("input_data_walls_summer+.csv",sep=";",index_col= 0)   #layers of wall summer case
    
U_wall_winterBetter = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winterBetter,materials_DataFrame)    #calculation of U wall winter
U_wall_summerBetter = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summerBetter,materials_DataFrame)    #calculation of U wall summer  

print "\nThis is the value of Uwall_winter (+): " + str(U_wall_winterBetter) + "  W/(m^2 * K)"
QtotOpaque_winterBetter = funcOp.QtotOpaque_winter_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_winterBetter,numericalDataDF["value"]["U_ceiling"],U_door_winter,inputs_list["deltaTheating"])
print "\tThis is the opaque heating load (+): " + str(QtotOpaque_winterBetter) + " W\n"

print "\nThis is the value of Uwall_summer (+): " + str(U_wall_summerBetter) + "  W/(m^2 * K)"
QtotOpaque_summerBetter = funcOp.QtotOpaque_summer_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_summerBetter,numericalDataDF["value"]["U_ceiling"],U_door_summer,dataDF["characteristic"]["colour_roof"],dataDF["characteristic"]["material_roof"],inputs_list["deltaTcooling"],inputs_list["DRcooling"],dataDF["characteristic"]["walls_surface_type"],dataDF["characteristic"]["ceiling_surface_type"],dataDF["characteristic"]["doors_surface_type"])
print "\tThis is the opaque cooling load (+): " + str(QtotOpaque_summerBetter) + " W\n"


#Fenestration surfaces Calculation:
windows_DFBetter = pd.read_csv("input_fenestration_3.csv",sep=";",index_col=0)    #windows description
windows_DFBetter["Area"] = windows_DFBetter["Height"]*windows_DFBetter["Width"]             #windows area calculation

Qfen_heating_loadBetter = func.Qfen_heating_calculator(windows_DFBetter,inputs_list)  #Q window heating
print 'The total amount of the heating load for the windows (+) is '+str(Qfen_heating_loadBetter)+' W.'
Qfen_cooling_loadBetter = func.Qfen_cooling_calculator(windows_DFBetter,inputs_list)  #Q window cooling
print 'The total amount of the cooling load for the windows (+) is '+str(Qfen_cooling_loadBetter)+' W.'


#Infiltration, Ventilation and Distribution losses Calculation:
input_data_inf_ventBetter = pd.read_csv("input_inf_vent.csv",sep = ";",index_col=0)
Output_Inf_VentBetter = iv.inf_vent_load_calc(input_data_inf_ventBetter)

LossesBetter = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_loadBetter,Qfen_cooling_loadBetter,QtotOpaque_winterBetter,QtotOpaque_summerBetter,Output_Inf_VentBetter.iloc[7][0],Output_Inf_VentBetter.iloc[6][0],Output_Inf_VentBetter.iloc[8][0])

#Latent results
QtotLatentBetter = lat.Qtot_latent (input_data_inf_ventBetter, inputs_list)

#Final Results
results_DFBetter = pd.read_csv("results_empty.csv",sep=";",index_col=0)     #put all the results in a data frame
results_DFBetter["Heating"] = [QtotOpaque_winterBetter,Qfen_heating_loadBetter,0,0,Output_Inf_VentBetter.iloc[7][0],LossesBetter.iloc[0][0],0,0]
results_DFBetter["Cooling"] = [QtotOpaque_summerBetter,Qfen_cooling_loadBetter,0,Output_Inf_VentBetter.iloc[8][0],Output_Inf_VentBetter.iloc[6][0],LossesBetter.iloc[1][0],0,QtotLatentBetter]
for column in results_DFBetter.columns.tolist():
    sensible_loads = pd.Series(results_DFBetter[column][0:6])
    results_DFBetter[column]["Q_sensible_tot"] = sensible_loads.sum() #total sensible heat
print results_DFWorst


#BEST CASE (++)
#WALL: wood_bevel, wood_fiber, com_brick, urethane (80%), wood_stud_2.4 (20%), air_space_90, gypsum
#WINDOWS: 25a, Insulated Fiberglass/Vinyl frame, RollerWhiteOpaque, Fcl 0,5
#Type of construction: good

# Opaque surfaces Calculation:
inputWalls_DataFrame_winterBest = pd.read_csv("input_data_walls_winter++.csv",sep=";",index_col= 0)   #layers of wall winter case
inputWalls_DataFrame_summerBest = pd.read_csv("input_data_walls_summer++.csv",sep=";",index_col= 0)   #layers of wall summer case
    
U_wall_winterBest = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winterBest,materials_DataFrame)    #calculation of U wall winter
U_wall_summerBest = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summerBest,materials_DataFrame)    #calculation of U wall summer  

print "\nThis is the value of Uwall_winter (++): " + str(U_wall_winterBest) + "  W/(m^2 * K)"
QtotOpaque_winterBest = funcOp.QtotOpaque_winter_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_winterBest,numericalDataDF["value"]["U_ceiling"],U_door_winter,inputs_list["deltaTheating"])
print "\tThis is the opaque heating load (++): " + str(QtotOpaque_winterBest) + " W\n"

print "\nThis is the value of Uwall_summer (++): " + str(U_wall_summerBest) + "  W/(m^2 * K)"
QtotOpaque_summerBest = funcOp.QtotOpaque_summer_calculator(numericalDataDF["value"]["height_windows"],numericalDataDF["value"]["width_windowsS"],numericalDataDF["value"]["width_windowsE"],numericalDataDF["value"]["width_windowsW"],U_wall_summerBest,numericalDataDF["value"]["U_ceiling"],U_door_summer,dataDF["characteristic"]["colour_roof"],dataDF["characteristic"]["material_roof"],inputs_list["deltaTcooling"],inputs_list["DRcooling"],dataDF["characteristic"]["walls_surface_type"],dataDF["characteristic"]["ceiling_surface_type"],dataDF["characteristic"]["doors_surface_type"])
print "\tThis is the opaque cooling load (++): " + str(QtotOpaque_summerBest) + " W\n"


#Fenestration surfaces Calculation:
windows_DFBest = pd.read_csv("input_fenestration_2.csv",sep=";",index_col=0)    #windows description
windows_DFBest["Area"] = windows_DFBest["Height"]*windows_DFBest["Width"]             #windows area calculation

Qfen_heating_loadBest = func.Qfen_heating_calculator(windows_DFBest,inputs_list)  #Q window heating
print 'The total amount of the heating load for the windows (++) is '+str(Qfen_heating_loadBest)+' W.'
Qfen_cooling_loadBest = func.Qfen_cooling_calculator(windows_DFBest,inputs_list)  #Q window cooling
print 'The total amount of the cooling load for the windows (++) is '+str(Qfen_cooling_loadBest)+' W.'


#Infiltration, Ventilation and Distribution losses Calculation:
input_data_inf_ventBest = pd.read_csv("input_inf_vent_2.csv",sep = ";",index_col=0)
Output_Inf_VentBest = iv.inf_vent_load_calc(input_data_inf_ventBest)

LossesBest = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_loadBest,Qfen_cooling_loadBest,QtotOpaque_winterBest,QtotOpaque_summerBest,Output_Inf_VentBest.iloc[7][0],Output_Inf_VentBest.iloc[6][0],Output_Inf_VentBest.iloc[8][0])

#Latent results
QtotLatentBest = lat.Qtot_latent (input_data_inf_ventBest, inputs_list)

#Final Results
results_DFBest = pd.read_csv("results_empty.csv",sep=";",index_col=0)     #put all the results in a data frame
results_DFBest["Heating"] = [QtotOpaque_winterBest,Qfen_heating_loadBest,0,0,Output_Inf_VentBest.iloc[7][0],LossesBest.iloc[0][0],0,0]
results_DFBest["Cooling"] = [QtotOpaque_summerBest,Qfen_cooling_loadBest,0,Output_Inf_VentBest.iloc[8][0],Output_Inf_VentBest.iloc[6][0],LossesBest.iloc[1][0],0,QtotLatentBest]
for column in results_DFBest.columns.tolist():
    sensible_loads = pd.Series(results_DFBest[column][0:6])
    results_DFBest[column]["Q_sensible_tot"] = sensible_loads.sum() #total sensible heat
print results_DFBest

plt.close('all')
#pie chart for cooling components:
labCool = ["Opaque","Windows","IntGains","Inf&Vent","DistrLosses"]
plt.figure(1)
CoolingLoadValues = np.append(results_DF[0:2]['Cooling'],results_DF[3:6]['Cooling'])
colCool=['yellow',"crimson",'g','darkviolet','b']
plt.pie(CoolingLoadValues,labels=labCool,colors=colCool,startangle=90, autopct='%1.1f%%')
plt.title("Total cooling load")

#pie chart for heating components:
labHeat = ["Opaque","Windows","Inf&Vent","DistrLosses"]
plt.figure(2)
HeatingLoadValues = np.append(results_DF[0:2]['Heating'],results_DF[4:6]['Heating'])
colHeat=['yellow',"crimson",'g','darkviolet']
plt.pie(HeatingLoadValues,labels=labHeat,colors=colHeat,startangle=90, autopct='%1.1f%%')
plt.title("Total heating load")

#Bar charts to compare the base case with the better, best and worst cases:
colCool2=['lightyellow',"palevioletred",'lightgreen','violet','skyblue']
colHeat2=['lightyellow',"palevioletred",'lightgreen','violet']
HeatingLoadValuesWorst = np.append(results_DFWorst[0:2]['Heating'],results_DFWorst[4:6]['Heating'])
plt.figure(3)
itemsCool = [1,2,3,4,5]
itemsHeat = [1,2,3,4]
plt.bar(itemsHeat,HeatingLoadValuesWorst,color=colHeat)
plt.bar(itemsHeat,HeatingLoadValues,color=colHeat2)
plt.xticks(itemsHeat,labHeat,color="grey")
plt.title("Comparison between base case and worst case, heating")

CoolingLoadValuesWorst = np.append(results_DFWorst[0:2]['Cooling'],results_DFWorst[3:6]['Cooling'])
plt.figure(4)
plt.bar(itemsCool,CoolingLoadValuesWorst,color=colCool)
plt.bar(itemsCool,CoolingLoadValues,color=colCool2)
plt.xticks(itemsCool,labCool,color="grey")
plt.title("Comparison between base case and worst case, cooling")

HeatingLoadValuesBetter = np.append(results_DFBetter[0:2]['Heating'],results_DFBetter[4:6]['Heating'])
plt.figure(5)
plt.bar(itemsHeat,HeatingLoadValues,color=colHeat)
plt.bar(itemsHeat,HeatingLoadValuesBetter,color=colHeat2)
plt.xticks(itemsHeat,labHeat,color="grey")
plt.title("Comparison between base case and better case, heating")

CoolingLoadValuesBetter = np.append(results_DFBetter[0:2]['Cooling'],results_DFBetter[3:6]['Cooling'])
plt.figure(6)
plt.bar(itemsCool,CoolingLoadValues,color=colCool)
plt.bar(itemsCool,CoolingLoadValuesBetter,color=colCool2)
plt.xticks(itemsCool,labCool,color="grey")
plt.title("Comparison between base case and better case, cooling")

HeatingLoadValuesBest = np.append(results_DFBest[0:2]['Heating'],results_DFBest[4:6]['Heating'])
plt.figure(7)
plt.bar(itemsHeat,HeatingLoadValues,color=colHeat)
plt.bar(itemsHeat,HeatingLoadValuesBest,color=colHeat2)
plt.xticks(itemsHeat,labHeat,color="grey")
plt.title("Comparison between base case and best case, heating")

CoolingLoadValuesBest = np.append(results_DFBest[0:2]['Cooling'],results_DFBest[3:6]['Cooling'])
plt.figure(8)
plt.bar(itemsCool,CoolingLoadValues,color=colCool)
plt.bar(itemsCool,CoolingLoadValuesBest,color=colCool2)
plt.xticks(itemsCool,labCool,color="grey")
plt.title("Comparison between base case and best case, cooling")

plt.show('all')