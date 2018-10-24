# -*- coding: utf-8 -*-
import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory) 
print os.getcwd() 

# first way
import os
#os.chdir("/Users/federicarossetti/Desktop/RES/1 semestre/building systems/Assignement/Assignment 4")
import WallFunctions_FRossetti as WallF

R_1={"Name":"Gypsum","type":"Cond","Material":"Gypsum","Length":0.013}
R_2={"Name":"Wood bevel lapped siding","type":"Cond","Material":"Wood bevel lapped siding","Length":0.013}
R_3={"Name":"Glass Fiber Ins","type":"Cond","Material":"Glass Fiber Ins","Length":0.090}
R_4={"Name":"Wood studs","type":"Cond","Material":"Wood studs","Length":0.090}
R_5={"Name":"fiberboard","type":"Cond","Material":"fiberboard","Length":0.013}
R_o={"Name":"OutsideSurfaceWinter","type":"Conv","Material":"OutsideSurfaceWinter"}
R_i={"Name":"inside surface","type":"Conv","Material":"InsideSurface"}
R_gap ={"name":"air-Gap","type":"Gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i,R_gap] 
ResistanceList_ins=[R_1,R_2,R_3,R_5,R_o,R_i,R_gap] 

print("The total Resistance considering the wood studs is "+str(WallF.TotalResistances(ResistanceList_wood)))
print("The total Resistance considering insulation is "+str(WallF.TotalResistances(ResistanceList_ins)))

U_wood=1/WallF.TotalResistances (ResistanceList_wood)["R_tot"]
U_ins=1/WallF.TotalResistances (ResistanceList_ins)["R_tot"]  
print("The heat transfer coefficient, considering the wood is " + str(U_wood)+ "  W/m^2")  
print("The heat transfer coefficient, considering the insulation is "+str(U_ins)+ "  W/m^2")
U_tot=U_wood*0.25+U_ins*0.75
print("The overall heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
A=50*0.8*2.5
DeltaT=24
print("The overall resistance is "+str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DeltaT
print("The overall heat tranfer is "+str(Q_tot)+ " W")


# second way

import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory) 
print os.getcwd() 

import os
#os.chdir("/Users/federicarossetti/Desktop/RES/1 semestre/building systems/Assignement/Assignment 4")
from WallFunctions_FRossetti import *


ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i,R_gap] 
ResistanceList_ins=[R_1,R_2,R_3,R_5,R_o,R_i,R_gap] 
print(ThermalConRes)

print("The total Resistance considering the wood studs is "+str(TotalResistances (ResistanceList_wood)))
print("The total Resistance considering ins is "+str(TotalResistances (ResistanceList_ins)))

U_wood=1/TotalResistances (ResistanceList_wood)["R_tot"]
U_ins=1/TotalResistances (ResistanceList_ins)["R_tot"]  
print("The heat transfer coefficient, considering the wood is " + str(U_wood)+ "  W/m^2")  
print("The heat transfer coefficient, considering the insulation is "+str(U_ins)+ "  W/m^2")
U_tot=U_wood*0.25+U_ins*0.75
print("The overall heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
A=50*0.8*2.5
DeltaT=24
print("The overall resistance is "+str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DeltaT
print("The overall heat tranfer is "+str(Q_tot)+ "  W")

