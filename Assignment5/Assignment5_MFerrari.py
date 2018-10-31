# -*- coding: utf-8 -*-
import numpy as np
#Definition of the different arrays I'll use in this script
Resistance_Names = np.array(["R_Out","R_WoodBevel","R_FiberBoard","R_GlassFiber","R_WoodStud","R_Gypsum","R_In"])
Resistance_Types = np.array(["conv","cond","cond","cond","cond","cond","conv"])
Resistance_Length = np.array([None,0.013,0.013,0.09,0.09,0.013,None])
Resistance_R = np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])
Reference_Length = np.array([None,0.013,0.013,0.025,0.09,0.013,None])
#Case for the wall without considering the insulation
Resistances_RvaluesWood = np.array(zeros(7))
Condition1 = (Resistance_Types == "cond") & (Resistance_Names != "R_GlassFiber")
Resistances_RvaluesWood[Resistance_Types == "conv"] = Resistance_R[Resistance_Types == "conv"]
Resistances_RvaluesWood[Condition1] = Resistance_R[Condition1]/Reference_Length[Condition1]*Resistance_Length[Condition1]
RtotWood = Resistances_RvaluesWood.sum()
#Case for the wall considering the insulation
Resistances_RvaluesInsulation = np.array(zeros(7))
Condition2 = (Resistance_Types == "cond") & (Resistance_Names != "R_WoodStud")
Resistances_RvaluesInsulation[Resistance_Types == "conv"] = Resistance_R[Resistance_Types == "conv"]
Resistances_RvaluesInsulation[Condition2] = Resistance_R[Condition2]/Reference_Length[Condition2]*Resistance_Length[Condition2]
RtotInsulation = Resistances_RvaluesInsulation.sum()
#Calculation of the corresponding heat trasnfer coefficient
UWood = 1.0/RtotWood
UInsulation = 1.0/RtotInsulation
#Calculation of the combined heat transfer coefficient through the wall
UWall = UWood*0.25 + UInsulation*0.75
RWall = 1.0/UWall
#Definition of the data of the problem
T_IN = 22
T_OUT = -2
DT = (T_IN - T_OUT)
A = 50*(1-0.2)*2.5
Q = UWall*A*DT
#Print the results
print ("The thermal resistance of the wall, without considering insulation is : " + str(RtotWood) + " (m^2°C)/W")
print ("The thermal resistance of the wall, considering insulation is : " + str(RtotInsulation) + " (m^2°C)/W")
print ("The overall heat transfer coefficient of the wall is: " + str(UWall) + " W/(m^2°C)")
print ("The overall heat transfer coefficient of the wall is: " + str(UWall) + " W/(m^2°C)")
print ("The overall thermal resistance of the wall is " + str(RWall) + " (m^2°C)/W")
print ("The heat flux through the wall is " + str(Q) + " W")