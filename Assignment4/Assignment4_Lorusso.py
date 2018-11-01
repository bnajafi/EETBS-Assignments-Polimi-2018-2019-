#Assignment4
#Main script Lorusso

import os
os.chdir("C:\Users\LoruPortatile\Desktop\clima 2\Assignments_Lorusso\Assignment4")

import WallCalculation_Lorusso as F

Tin=2
Tout=-2
A=50*0.8 
A_wood=A*0.25    #25%
A_fiber=A*0.75

Ri={"name":"Inside Air","type":"conv","material":"InsideAir","area":A}
R1={"name":"Wood blevel lapped Siding","type":"cond","material":"WoodLappedSiding","area":A,"lenght":0.013}
R2={"name":"WoodFiberBoard","type":"cond","material":"WoodFiberBoard","area":A,"lenght":0.013}
R3={"name":"Glass Fiber Insulation","type":"cond","material":"GlassFiberIsulation","area":A,"lenght":0.09}
R4={"name":"WoodStud_90mm","type":"cond","material":"WoodStud_90mm","area":A,"lenght":0.9}
R5={"name":"Gypsum Wallboard","type":"cond","material":"Gypsum","area":A,"lenght":0.013}
Ro={"name":"OutSide Surface","type":"conv","material":"outsideSurfaceWinter","area":A}
R_gap={"name":"air gap","type":"gap","epsilon1":0.05,"lenght":0.020}

R_Wood=[Ri,R1,R2,R4,R5,Ro,R_gap]
R_Ins=[Ri,R1,R2,R3,R5,Ro,R_gap]
Rseries1={"name":"R_Wood","serie":R_Wood,"Area":A_wood}
Rseries2={"name":"R_Ins","serie":R_Ins,"Area":A_fiber}


Rtot1=F.ResistanceOfLayersInSeries(Rseries1)
Rtot2=F.ResistanceOfLayersInSeries(Rseries2)
ListOfResult=[Rtot1,Rtot2]

Utot=Rtot1["Uvalue"]*Rtot1["Area"]+Rtot2["Uvalue"]*Rtot2["Area"]


Q=F.HeatTransfer(Tin,Tout,Utot,A)

print("the heat transfer Q though the wall is : "+str(Q)+" W")