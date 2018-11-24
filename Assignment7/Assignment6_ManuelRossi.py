
import pandas as pd

Res = ["RoW","RoS","R1","R2","R3","R4","R5","Ri"]
namesR = ["OutsideSurfaceWinter","OutsideSurfaceSummer","Wood bevel lapped siding","Glass Fiber Insulation","Wood studs","fiberboard","Gypsum","InsideSurface"]
typeR = ["conv","conv","cond","cond","cond","cond","cond","conv"]
ResL = [None,None,0.013,0.09,0.09,0.013,0.013,None]
ResValues = []

resistances_listoflists=[namesR,typeR,ResL,ResValues]
ResDataframe=pd.DataFrame(resistances_listoflists, index=["Name","Type","Length","Value"],columns=Res)
ResDataframe=ResDataframe.T
    

def RValue_material(material):
    ThermalResDict={"FaceBrick":{"R":0.75, "length":0.1},
    "Wood bevel lapped siding":{"R":0.14, "length":0.013},
    "Wood studs":{"R":0.63 ,"length":0.090},
    "fiberboard":{"R":0.23 ,"length":0.013},
    "Glass Fiber Insulation":{"R":0.70 ,"length":0.025},
    "Gypsum":{"R":0.079 ,"length":0.013},
    "InsideSurface":{"R":0.12},
    "OutsideSurfaceWinter":{"R":0.03},
    "OutsideSurfaceSummer":{"R":0.044}
    }
    
    RValue= ThermalResDict[material]["R"]
    return RValue

def  StandardLength_material(material):
    ThermalResDict={"FaceBrick":{"R":0.75, "length":0.1},
    "Wood bevel lapped siding":{"R":0.14, "length":0.013},
    "Wood studs":{"R":0.63 ,"length":0.090},
    "fiberboard":{"R":0.23 ,"length":0.013},
    "Glass Fiber Insulation":{"R":0.70 ,"length":0.025},
    "Gypsum":{"R":0.079 ,"length":0.013},
    "InsideSurface":{"R":0.12},
    "OutsideSurfaceWinter":{"R":0.03},
    "OutsideSurfaceSummer":{"R":0.044}
    }
    
    RValue= ThermalResDict[material]["length"]
    return RValue


AirGapRes=pd.DataFrame(index=["0.03","0.05","0.5","0.82"], columns=["0.02","0.04","0.09"])
AirGapRes.loc[:,"0.02"]=[0.51,0.49,0.23,0.18]
AirGapRes.loc[:,"0.04"]=[0.45,0.43,0.22,0.16]
AirGapRes.loc[:,"0.09"]=[0.47,0.45,0.22,0.16]

def epsilonEffective(eps1=0.9,eps2=0.9):
    result = 1/(1/eps1+1/eps2 -1)
    return result
       
EpsEffective = round(epsilonEffective(0.9,0.1),5)

def Interpole(AirGapRes,eff):
    if (eff<=0.05):
        R=(AirGapRes.loc["0.05",:]-AirGapRes.loc["0.03",:])/(0.05-0.03)*(eff-0.03)+AirGapRes.loc["0.03",:]
    elif (eff>0.05 and eff<=0.5):
        R=(AirGapRes.loc["0.5",:]-AirGapRes.loc["0.05",:])/(0.5-0.05)*(eff-0.05)+AirGapRes.loc["0.05",:]
    elif (eff>0.5):
        R=(AirGapRes.loc["0.82",:]-AirGapRes.loc["0.5",:])/(0.82-0.5)*(eff-0.5)+AirGapRes.loc["0.5",:]
    return R

Rgap = Interpole(AirGapRes,EpsEffective)["0.02"]

Rvalue_raw = ResDataframe["Name"].apply(RValue_material)
#standardLength_material = ResDataframe["Name"][ResDataframe["Type"]=="cond"].apply(StandardLength_material)
standardLength_material = ResDataframe.loc[:,"Name"][ResDataframe.loc[:,"Type"]=="cond"].apply(StandardLength_material)
RValue_final=Rvalue_raw
#RValue_final[ResDataframe["Type"]=="cond"] = RValue_final[ResDataframe["Type"]=="cond"]*ResDataframe["Length"][ResDataframe["Type"]=="cond"]/standardLength_material
RValue_final[ResDataframe.loc[:,"Type"]=="cond"]=RValue_final[ResDataframe.loc[:,"Type"]=="cond"]*ResDataframe.loc[:,"Length"][ResDataframe.loc[:,"Type"]=="cond"]/standardLength_material
standardLength_material = ResDataframe.loc[:,"Name"][ResDataframe.loc[:,"Type"]=="cond"].apply(StandardLength_material)
ResDataframe.loc["Rgap",:] = ["Air gap","gap", None, Rgap]
ResDataframe["Value"]=RValue_final

ResWoodWinter=ResDataframe.loc[:,"Value"][ResDataframe.loc[:,"Name"]!=("Glass Fiber Insulation" and "OutsideSurfaceSummer")].sum()
ResWoodSummer=ResDataframe.loc[:,"Value"][ResDataframe.loc[:,"Name"]!=("Glass Fiber Insulation" and "OutsideSurfaceWinter")].sum()

ResFiberWinter=ResDataframe.loc[:,"Value"][ResDataframe.loc[:,"Name"]!=("Wood studs" and "OutsideSurfaceSummer")].sum()
ResFiberSummer=ResDataframe.loc[:,"Value"][ResDataframe.loc[:,"Name"]!=("Wood studs" and "OutsideSurfaceWinter")].sum()

UWinter=0.20/ResWoodWinter+0.8/ResFiberWinter
USummer=0.20/ResWoodSummer+0.8/ResFiberSummer

ResDataframe.loc["U Winter",:] = ["Winter","result", None, UWinter]
ResDataframe.loc["U Summer",:] = ["Summer","result", None, USummer]

T_in = 22
T_out = -2
DT = (T_in - T_out)
A = 50*(1-0.2)*2.5
QWinter = UWinter*A*DT
QSummer = USummer*A*DT

ResDataframe.loc["Q Winter",:] = ["Winter","result", None, QWinter]
ResDataframe.loc["Q Summer",:] = ["Summer","result", None, QSummer]


import os
os.chdir (r"C:\Users\Famiglia\Documents\Manuel\Polimi\MAGISTRALE\PRIMO ANNO\Primo semestre\Bezhad\forkedRepos")

ResDataframe.to_csv("ManuelResult.csv")
ResDataframe.to_html("ManuelResult.html")
ResDataframe.to_excel("ManuelResult.xlsx")