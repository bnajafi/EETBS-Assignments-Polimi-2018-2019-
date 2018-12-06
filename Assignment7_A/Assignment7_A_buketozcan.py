import os
os.chdir(r"/Users/apple/Desktop/EETBS-Assignments-Polimi-2018-2019-/Assignment7_A/ExampleAssignments_fromPreviousYear/example1_assignment8")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

#importing all the functions to calculate heat loads via fenestrations, internalgains ,psychrometric data, opaque parts and latent loads
import fenestration_functions as func
import IntGains_Inf_Vent_DistrLosses as iv
import FunctionsOpaque as funcOp
import psySI as SI
import latent_functions as lat

#Weather Inputs of Piacenza:

inputs_DF = pd.read_csv("input_weather_Piacenza.csv",sep=";",index_col=0)
inputs_list = func.weather_data_calculator(inputs_DF)

    
def solverr(wallwinter,wallsummer,Windows):
    # Opaque surfaces Calculation:
    numericalDataDF = pd.read_csv("input_numerical_data.csv",sep=";",index_col= 0)   #numerical
    dataDF = pd.read_csv("input_data.csv",sep=";",index_col= 0)     #string
    materials_DataFrame = pd.read_csv("resistences_materials.csv",sep=";",index_col= 1)   #materials and resistances
    inputWalls_DataFrame_winter = pd.read_csv(wallwinter,sep=";",index_col= 0)# reading the wallwinter data
    inputWalls_DataFrame_summer = pd.read_csv(wallsummer,sep=";",index_col= 0)# reading the wallsummer data
    inputDoor_DataFrame_winter = pd.read_csv("input_data_door_winter.csv",sep=";",index_col= 0)# reading the doorwinter data
    inputDoor_DataFrame_summer = pd.read_csv("input_data_door_summer.csv",sep=";",index_col= 0)# reading the doorsummer data
    #calling functions to calculate wall and door loads
    U_wall_winter = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_winter,materials_DataFrame)  
    U_wall_summer = funcOp.Utot_wall_Calculator(inputWalls_DataFrame_summer,materials_DataFrame)  
    U_door_winter = funcOp.Utot_door_Calculator(inputDoor_DataFrame_winter,materials_DataFrame)  
    U_door_summer = funcOp.Utot_door_Calculator(inputDoor_DataFrame_summer,materials_DataFrame)  
    
    #printing the Heating and Cooling loads of the opaque elements of the building
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
    windows_DF = pd.read_csv(Windows,sep=";",index_col=0) #reading fenestration data file
    windows_DF["Area"] = windows_DF["Height"]*windows_DF["Width"] #calculating areas of all the windows
    
    Qfen_heating_load = func.Qfen_heating_calculator(windows_DF,inputs_list)#calling function to calculate fenestration heating load
    print 'The total amount of the heating load for the windows is '+str(Qfen_heating_load)+' W.'
    Qfen_cooling_load = func.Qfen_cooling_calculator(windows_DF,inputs_list)#calling function to calculate fenestration cooling load
    print 'The total amount of the cooling load for the windows is '+str(Qfen_cooling_load)+' W.'
    
    
    #Infiltration, Ventilation and Distribution losses Calculation:
    input_data_inf_vent = pd.read_csv("input_inf_vent.csv",sep = ";",index_col=0) #importing infiltration and ventilation data
    Output_Inf_Vent = iv.inf_vent_load_calc(input_data_inf_vent)
    
    input_data_distribution = pd.read_csv("input_distribution.csv",sep = ";",index_col=0)  #input data for read the distribution table
    Losses = iv.Q_distri_Losses(input_data_distribution,Qfen_heating_load,Qfen_cooling_load,QtotOpaque_winter,QtotOpaque_summer,Output_Inf_Vent.iloc[7][0],Output_Inf_Vent.iloc[6][0],Output_Inf_Vent.iloc[8][0])
    
    #Latent results
    QtotLatent = lat.Qtot_latent (input_data_inf_vent, inputs_list)
    
    #Final Results
    results_DF = pd.read_csv("results_empty.csv",sep=";",index_col=0)     #put all the results in a data frame
    results_DF["Heating"] = [QtotOpaque_winter,Qfen_heating_load,0,0,Output_Inf_Vent.iloc[7][0],Losses.iloc[0][0],0,0]
    #calculated values of the loads are arranged in dataframes
    results_DF["Cooling"] = [QtotOpaque_summer,Qfen_cooling_load,0,Output_Inf_Vent.iloc[8][0],Output_Inf_Vent.iloc[6][0],Losses.iloc[1][0],0,QtotLatent]
    for column in results_DF.columns.tolist():
        sensible_loads = pd.Series(results_DF[column][0:6])     #6 not included
        results_DF[column]["Q_sensible_tot"] = sensible_loads.sum() #sum of all sensible and put it in the table
   
    #results_DF.to_csv("results_wholeRFL.csv",sep =";")
    
    
    
    
    print "\nThis is the value of sensible internal gain: "+str(Output_Inf_Vent["Results"]["Internal Gain, sensible [W]"])+" W."
    print "This is the value of sensible infiltration-ventilation Cooling load: "+str(Output_Inf_Vent["Results"]["Sensible Infiltration/Ventilation Cooling Load [W]"])+" W."
    print "This is the value of sensible infiltration-ventilation Heating load: "+str(Output_Inf_Vent["Results"]["Sensible Infiltration/Ventilation Heating Load [W]"])+" W.\n"    
    print "This is the value of Heating distribution losses: "+str(Losses["Results"]["Heating distribution losses"])+" W."
    print "This is the value of Cooling distribution losses: "+str(Losses["Results"]["Cooling distribution losses"])+" W.\n" 
    print "\t\t\t So the total Sensible Heating Load is :"+str(results_DF["Heating"]["Q_sensible_tot"])+" W."      
    print "\t\t\t So the total Sensible Cooling Load is :"+str(results_DF["Cooling"]["Q_sensible_tot"])+" W.\n"      
    print "Here is given a table with all the results:\n"
    print results_DF
    return results_DF

