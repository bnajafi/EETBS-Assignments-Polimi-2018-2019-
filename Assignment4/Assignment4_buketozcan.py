import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

Atot=100
Awood=25
Ains=75
DeltaT=24

R_1= {"name":"Outside surface", "type":"conv", "material":"outsideSurfaceWinter"}
R_2= {"name":"Wood bevel lapped siding", "type":"cond", "material":"woodLappedSiding","length":0.013}
R_3= {"name":"Wood FiberBoard", "type":"cond", "material":"woodFiberBoard","length":0.013}
R_4= {"name":"Glass Fiber Insulation", "type":"cond", "material":"glassFiberInsulation","length":0.09}
R_5= {"name":"Wood stud", "type":"cond", "material":"woodStud_90mm","length":0.09}
R_6= {"name":"Gypsum WallBoard", "type":"cond", "material":"Gypsum","length":0.013}
R_7= {"name":"Inside surface", "type":"conv", "material":"insideSurface"}
R_gap={"name":"air-gap", "type":"gap", "epsilon1":0.05, "epsilon2":0.9,"length":0.020}

ResistanceList_withWood=[R_1,R_2,R_3,R_5,R_6,R_7,R_gap]
ResistanceList_withInsulation=[R_1,R_2,R_3,R_4,R_6,R_7,R_gap]

import os 
currentDirectory=os.getcwd()
os.chdir(r"/Users/apple/Desktop/POLIMI LESSONS/Energy/Assignments")

import WallFunctions_buketozcan
os.chdir(currentDirectory)

import WallFunctions_buketozcan as wallF

ResultDictWood=wallF.ResistanceOfLayersInSeries(ResistanceList_withWood)
Rtot_withWood1 = ResultDictWood["Rtot"]

ResultDictInsulation=wallF.ResistanceOfLayersInSeries(ResistanceList_withInsulation)
Rtot_withInsulation1 = ResultDictInsulation["Rtot"]

Uwood1=1/float(Rtot_withWood1)
Uins1=1/float(Rtot_withInsulation1)
Utot1=(Uwood1*(float(Awood)/Atot))+(Uins1*(float(Ains)/Atot))
Rtot1=1/float(Utot1)
Qtot1=Utot1*Atot*DeltaT
print("R total is "+str(Rtot1)+" m2.degC/W")
print("U overall is "+str(Utot1)+" W/m2.degC")
print("Q total is "+str(Qtot1)+" W")

#the second way; 
from WallFunctions_buketozcan import *

ResultDictWood2=ResistanceOfLayersInSeries(ResistanceList_withWood)
Rtot_withWood2 = ResultDictWood2["Rtot"]
ResultDictInsulation2=ResistanceOfLayersInSeries(ResistanceList_withInsulation)
Rtot_withInsulation2 = ResultDictInsulation2["Rtot"]


Uwood2=1/float(Rtot_withWood2)
Uins2=1/float(Rtot_withInsulation2)
Utot2=(Uwood2*(float(Awood)/Atot))+(Uins2*(float(Ains)/Atot))
Rtot2=1/float(Utot2)
Qtot2=Utot2*Atot*DeltaT
print("R total is "+str(Rtot2)+" m2.degC/W")
print("U overall is "+str(Utot2)+" W/m2.degC")
print("Q total is "+str(Qtot2)+" W")