#ASSIGNMENT 6:

#Air gap calculation:
#R_gap={"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.02}


def epsilonEffective(epsilon1, epsilon2):
    result=1/(1/epsilon1+1/epsilon2-1)
    return result


AirGapResDict={0.02:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
            0.04:{0.03:0.63,0.05:0.59,0.5:0.25}}


epsilon=epsilonEffective(0.05,0.9)
RValue_AirGap=AirGapResDict[0.02][epsilon]


#Matrix

import pandas as pd

R=["Ri","R1","R2","R3","R4","R5","Ro","Rgap"]
Names= ["OutsideSurfaceWinter","WoodBevelLappedSiding","GlassFiberInsulation","WoodStuds","FiberBoard","Gypsum","InsideSurface","AirGap"]
Type=["conv","cond","cond","cond","cond","cond","conv","gap"]
Resistance_L=[None,0.013,0.09,0.09,0.013,0.013,None,0.02]
Resistance_RValues=[0.03,0.14,0.70,0.63,0.23,0.079,0.12,RValue_AirGap]

Resistances_list=[Names,Type,Resistance_L,Resistance_RValues]
Resistance_Dataframe=pd.DataFrame(Resistances_list,index=["Name","Type","L","R"],columns=R)

def CreatingMatrix(DataFrame):

    ThermalConRes={"FaceBrick":{"R":0.75, "length":0.1},
    "WoodBevelLappedSiding":{"R":0.14, "length":0.013},
    "WoodStuds":{"R":0.63 ,"length":0.090},
    "FiberBoard":{"R":0.23 ,"length":0.013},
    "GlassFiberInsulation":{"R":0.70 ,"length":0.025},
    "Gypsum":{"R":0.079 ,"length":0.013},
    "InsideSurface":{"R":0.12},
    "AirGap":{"R":RValue_AirGap,"length":0.02},
    "OutsideSurfaceWinter":{"R":0.03},
    "OutsideSurfaceSummer":{"R":0.44},
    }

    for Any_Resistance in R:
        name=DataFrame.loc["Name",Any_Resistance]
        List=ThermalConRes[name]
        if DataFrame.loc["Type",Any_Resistance]=="cond":
            length=DataFrame.loc["L",Any_Resistance]
            DataFrame.loc["R",Any_Resistance]=(length/List["length"])*DataFrame.loc["R",Any_Resistance]
        elif DataFrame.loc["Type",Any_Resistance]=="gap":
            length=DataFrame.loc["L",Any_Resistance]
            DataFrame.loc["R",Any_Resistance]=(length/List["length"])*DataFrame.loc["R",Any_Resistance]
    return(DataFrame)
   

Table=CreatingMatrix(Resistance_Dataframe)


import os
os.chdir(r"C:\Users\media\Documents\1 Master POLIMI\Building Systems\My assignments\Assignment 6")
Table.to_excel("Assignment6_AnaBlanco_Matrix.xlsx")