#function to form a piechart for all different variations of wall and fens data (parametric analysis)
def piecharts(parameter1,parameter2,parameter3):
    labels=['opaque','windows','below','internalgain','infilventilation','distloss']
    cols=["b","maroon","goldenrod","g","r","slateblue"]
    x=parameter1[parameter2]
    y=x[0:6]
    plt.figure()
    plt.pie(y,labels=labels,colors=cols,startangle=90,explode=(0.1,0.1,0.1,0.1,0.1,0.1), autopct='%1.1f%%')
    plt.title(str(parameter2)+" load of "+ parameter3)
    plt.show()

#function to form a bar chart to compare the loads of the base case with that of the parametric variations    
def barcharts(parameter1,parameter2,parameter3,parameter4,modifier1,modifier2):
    items = [1,2,3]
    types = ["Base",modifier1,modifier2]
    plt.figure()
    plt.bar(items,[A[parameter1][parameter2],parameter3[parameter1][parameter2],parameter4[parameter1][parameter2]],color=["goldenrod","fuchsia","cyan"])
    plt.xticks(items,types,color="k")
    plt.title("Variation of "+parameter1+parameter2+" because of "+ modifier1+"  "+modifier2)
    plt.show()
    
#CALLING THE MAIN FUNCTION TO CALCULATE THE LOADS FOR THE BASE CASE AND THE VARIATIONAL CASES IN WALL DATA AND WINDOWS DATA (PARAMETRIC ANALYSIS)
#PIE CHARTS ARE DRAWN FOR EVERY SINGLE CASE TO FIND THE CONTRIBUTION OF EACH ELEMENT IN THE BUILDING
#FOR BOTH HEATING AND COOLING LOADS
##BAR CHARTS ARE DRAWN TO COMPARE THE BASE CASE LOADS WITH THE WALL VARIATION AND THE WINDOWS VARIATIONS SEPERATELY  
A=solverr("input_data_walls_winter.csv","input_data_walls_summer.csv","input_fenestration.csv")
piecharts(A,"Heating","base")
piecharts(A,"Cooling","base")


B=solverr("input_data_walls_winter--.csv","input_data_walls_summer--.csv","input_fenestration.csv")
piecharts(B,"Heating","wall--")
piecharts(B,"Cooling","wall--")


C=solverr("input_data_walls_winter++.csv","input_data_walls_summer++.csv","input_fenestration.csv")
piecharts(C,"Heating","wall++")
piecharts(C,"Cooling","wall++")
barcharts("Heating","Q_sensible_tot",B,C,"wall--","wall++")
barcharts("Cooling","Q_sensible_tot",B,C,"wall--","wall++")
#barcharts("Cooling","Q_latent",B,C,"wall--","wall++")

D=solverr("input_data_walls_winter.csv","input_data_walls_summer.csv","input_fenestration_1.csv")
piecharts(D,"Heating","fen1")
piecharts(D,"Cooling","fen1")


E=solverr("input_data_walls_winter.csv","input_data_walls_summer.csv","input_fenestration_2.csv")
piecharts(E,"Heating","fen2")
piecharts(E,"Cooling","fen2")
barcharts("Heating","Q_sensible_tot",D,E,"fen1","fen2")
barcharts("Cooling","Q_sensible_tot",D,E,"fen1","fen2")
#barcharts("Cooling","Q_latent",D,E,"fen1","fen2")