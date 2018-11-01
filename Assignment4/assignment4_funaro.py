#assignment4
#funaro_eleonora


import os
import sys
CurrentDirectory=os.path.dirname(sys.argv[0])
os.chdir(CurrentDirectory) 
print os.getcwd()
FolderOfMyWallCalculation=r"C:\Users\Nora\Documents\Piacenza\Building systems\Python"

Awood=0.25
Ainsulation=0.75
Atot=100 
dT=24

R_1 = {"name":"glass fiber","type":"cond","material":"glass_fiber", "length":0.09}
R_2 = {"name":"wood stud","type":"cond","material":"woodStud_90mm", "length":0.09}
R_3 = {"name":"wood fiber board","type":"cond","material":"woodFiberBoard", "length":0.013}
R_4 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}
R_5 = {"name":"gypsum wallboard","type":"cond","material":"gypsum", "length":0.013}
R_i = {"name":"inside surface","type":"conv","material":"insideSurface"}
R_o = {"name":"outside surface","type":"conv","material":"outsideSurface"}
R_gap = {"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

ResistanceList_withWood = [R_2,R_3,R_4,R_5,R_i,R_o,R_gap]
ResistanceList_withInsulation = [R_1,R_3,R_4,R_5,R_i,R_o,R_gap]




#Resolution of the problem using the first way

import WallFunction_funaro as wallF
ResultWood=wallF.ResistanceOfLayersInSeries(ResistanceList_withWood)
ResultInsulation=wallF.ResistanceOfLayersInSeries(ResistanceList_withInsulation)

DictWood=ResultWood
Rwood=DictWood['Rtot']
print("R Wood: " +str(Rwood))

DictGlass=ResultInsulation
Rinsulation=DictGlass['Rtot']
print("R Insulation: " +str(Rinsulation))


Uinsulation=1/Rinsulation
Uwood=1/Rwood
Utot=(Uinsulation*Ainsulation)+(Uwood*Awood)
RTot=1/Utot

print("R Tot: " +str(RTot))

Q=(Atot*dT)/RTot
        
print("Q: " +str(Q)) 


#Resolution of the problem using the second way

from WallFunction_funaro import ResistanceOfLayersInSeries
ResultW=ResistanceOfLayersInSeries(ResistanceList_withWood)
ResultI=ResistanceOfLayersInSeries(ResistanceList_withInsulation)

DictW=ResultW
Rw=DictW['Rtot']
print("R Wood: " +str(Rw))

DictG=ResultI
Ri=DictG['Rtot']
print("R Insulation: " +str(Ri))


Ui=1/Ri
Uw=1/Rw
UTot=(Ui*Ainsulation)+(Uw*Awood)
Rtot=1/UTot

print("R Tot: " +str(Rtot))

Qtot=(Atot*dT)/Rtot
        
print("Q: " +str(Qtot)) 
