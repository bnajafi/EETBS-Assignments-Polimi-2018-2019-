# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os
import sys
#In this way you should be able to see where also the Excel file I'm using is. Use RUN for this time.
thisFileDirectory = os.path.dirname(sys.argv[0])
os.chdir(thisFileDirectory)
print os.getcwd()

#I'm taking from an Excel file the characteristics of the resistances I've to work with,
DF_Input = pd.read_excel("InputData_Ferrari.xlsx")

#I'm calculating the effective epsilon of an air gap with eps1=0.9, eps2=0.1 and width of 40 mm.
def epsilonEffective(epsilon1=0.9,epsilon2=0.9):
    """This is a function that, given two input values for epsilon1 and epsilon2, returns the 
    corresponding epsilon effective."""
    result = 1/(1/epsilon1+1/epsilon2 -1)
    return result
Eps_Eff = epsilonEffective(0.9,0.1)

#What follows (from row 24 to row 37 ), I've found it in the Web and it's necessary to interpolate the value  
#of the resistance of the air gap.
from bisect import bisect_left
class Interpolate(object):
    def __init__(self, x_list, y_list):
        if any([y - x <= 0 for x, y in zip(x_list, x_list[1:])]):
            raise ValueError("x_list must be in strictly ascending order!")
        x_list = self.x_list = map(float, x_list)
        y_list = self.y_list = map(float, y_list)
        intervals = zip(x_list, x_list[1:], y_list, y_list[1:])
        self.slopes = [(y2 - y1)/(x2 - x1) for x1, x2, y1, y2 in intervals]
    def __getitem__(self, x):
        i = bisect_left(self.x_list, x) - 1
        return self.y_list[i] + self.slopes[i] * (x - self.x_list[i])
i = Interpolate([0.03,0.05,0.5],[0.063,0.59,0.25])
Rgap = i[Eps_Eff]

def RVAlue_Material(inputMaterial):
    """This is a function which, for each input material, returns the value of the resistance for that material given 
    a certain reference length."""
    ThermalResDict = {"GlassFiberInsulation":{"R":0.7, "length":0.025},
    "WoodStud_90mm":{"R":0.63, "length":0.09},
    "InsideSurface":{"R":0.12},
    "OutsideSurfaceWinter":{"R":0.03},
    "Gypsum":{"R":0.079,"length":0.013},
    "WoodLappedSiding":{"R":0.14,"length":0.013},
    "WoodFiberboard":{"R":0.23,"length":0.013},
    }
    RValue_ThisMaterial = ThermalResDict[inputMaterial]["R"]
    return RValue_ThisMaterial

def StandardLength_Material(inputMaterial):
    """This is a function which, for each input material, returns the value of the standard length for which a 
    certain value of resistance is reported."""
    ThermalResDict = {"GlassFiberInsulation":{"R":0.7, "length":0.025},
    "WoodStud_90mm":{"R":0.63, "length":0.09},
    "InsideSurface":{"R":0.12},
    "OutsideSurfaceWinter":{"R":0.03},
    "Gypsum":{"R":0.079,"length":0.013},
    "WoodLappedSiding":{"R":0.14,"length":0.013},
    "WoodFiberboard":{"R":0.23,"length":0.013},
    }
    StandardLength_ThisMaterial = ThermalResDict[inputMaterial]["length"]
    return StandardLength_ThisMaterial

RVAlue_R_Raw = DF_Input.loc[:,"Material"].apply(RVAlue_Material)
StandardLength_Material = DF_Input.loc[:,"Material"][DF_Input.loc[:,"type"] == "cond"].apply(StandardLength_Material)
RVAlue_R_Corrected = RVAlue_R_Raw
RVAlue_R_Corrected[DF_Input.loc[:,"type"] == "cond"] = RVAlue_R_Corrected[DF_Input.loc[:,"type"] == "cond"]*DF_Input.loc[:,"length"][DF_Input.loc[:,"type"] == "cond"]/StandardLength_Material
DF_Input.loc[:,"Rvalue"] = RVAlue_R_Corrected

#I'm updating the Excel file with the correct values of resistances.
DF_Input.to_excel("InputData_Ferrari.xlsx")

#It's time to calculate the total resistance of the wall in the two different cases.   
RTot_Wood = sum(DF_Input.loc[:,"Rvalue"][DF_Input.loc[:,"Material"] != "GlassFiberInsulation"]) + Rgap
RTot_Insulation = sum(DF_Input.loc[:,"Rvalue"][DF_Input.loc[:,"Material"] != "WoodStud_90mm"]) + Rgap

def HeatTransferCoefficient(R):
    """This is a function which takes the value of a resistance and simply gives the corresponding heat
    transfer coefficient value."""
    U = 1/R
    return U
UWood = HeatTransferCoefficient(RTot_Wood)
UInsulation = HeatTransferCoefficient(RTot_Insulation)

UWall = UWood*0.25 + UInsulation*0.75
RWall = 1/UWall

T_IN = 22
T_OUT = -2
DT = (T_IN - T_OUT)
A = 50*(1-0.2)*2.5
Q = UWall*A*DT

#Printing the results.
print ("The overall heat transfer coefficient of the wall is: " + str(UWall) + " W/(m^2°C)")
print ("The overall thermal resistance of the wall is " + str(RWall) + " (m^2°C)/W")
print ("The heat flux through the wall is " + str(Q) + " W")