
import numpy as np

A=50*0.8*2.5
DT=24


names_R_wood= np.array(["InsideSurface","WoodbevelLappedSiding","WoodStuds","fiberboard","Gypsum","OutsideSurfaceWinter"])
names_R_insulation= np.array(["InsideSurface","WoodbevelLappedSiding","GlassFiberInsulation","fiberboard","Gypsum","OutsideSurfaceWinter"])
lengths_inLibrary_with_wood=np.array([1,0.013,0.090,0.013,0.013,1])
lengths_inLibrary_with_ins=np.array([1,0.013,0.013,0.25,0.013,1])
lengths_wall_with_ins=np.array([1,0.013,0.013,0.90,0.013,1])
lengths_wall_with_wood=np.array([1,0.013,0.090,0.013,0.013,1])


typeR=np.array(["conv","cond","cond","cond","cond","conv"])
Resistances_cond_wood=np.array([None,0.14,0.63,0.23,0.079,None])
Resistances_cond_insulation=np.array([None,0.14,0.23,0.7,0.079,None])
ResistanceA=np.array([A,A,A,A,A])
Resistanceh=np.array([0.12,None,None,None,None,0.03])

Rcond_with_wood=np.array(np.zeros(6))
Rcond_with_wood[typeR=="cond"]=Resistances_cond_wood[typeR=="cond"]

Rcond_with_ins=np.array(np.zeros(6))
Rcond_with_ins[typeR=="cond"]=Resistances_cond_insulation[typeR=="cond"]

R_conv=np.array(np.zeros(6))


length_coeff_ins=lengths_wall_with_ins/lengths_inLibrary_with_ins
Resistances_cond_ins=length_coeff_ins*Rcond_with_ins

length_coeff_wood=lengths_wall_with_wood/lengths_inLibrary_with_wood
Resistances_cond_wood=length_coeff_wood*Rcond_with_wood

R_conv[typeR=="conv"]=Resistanceh[typeR=="conv"]


Rtot_wood=Resistances_cond_wood.sum()+R_conv.sum()
Rtot_insulation=Resistances_cond_ins.sum()+R_conv.sum()

U_wood=1/Rtot_wood
U_insulation=1/Rtot_insulation  
print("The heat transfer coefficient of layers in series with the wood stud is " + str(U_wood)+ "  W/m^2K")
print("")   
print("The heat transfer coefficient of layers in series with the insulation is "+str(U_insulation)+ "  W/m^2K")
print("") 
 
U_tot=U_wood*0.25+U_insulation*0.75

print("The OVERALL heat transfer coefficient, is "+str(U_tot)+ "  W/m^2K")
print("")

R_Tot=1/U_tot

print("The OVERALL resistance is " + str(R_Tot)+ " K*m^2/W")
print("")

Q_tot=U_tot*A*DT

print("The OVERALL heat tranfer is: ")
print(str(Q_tot)+ "  W")