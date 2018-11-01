A=50*0.8*2.5
DeltaT=24

import numpy as np

Materials=np.array(["Gypsum","Wood bevel lapped siding","Wood studs","Glass Fiber Ins","fiberboard","OutsideSurfaceWinter","inside surface"])
ResistanceTypes=np.array(["Cond","Cond","Cond","Cond","Cond","Conv","Conv"])
ResistancesLength=np.array([0.013,0.013,0.090,0.090,0.013,None,None])
ResistancesValue=np.array([0.079,0.14,0.63,0.7,0.23,0.03,0.12])
ResistancesLenghtTable=np.array([0.013,0.013,0.090,0.025,0.013,None,None])

Resistances= np.array(np.zeros(7))

WoodList=Wood=np.array(["Wood","Wood","Wood","Ins","Wood","Wood","Wood"])=="Wood"
InsList=Insulation=np.array(["Ins","Ins","Wood","Ins","Ins","Ins","Ins"])=="Ins"
Cond=ResistanceTypes=="Cond"
Wood_Cond= WoodList & Cond 
Ins_Cond= InsList & Cond

Resistances[ResistanceTypes=="Conv"]=ResistancesValue[ResistanceTypes=="Conv"]
R_tot_Conv=Resistances[ResistanceTypes=="Conv"].sum()

Resistances[Wood_Cond]=ResistancesValue[Wood_Cond]*ResistancesLength[Wood_Cond]/ResistancesLenghtTable[Wood_Cond]
R_tot_WoodCond=Resistances[Wood_Cond].sum()

Resistances[Ins_Cond]=ResistancesValue[Ins_Cond]*ResistancesLength[Ins_Cond]/ResistancesLenghtTable[Ins_Cond]
R_tot_InsCond=Resistances[Ins_Cond].sum()

print("The total Resistance considering Wood is " + str(R_tot_WoodCond+R_tot_Conv) )
print("The total Resistance considering Insulation is "+ str(R_tot_InsCond+R_tot_Conv))

U_Wood=1.0/(R_tot_WoodCond+R_tot_Conv)
U_Ins=1.0/(R_tot_InsCond+R_tot_Conv)
  
print("The heat transfer coefficient, considering the wood is " + str(U_Wood)+ "  W/m^2")  
print("The heat transfer coefficient, considering the insulation is "+str(U_Ins)+ "  W/m^2")
U_tot=U_Wood*0.25+U_Ins*0.75
print("The overall heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_tot=1/U_tot
print("The overall resistance is "+str(R_tot)+ " m^2/W")
Q_tot=U_tot*A*DeltaT
print("The overall heat tranfer is "+str(Q_tot)+ "  W")


