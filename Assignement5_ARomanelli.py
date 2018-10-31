import numpy as np

#wood
R_1=["outside surface","conv",0.03]
R_2=["wood bevel lapped siding","cond",0.013,0.14,0.013]
R_3=["fiberboard","cond",0.013,0.23,0.013]
R_4b=["wood stud","cond",0.09,0.63,0.09]
R_5=["Gypsum Wallboard","cond",0.013,0.079,0.013]
R_6=["inside surface","conv",0.12]


resistences_names=np.array(["outside surface","wood bevel lapped siding","fiberboard","wood stud","Gypsum Wallboard","inside surface"])
resistences_types=np.array(["conv","cond","cond","cond","cond","conv"])
resistences_Lreal=np.array([None,0.013,0.013,0.09,0.013,None])
resistences_R=np.array([0.03,0.14,0.23,0.63,0.079,0.12])
resistences_Ltab=np.array([None,0.013,0.013,0.09,0.013,None])

Rwood=np.array(np.zeros(6))

Rwood[resistences_types=="cond"]=resistences_R[resistences_types=="cond"]*(resistences_Lreal[resistences_types=="cond"]/resistences_Ltab[resistences_types=="cond"])
Rwood[resistences_types=="conv"]=resistences_R[resistences_types=="conv"]
Rtot_wood=Rwood.sum()


#insulation

R_1=["outside surface","conv",0.03]
R_2=["wood bevel lapped siding","cond",0.013,0.14,0.013]
R_3=["fiberboard","cond",0.013,0.23,0.013]
R_4a=["glass fiber insulation","cond",0.09,0.70,0.025]
R_5=["Gypsum Wallboard","cond",0.013,0.079,0.013]
R_6=["inside surface","conv",0.12]

resistences_names=np.array(["outside surface","wood bevel lapped siding","fiberboard","glass fiber insulation","Gypsum Wallboard","inside surface"])
resistences_types=np.array(["conv","cond","cond","cond","cond","conv"])
resistences_Lreal=np.array([None,0.013,0.013,0.09,0.013,None])
resistences_R=np.array([0.03,0.14,0.23,0.70,0.079,0.12])
resistences_Ltab=np.array([None,0.013,0.013,0.025,0.013,None])

Rins=np.array(np.zeros(6))

Rins[resistences_types=="cond"]=resistences_R[resistences_types=="cond"]*(resistences_Lreal[resistences_types=="cond"]/resistences_Ltab[resistences_types=="cond"])
Rins[resistences_types=="conv"]=resistences_R[resistences_types=="conv"]
Rtot_ins=Rins.sum()

print("The total resistence with wood is "+ str(Rtot_wood)+ " degC/W")
print("The total resistence with insulation is "+ str(Rtot_ins)+ " degC/W")

U_wood=1/Rtot_wood
U_ins= 1/Rtot_ins

print("The heat  transfer  coefficient with wood is "+ str(U_wood)+ "W/degC" )
print("The heat  transfer  coefficient with insulation is "+ str(U_ins)+ "W/degC" )


A=50*0.8*2.5
DeltaT=24

U_tot=U_wood*0.25+U_ins*0.75

print("The overall  heat  transfer  coefficient  is "+ str(U_tot)+ "W/degC" )

R_tot=1/U_tot

print("The overall  unit  thermal  resistance is "+ str(R_tot)+ "degC/W" )

Q=U_tot*A*DeltaT

print("The rate  of  heat  loss  through  the  walls is "+str(Q)+ "W")

                                                       
        
        
        



