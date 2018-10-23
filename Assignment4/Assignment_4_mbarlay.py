#Assignment 4

import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import os 
currentDirectory=os.getcwd()
os.chdir(r"C:\Users\My\Desktop\Laurea Magistrale\ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS\Energy and environmental tech for building systems\Polimi-Asssignments")

import Assignment_4_wallfunctions_mbarlay
os.chdir(currentDirectory)

#first way: using from .. import command.

from Assignment_4_wallfunctions_mbarlay import *

resistanceOfLayersInSeries(ResistanceList_withWood)
Rtot_wood = ResultsDictionary["Rtot"]
resistanceOfLayersInSeries(ResistanceList_withInsulation)
Rtot_insulation = ResultsDictionary["Rtot"]

U_wood = 1/float(Rtot_wood)
U_ins = 1/float(Rtot_insulation)
U_tot = (U_wood*(float(A_wood)/A_tot))+(U_ins*(float(A_ins)/A_tot))
R_total = 1/float(U_tot)
Q_tot = U_tot*A_tot*delta_T

print("R overall is: "+str(R_total)+"m2.degC/W")
print("U overall is: "+str(U_tot)+"W/(m^2C)")
print("Q total is "+str(Q_tot)+"W")

#second way: using import .. as .. command.

import Assignment_4_wallfunctions_mbarlay as wallFunc
resultDictWood = wallFunc.resistanceOfLayersInSeries(ResistanceList_withWood)
Rtot_wood1 = wallFunc.Rtot_wood
resultDictInsulation = wallFunc.resistanceOfLayersInSeries(ResistanceList_withInsulation)
Rtot_insulation1 = wallFunc.Rtot_insulation

U_wood1 = 1/float(Rtot_wood1)
U_ins1 = 1/float(Rtot_insulation1)
U_tot1 = (U_wood1*(float(A_wood)/A_tot))+(U_ins1*(float(A_ins)/A_tot))
R_total1 = 1/float(U_tot1)
Q_tot1 = U_tot1*A_tot*delta_T

print("R overall is: "+str(R_total)+"m2.degC/W")
print("U overall is: "+str(U_tot)+"W/(m^2C)")
print("Q total is "+str(Q_tot)+"W")

