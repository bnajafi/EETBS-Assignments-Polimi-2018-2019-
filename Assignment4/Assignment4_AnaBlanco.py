#ASSIGNMENT 4 (Example 1 Unit 1.2):
#Calculate Overall unit thermal resistance (Rtotal) and overall heat transfer coefficient (Utotal)


#1st way of importing data: import wallFunctions as nickname

import os
import sys
thisFileDirectory = os.path.dirname(sys.argv[0])
os.chdir(thisFileDirectory)
print os.getcwd()

R_i={"name":"inside surface", "type":"conv", "material":"InsideSurface"}
R_2={"name":"Wood bevel lapped Siding", "type":"cond", "material":"WoodLappedSiding", "length":0.013}
R_3={"name":"Wood fiberboard", "type":"cond", "material":"WoodFiberBoard", "length":0.013}
R_4={"name":"Glass fiber insulation", "type":"cond", "material":"GlassFiberInsulation", "length":0.09}
R_5={"name":"Wood studs", "type":"cond", "material":"WoodStud_90mm", "length":0.09}          
R_6={"name":"Gypsum Wallboard","type":"cond", "material":"Gypsum", "length":0.013}
R_o={"name":"Outside surface", "type":"conv", "material":"OutsideSurface"}
R_gap={"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.02}

ResistanceList_withWood=[R_i,R_2,R_3,R_5,R_6,R_o,R_gap]
ResistanceList_withInsulation=[R_i,R_2,R_3,R_4,R_6,R_o,R_gap]

import wallFunctions_AnaBlanco as Ana


myResistanceOfWall_Wood=Ana.ResistanceOfWall_wood(ResistanceList_withWood)
R_wood=myResistanceOfWall_Wood["Rtot_withWood"]
myResistanceOfWall_Insulation=Ana.ResistanceOfWall_insulation(ResistanceList_withInsulation)
R_insulation=myResistanceOfWall_Insulation["Rtot_withInsulation"]

U_wood=1/R_wood
U_insulation=1/R_insulation

Utotal=0.25*U_wood+0.75*U_insulation
print("The total heat transfer coefficient is Utotal= "+str(Utotal))
Rtotal=1/Utotal
print("The total thermal resistance is Rtotal= "+str(Rtotal))

#Rate of heat loss through the walls
Area=50*2.5*0.8
T_1=22
T_2=-2
Q=Utotal*Area*(T_1-T_2)
print("The rate of heat loss through the walls is Q= "+str(Q))

#2nd way of importing data: from wallFunctions import functions
import wallFunctions_AnaBlanco
from wallFunctions_AnaBlanco import *

myResistanceOfWall_Wood2=wallFunctions_AnaBlanco.ResistanceOfWall_wood(ResistanceList_withWood)

R_wood2 = myResistanceOfWall_Wood2["Rtot_withWood"]
myResistanceOfWall_Insulation2=wallFunctions_AnaBlanco.ResistanceOfWall_insulation(ResistanceList_withInsulation)
R_insulation2=myResistanceOfWall_Insulation2["Rtot_withInsulation"]

U_wood2=1/R_wood2
U_insulation2=1/R_insulation2

Utotal2=0.25*U_wood2+0.75*U_insulation2
print("The total heat transfer coefficient is Utotal= "+str(Utotal2))
Rtotal2=1/Utotal2
print("The total thermal resistance is Rtotal= "+str(Rtotal2))

#Rate of heat loss through the walls
Area=50*2.5*0.8
T_1=22
T_2=-2
Q2=Utotal2*Area*(T_1-T_2)
print("The rate of heat loss through the walls is Q= "+str(Q2))