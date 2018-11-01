#first method                        
import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import os   

os.chdir("C:\Users\Alessia\Documents\Primo_anno_en\Building\Assignment4")
import wallfunctions_Romanelli as wallf
R_1={"name":"outside surface","type":"conv","material":"outsidesurfaceWinter"}
R_2={"name":"wood bevel lapped siding","type":"cond","material":"woodLappedSiding","length":0.013}
R_3={"name":"fiberboard","type":"cond","material":"woodFiberBoard","length":0.013}
R_4a={"name":"glass fiber insulation","type":"cond","material":"glassfiber","length":0.09}
R_4b={"name":"wood stud","type":"cond","material":"WoodStud_90mm","length":0.09}
R_5={"name":"Gypsum Wallboard","type":"cond","material":"gypsum","length":0.013}
R_6={"name":"inside surface","type":"conv","material":"insideSurface"}
R_gap={"name":"air gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}


ResistenceList_withWood=[R_1,R_2,R_3,R_gap,R_4b,R_5,R_6] 
ResistenceList_withInsulation=[R_1,R_2,R_3,R_4a,R_5,R_6,R_gap]

ResistenceWithWood=wallf.ResistenceWithWood(ResistenceList_withWood)
ResistenceWithIns=wallf.ResistenceWithIns(ResistenceList_withInsulation)


A=50*0.8*2.5
DeltaT=24

U_wood=1/wallf.ResistenceWithWood (ResistenceList_withWood)["Rtot_wood"]
U_ins= 1/wallf.ResistenceWithIns(ResistenceList_withInsulation)["Rtot_ins"]

print("The heat  transfer  coefficient with wood is "+ str(U_wood)+ "W/degC" )
print("The heat  transfer  coefficient with insulation is "+ str(U_ins)+ "W/degC" )


U_tot=U_wood*0.25+U_ins*0.75

print("The overall  heat  transfer  coefficient  is "+ str(U_tot)+ "W/degC" )

R_tot=1/U_tot

print("The overall  unit  thermal  resistance is "+ str(R_tot)+ "degC/W" )

Q=U_tot*A*DeltaT

print("The rate  of  heat  loss  through  the  walls is "+str(Q)+ "W")



import os
 
FolderOfMyWallCalculation="C:\Users\Alessia\Documents\Primo_anno_en\Building\Assignment4"
os.chdir(FolderOfMyWallCalculation)

from wallfunctions_Romanelli import *

ResistenceWithWood=ResistenceWithWood (ResistenceList_withWood)["Rtot_wood"]
ResistenceWithIns=ResistenceWithIns(ResistenceList_withInsulation)["Rtot_ins"]

               
A=50*0.8*2.5
DeltaT=24

U_wood=1/ResistenceWithWood 
U_ins= 1/ResistenceWithIns
print("The heat  transfer  coefficient with wood is "+ str(U_wood)+ "W/degC" )
print("The heat  transfer  coefficient with insulation is "+ str(U_ins)+ "W/degC" )


U_tot=U_wood*0.25+U_ins*0.75

print("The overall  heat  transfer  coefficient  is "+ str(U_tot)+ "W/degC" )

R_tot=1/U_tot

print("The overall  unit  thermal  resistance is "+ str(R_tot)+ "degC/W" )

Q=U_tot*A*DeltaT

print("The rate  of  heat  loss  through  the  walls is "+str(Q)+ "W")

                                                       
        
        
        


