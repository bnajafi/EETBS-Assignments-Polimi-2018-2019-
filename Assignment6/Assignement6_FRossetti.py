# -*- coding: utf-8 -*-
A=50*0.8*2.5
DeltaT=24

import numpy as np
import pandas as pd

R1=["Cond","Gypsum",0.013]
R2=["Cond","Wood bevel lapped siding",0.013]
R3=["Cond","Glass Fiber Ins",0.09]
R4=["Cond","Wood studs",0.09]
R5=["Cond","fiberboard",0.013]
Ro=["Conv","OutsideSurfaceWinter",0]
Ri=["Conv","InsideSurface",0]
Rgap=["Gap","Air-Gap",0.020]

resistances_listOfResistances=[R1,R2,R3,R4,R5,Ro,Ri,Rgap]

Columns=["type","material","Length"]
Resistances_DataFrame=pd.DataFrame(resistances_listOfResistances,index=["R1","R2","R3","R4","R5","Ro","Ri","Rgap"], columns=Columns)

def RValue_material(material):
    ThermalConRes={"FaceBrick":{"R":0.75, "length":0.1},
                "Wood bevel lapped siding":{"R":0.14, "length":0.013},
                "Wood studs":{"R":0.63 ,"length":0.090},
                "fiberboard":{"R":0.23 ,"length":0.013},
                "Glass Fiber Ins":{"R":0.70 ,"length":0.025},
                "Gypsum":{"R":0.079 ,"length":0.013},
                "InsideSurface":{"R":0.12},
                "OutsideSurfaceWinter":{"R":0.03},
                "OutsideSurfaceSummer":{"R":0.44},
                }

    RValue= ThermalConRes[material]["R"]
    return RValue
    
def  StandardLength_material(material):
    ThermalConRes={"FaceBrick":{"R":0.75, "length":0.1},
                "Wood bevel lapped siding":{"R":0.14, "length":0.013},
                "Wood studs":{"R":0.63 ,"length":0.090},
                "fiberboard":{"R":0.23 ,"length":0.013},
                "Glass Fiber Ins":{"R":0.70 ,"length":0.025},
                "Gypsum":{"R":0.079 ,"length":0.013},
                "InsideSurface":{"R":0.12,"length":0},
                "OutsideSurfaceWinter":{"R":0.03},
                "OutsideSurfaceSummer":{"R":0.44},
                }
    
    RValue= ThermalConRes[material]["length"]
    return RValue

def R_AirGap(Length):
    
    AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23},
                   0.040:{0.03:0.063,0.05:0.59,0.5:0.25}}
    Rvalue= AirGapResDict[Length][EpsilonEffective]
    return Rvalue 

R_ValueWood=Resistances_DataFrame.loc[:,"material"][Resistances_DataFrame.loc[:,"type"] == "Cond"][Resistances_DataFrame.loc[:,"material"] != "Glass Fiber Ins"].apply(RValue_material) 
R_valueIns=Resistances_DataFrame.loc[:,"material"][Resistances_DataFrame.loc[:,"type"] == "Cond"][Resistances_DataFrame.loc[:,"material"] != "Wood studs"].apply(RValue_material)   
L_ValueWood=Resistances_DataFrame.loc[:,"material"][Resistances_DataFrame.loc[:,"type"] == "Cond"][Resistances_DataFrame.loc[:,"material"] != "Glass Fiber Ins"].apply(StandardLength_material) 
L_ValueIns=Resistances_DataFrame.loc[:,"material"][Resistances_DataFrame.loc[:,"type"] == "Cond"][Resistances_DataFrame.loc[:,"material"] != "Wood studs"].apply(StandardLength_material) 

Resistances_DataFrame = Resistances_DataFrame.fillna(0)

Resistances_DataFrame.loc[:,"R_finalWood"]=1
Resistances_DataFrame.loc[:,"R_finalIns"]=1

Resistances_DataFrame.loc[:,"R_finalWood"][Resistances_DataFrame.loc[:,"type"] == "Cond"]=R_ValueWood*Resistances_DataFrame.loc[:,"Length"][Resistances_DataFrame.loc[:,"type"] == "Cond"]/L_ValueWood  
Resistances_DataFrame.loc[:,"R_finalIns"][Resistances_DataFrame.loc[:,"type"] == "Cond"]=R_valueIns*Resistances_DataFrame.loc[:,"Length"][Resistances_DataFrame.loc[:,"type"] == "Cond"]/L_ValueIns 

Resistances_DataFrame.loc[:,"R_finalWood"][Resistances_DataFrame.loc[:,"type"] == "Conv"]=Resistances_DataFrame.loc[:,"material"][Resistances_DataFrame.loc[:,"type"]=="Conv"].apply(RValue_material)
Resistances_DataFrame.loc[:,"R_finalIns"][Resistances_DataFrame.loc[:,"type"] == "Conv"]=Resistances_DataFrame.loc[:,"material"][Resistances_DataFrame.loc[:,"type"]=="Conv"].apply(RValue_material)


EpsilonEffective=round(1/(1/0.05+1/0.9-1),2)

Resistances_DataFrame.loc[:,"R_finalWood"][Resistances_DataFrame.loc[:,"type"] == "Gap"]=Resistances_DataFrame.loc[:,"Length"][Resistances_DataFrame.loc[:,"type"]=="Gap"].apply(R_AirGap)
Resistances_DataFrame.loc[:,"R_finalIns"][Resistances_DataFrame.loc[:,"type"] == "Gap"]=Resistances_DataFrame.loc[:,"Length"][Resistances_DataFrame.loc[:,"type"]=="Gap"].apply(R_AirGap)


R_totWood=Resistances_DataFrame.loc[:,"R_finalWood"].sum()
print("The total Resistance considering the wood studs is: "+str(R_totWood))
R_totIns=Resistances_DataFrame.loc[:,"R_finalIns"].sum()
print("The total Resistance considering ins is:"+str(R_totIns)) 

U_wood=1/R_totWood
U_ins=1/R_totIns 
print("The heat transfer coefficient, considering the wood is " + str(U_wood)+ "  W/m^2")  
print("The heat transfer coefficient, considering the insulation is "+str(U_ins)+ "  W/m^2")
U_tot=U_wood*0.25+U_ins*0.75
print("The overall heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
print("The overall resistance is "+str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DeltaT
print("The overall heat tranfer is "+str(Q_tot)+ "  W")
