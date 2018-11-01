# -*- coding: utf-8 -*-
#
import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()


Tin=22       #Temperature in the inside
Tout=-2     #Temperature in the outside
A=50*2.5*0.8 #Portion of area made by wall
A_wood=A*0.25 
A_fiber=A*0.75
                                                                                                                                                                                
R1={"name":"Outside Air","type":"conv","A":A}
R2={"name":"Wood Bevel Lapped Siding","type":"cond","l":0.013,"area":A}
R3={"name":"Wood Fiberboard","type":"cond","l":0.013,"area":A}
R4={"name":"Glass Fiber Insulation","type":"cond","l":0.09,"area":A}
R5={"name":"Wood Stud","type":"cond","l":0.9,"area":A}
R6={"name":"Gypsum","type":"cond","l":0.013,"area":A}
R7={"name":"Inside Air","type":"conv","area":A}
R_gap={"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

resistancesListWithWood=[R1,R2,R_gap,R3,R5,R6,R7]
resistanceListFiberGlass=[R1,R2,R_gap,R3,R4,R6,R7]
                                              
import os
os.getcwd()
os.chdir(r"C:\Users\Giulia\Documents\Pyton")                      


import WallFunctions_GiuliaSora  
resultsWood=WallFunctions_GiuliaSora.resistanceFunction(resistancesListWithWood)
resultsFiberGlass=WallFunctions_GiuliaSora.resistanceFunction(resistanceListFiberGlass)
                                                                                                            
ueQ=WallFunctions_GiuliaSora.Utot(Tin,Tout,A,resultsWood[0],resultsFiberGlass[0])

print ("La U totale è: "+str(ueQ[0]))
print ("La Q totale è: "+str(ueQ[1]))



#Other way to call the functions
from WallFunctions_GiuliaSora import resistanceFunction,Utot
ResultsWood=resistanceFunction(resistancesListWithWood)
ResultsFiberGlass=resistanceFunction(resistanceListFiberGlass)
UeQ=Utot(Tin,Tout,A,ResultsWood[0],ResultsFiberGlass[0])

print ("La U totale è: "+str(UeQ[0]))
print ("La Q totale è: "+str(UeQ[1]))