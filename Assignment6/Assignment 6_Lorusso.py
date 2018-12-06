import pandas as pd

Tin=2
Tout=-2
A=50*0.8 
A_wood=A*0.25    #25%
A_fiber=A*0.75

ThermalResDic={"FaceBrick":{"R":0.075,"lenght":0.1}
,"WoodStud_90mm":{"R":0.36,"lenght":0.09}
,"WoodFiberBoard":{"R":0.24,"lenght":0.013}
,"GlassFiberIsulation":{"R":0.7,"lenght":0.025}
,"WoodLappedSiding":{"R":0.14,"lenght":0.013}
,"Gypsum":{"R":0.079,"lenght":0.013}
,"InsideAir":{"R":0.12}
,"outsideSurfaceWinter":{"R":0.03}
,"outsideSurfaceSummer":{"R":0.044}
}

AirGapDict={
            0.020:{0.03:0.05,0.05:0.49,0.5:0.23},
            0.040:{0.03:0.063,0.05:0.59,0.5:0.25}
            }

Ri = ["conv","InsideAir",None,None,A,None,0.12,0]
R1 = ["cond","WoodLappedSiding",0.013,0.013,A,None,0.14,0]
R2 = ["cond","WoodFiberBoard",0.013,0.013,A,None,0.24, 0]
R3 = ["cond","GlassFiberIsulation",0.09,0.025,A,None,0.7, 0]
R4 = ["cond","WoodStud_90mm",0.09,0.09,A,None,0.36, 0]
R5 = ["cond","Gypsum",0.013,0.013,A,None,0.079, 0]
Ro = ["conv","outsideSurfaceWinter",None,None,A,None,0.03,0]
R_gap = ["cond","gap",0.02,0.02,A,0.05,0.49, 0]

E_effective=1/(1/R_gap[5]+1/0.9-1)
Eps=R_gap[5]
error= (Eps-E_effective)/Eps
R_gap[-1]=R_gap[-2]

resistences_name=["Inside Air","Wood blevel lapped Siding","WoodFiberBoard","Glass Fiber Insulation","WoodStud_90mm","Gypsum Wallboard","OutSide Surface","air gap"]
colums_name=["type","material","L_real","L_tab","A","epsilon","R_tab","RValue"]

Resistences_DF = pd.DataFrame([Ri,R1,R2,R3,R4,R5,Ro,R_gap],index=resistences_name,columns=colums_name)

Resistences_DF["RValue"][Resistences_DF["type"]=="conv"] = Resistences_DF["R_tab"][Resistences_DF["type"]=="conv"]
Resistences_DF["RValue"][Resistences_DF["type"]=="cond"] = Resistences_DF["R_tab"][Resistences_DF["type"]=="cond"] * Resistences_DF["L_real"][Resistences_DF["type"]=="cond"]/Resistences_DF["L_tab"][Resistences_DF["type"]=="cond"]
 
 #R wood calculation
Rwood_serie=Resistences_DF["RValue"]
Rwood_serie["Glass Fiber Insulation"]=0
Rwood=Rwood_serie.sum()
Uwood=1/Rwood

Resistences_DF = pd.DataFrame([Ri,R1,R2,R3,R4,R5,Ro,R_gap],index=resistences_name,columns=colums_name)
Resistences_DF["RValue"][Resistences_DF["type"]=="conv"] = Resistences_DF["R_tab"][Resistences_DF["type"]=="conv"]
Resistences_DF["RValue"][Resistences_DF["type"]=="cond"] = Resistences_DF["R_tab"][Resistences_DF["type"]=="cond"] * Resistences_DF["L_real"][Resistences_DF["type"]=="cond"]/Resistences_DF["L_tab"][Resistences_DF["type"]=="cond"]
 
# R ins calclation
Rins_serie=Resistences_DF["RValue"]
Rins_serie["WoodStud_90mm"]=0
Rins=Rins_serie.sum()
Uins=1/Rins

Resistences_DF = pd.DataFrame([Ri,R1,R2,R3,R4,R5,Ro,R_gap],index=resistences_name,columns=colums_name)
Resistences_DF["RValue"][Resistences_DF["type"]=="conv"] = Resistences_DF["R_tab"][Resistences_DF["type"]=="conv"]
Resistences_DF["RValue"][Resistences_DF["type"]=="cond"] = Resistences_DF["R_tab"][Resistences_DF["type"]=="cond"] * Resistences_DF["L_real"][Resistences_DF["type"]=="cond"]/Resistences_DF["L_tab"][Resistences_DF["type"]=="cond"]

#U tot

Utot=0.25*Uwood+0.75*Uins

Q=Utot*A*(Tin-Tout)

print("the heat transfer is "+ str(Q)+ " W")


import os

os.chdir(r"C:\Users\LoruPortatile\Desktop\clima 2\Assignments_Lorusso\Assignment6")

Resistences_DF.to_excel("Assignment6Result_Lorusso.xlsx")