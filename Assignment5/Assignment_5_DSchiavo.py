import numpy as np

A=50*0.8*2.5
DT=24

Ri=["R_InsideSurface""Conv",0.12]
R1=["R_Woodbevellappedsiding""Cond",0.14]
R2=["R_Woodstuds""Cond",0.63]
R3=["R_fiberboard""Cond", 0.23]
R4=["R_Glass_Fiber_Insulation""Cond",0.70]
R5=["R_Gypsum""Cond",0.079]
Ro=["R_OutsideSurfaceWinter","Conv",0.03]



namesR_wood= np.array(["R_InsideSurface","R_Woodbevellappedsiding","R_Woodstuds","R_fiberboard","R_Gypsum","R_OutsideSurfaceWinter"])
namesR_insulation= np.array(["R_InsideSurface","R_Woodbevellappedsiding","R_Glass_Fiber_Insulation","R_fiberboard","R_Gypsum","R_OutsideSurfaceWinter"])
length_directory_wood=np.array([1,0.013,0.090,0.013,0.013,1])
length_directory_insulation=np.array([1,0.013,0.013,0.25,0.013,1])
length_wall_insulation=np.array([1,0.013,0.013,0.90,0.013,1])
length_wall_wood=np.array([1,0.013,0.090,0.013,0.013,1])


typeR=np.array(["conv","cond","cond","cond","cond","conv"])
Resistance_Cond_wood=np.array([None,0.14,0.63,0.23,0.079,None])
Resistance_Cond_insulation=np.array([None,0.14,0.23,0.7,0.079,None])
ResistanceA=np.array([A,A,A,A,A])
Resistanceh=np.array([0.12,None,None,None,None,0.03])

ResistanceR_wood=np.array(np.zeros(6))
ResistanceR_wood[typeR=="cond"]=Resistance_Cond_wood[typeR=="cond"]

ResistanceR_insulation=np.array(np.zeros(6))
ResistanceR_insulation[typeR=="cond"]=Resistance_Cond_insulation[typeR=="cond"]

ResistanceR_conv=np.array(np.zeros(6))


length_coeff_insulation=length_wall_insulation/length_directory_insulation
Resistance_insulation=length_coeff_insulation*ResistanceR_insulation

length_coeff_wood=length_wall_wood/length_directory_wood
Resistance_wood=length_coeff_wood*ResistanceR_wood

ResistanceConvection=ResistanceR_conv[typeR=="conv"]=Resistanceh[typeR=="conv"]


Rtot_wood=Resistance_wood.sum()+ResistanceConvection.sum()
Rtot_insulation=Resistance_insulation.sum()+ResistanceConvection.sum()

U_wood=1/Rtot_wood
U_insulation=1/Rtot_insulation  
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
