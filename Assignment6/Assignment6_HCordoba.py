# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

R=["R_outside","R1","R2","R3","R4","R5","R_inside"]
Material= ["outsideSurfaceWinter","woodLappedSiding","glass fiber insulation","woodStud_90mm","woodFiberBoard","gypsum","insideSurface"]
Type=["conv","cond","cond","cond","cond","cond","conv"]
Length=[None,0.013,0.09,0.09,0.013,0.013,None]
Resistance_RValues=[0.03,0.14,0.70,0.63,0.23,0.079,0.12]

listoflists=[Type,Material,Length]
resistanceDataframe=pd.DataFrame(listoflists, index=["Type","Material","Length"],columns= R)


def epsilonEffective(epsilon1, epsilon2):
    result=1/(1/epsilon1+1/epsilon2-1)
    return result
epsilon=epsilonEffective(0.05,0.9)

AirGapResDict={0.02:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
    0.04:{0.03:0.63,0.05:0.59,0.5:0.25}}
RAirGap=AirGapResDict[0.02][epsilon]
 
def RValue_material(Material):
    ThermalResDict= { 
                    "woodStud_90mm":{"R":0.63, "length":0.09},
                    "woodFiberBoard":{"R":0.23, "length":0.013},
                    "woodLappedSiding":{"R":0.14, "length":0.013},
                    "insideSurface":{"R":0.12},
                    "outsideSurfaceWinter":{ "R":0.03},
                    "gypsum":{"R":0.079, "length":0.013},
                    "glass fiber insulation" : {"R":0.7, "length":0.025}
                    }
    RValue_thismaterial = ThermalResDict[Material]["R"]
    return RValue_thismaterial
    
def standardlength(Material):
    ThermalResDict= { 
                    "woodStud_90mm":{"R":0.63, "length":0.09},
                    "woodFiberBoard":{"R":0.23, "length":0.013},
                    "woodLappedSiding":{"R":0.14, "length":0.013},
                    "insideSurface":{"R":0.12},
                    "outsideSurfaceWinter":{ "R":0.03},
                    "gypsum":{"R":0.079, "length":0.013},
                    "glass fiber insulation" : {"R":0.7, "length":0.025}
                    }
    standardlengththismaterial = ThermalResDict[Material]["length"]
    return standardlengththismaterial



RVAlue_material =resistanceDataframe.loc["Material",:].apply(RValue_material)
StandardLength_Material = resistanceDataframe.loc["Material",:][resistanceDataframe.loc["Type",:] == "cond"].apply(standardlength)
RVAlue_Correctedmaterial = RVAlue_material
RVAlue_Correctedmaterial[resistanceDataframe.loc["Type",:] == "cond"] = RVAlue_Correctedmaterial[resistanceDataframe.loc["Type",:]  == "cond"]*resistanceDataframe.loc["Length",:][resistanceDataframe.loc["Type",:] == "cond"] /StandardLength_Material
resistanceDataframe.loc["Rvalue",:]=RVAlue_Correctedmaterial
resistanceDataframe.transpose()

Rtot_woodraw=resistanceDataframe.loc["Rvalue"][resistanceDataframe.loc["Material"] != "glass fiber insulation"].sum()
Rtot_insulationraw=resistanceDataframe.loc["Rvalue"][resistanceDataframe.loc["Material"] != "woodStud_90mm"].sum()

#Now I am going to add the air gap
Rtotinsulation= Rtot_insulationraw + RAirGap
Rtotwood= Rtot_woodraw + RAirGap


U_insulation= 1/(Rtotinsulation)
U_wood= 1/(Rtotwood)
A_insulation=0.75
A_wood=0.25

U_total= U_insulation*A_insulation + (U_wood*A_wood)#This is the second answer
R_total= 1/U_total  #This is the first answer
print("The Total resistance for the problem is " + str(R_total))
print("The Total U for the problem is " + str(U_total))
#Now we have the area that is not covered by glazin

A_noglazing= 0.8*2.5*50

#We have the temperature difference

delta_t= 24

#Now we can determine the rate of heat loss through the walls

Q_total= U_total*A_noglazing*delta_t

print("the rate of heat loss through the walls " + str(Q_total))




            
            
                     
              
