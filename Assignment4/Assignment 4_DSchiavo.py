R_1={"Name":"Gypsum","type":"Cond","Material":"Gypsum","Length":0.013}
R_2={"Name":"Wood bevel lapped siding","type":"Cond","Material":"Wood bevel lapped siding","Length":0.013}
R_3={"Name":"Glass Fiber Insulation","type":"Cond","Material":"Glass Fiber Insulation","Length":0.090}
R_4={"Name":"Wood studs","type":"Cond","Material":"Wood studs","Length":0.090}
R_5={"Name":"fiberboard","type":"Cond","Material":"fiberboard","Length":0.013}
R_o={"Name":"OutsideSurfaceWinter","type":"Conv","Material":"OutsideSurfaceWinter"}
R_i={"Name":"inside surface","type":"Conv","Material":"InsideSurface"}
R_gap={"Name":"Gap","type":"gap","epsilon1":0.05, "epsilon2":0.9, "length":0.020}
ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i,R_gap]

ResistanceList_insulation=[R_1,R_2,R_3,R_5,R_o,R_i,R_gap]
ResistanceList=[ResistanceList_wood,ResistanceList_insulation]     

import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import WallFunction_DSchiavo as DanieleSchiavo

R= DanieleSchiavo.resistanceoflayer(ResistanceList)

A=50*0.8*2.5
DT=24

R_wood=R[0]["R_tot"]
R_insulation=R[1]["R_tot"]
U_wood=1/R_wood
U_insulation=1/R_insulation
print("The heat transfer coefficient, considering the wood studs is ")
print(str(U_wood)+ "  W/m^2")   
print("The heat transfer coefficient, considering the glass fiber insulation is ")
print(str(U_insulation)+ "  W/m^2")  
U_tot=U_wood*0.25+U_insulation*0.75
print("The OVERALL heat transfer coefficient, is")
print(str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
print("The OVERALL resistance is ")
print(str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DT
print("The OVERALL heat tranfer is ")
print(str(Q_tot)+ "  W")