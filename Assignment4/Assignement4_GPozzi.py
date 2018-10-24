
Rgyp={"name":"Gypsum Wallboard", "material":"gypsum", "length":0.013, "type":"cond"}
Rwood={"name":"wood bevel lapped siding", "material":"woodLappedSiding", "length":0.013, "type":"cond"}
Rin={"name":"inside surface", "material":"insideSurface", "type":"conv"}
Rfib={"name":"fiberboard", "material":"woodFiberBoard", "length":0.013, "type":"cond"}
Rins={"name":"insulation", "material":"glassfiber", "length":0.09, "type":"cond"}
Rstud={"name":"wood stud", "material":"woodStud", "length":0.09, "type":"cond"}
RoutS={"name":"Summer Out", "material":"outsideSurfaceSummer", "type":"conv"}
RoutW={"name":"Winter Out", "material":"outsideSurfaceWinter", "type":"conv"}
R_gap={"name":"Gap","type":"gap","epsilon1":0.9, "epsilon2":0.9, "length":0.020}

ResistanceList_withWood=[Rin, Rgyp, Rwood, Rfib, R_gap, Rstud,RoutW]
ResistanceList_withIns=[Rin, Rgyp, Rwood, Rfib,R_gap, Rins, RoutW]

ResistanceList=[ResistanceList_withWood,ResistanceList_withIns]

import os
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import WallFunction_GPozzi as Gilberto

R= Gilberto.resistanceoflayer(ResistanceList)

DT=24
A=2.5*50*0.8

R_wood=R[0]["R_tot"]
R_ins=R[1]["R_tot"]
U_wood=1/R_wood
U_ins=1/R_ins

U_tot=U_wood*0.25+U_ins*0.75
R_tot=1/U_tot

Q_tot=U_tot*A*DT

print("U with wood studs: " + str(U_wood)+ "  W/(m^2K)")
print("") 
print("U with glass fiber insulation: " + str(U_ins)+ "  W/m^K2")
print("")
print("U_tot: "+ str(U_tot)+ "  W/m^2K")
print("")
print("Rtot: " + str(R_tot)+ " m^2*K/W")
print("")

print("The OVERALL HEAT TRANSFER RATE is:  Q_tot = " + str(Q_tot)+ "  W")

print("")
print("________________________________________________________")
print("")

from WallFunction_GPozzi import resistanceoflayer

R1= resistanceoflayer(ResistanceList)

R_wood=R1[0]["R_tot"]
R_ins=R1[1]["R_tot"]
U_wood=1/R_wood
U_ins=1/R_ins

U_tot=U_wood*0.25+U_ins*0.75
R_tot=1/U_tot

Q_tot=U_tot*A*DT

print("U with wood studs: " + str(U_wood)+ "  W/(m^2K)")
print("") 
print("U with glass fiber insulation: " + str(U_ins)+ "  W/m^K2")
print("")
print("U_tot: "+ str(U_tot)+ "  W/m^2K")
print("")
print("Rtot: " + str(R_tot)+ " m^2*K/W")
print("")

print("The OVERALL HEAT TRANSFER RATE is:  Q_tot = " + str(Q_tot)+ "  W")