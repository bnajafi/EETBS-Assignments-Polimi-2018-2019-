import pandas as pd
A=50*0.8*2.5
DT=24

AirGapResDict={0.02:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
            0.04:{0.03:0.63,0.05:0.59,0.5:0.25}}   
ThermalConRes={"FaceBrick":{"R":0.75, "length":0.1},
"Wood bevel lapped siding":{"R":0.14, "length":0.013},
"Wood studs":{"R":0.63 ,"length":0.090},
"fiberboard":{"R":0.23 ,"length":0.013},
"Glass Fiber Insulation":{"R":0.70 ,"length":0.025},
"Gypsum":{"R":0.079 ,"length":0.013},
"InsideSurface":{"R":0.12},
"OutsideSurfaceWinter":{"R":0.03},
"OutsideSurfaceSummer":{"R":0.44},
}

epsilon1=0.05
epsilon2=0.9
E_effective=1/(1/epsilon1+1/epsilon2-1)
L_gaP=0.02
R_gap=AirGapResDict[L_gaP][E_effective]
gap={"R":R_gap}
ThermalConRes["Gap"]=gap

R=["Ri","R1","R2","R3","R4","R5","Rgap","Ro"]
namesR= ["OutsideSurfaceWinter","Wood bevel lapped siding","Glass Fiber Insulation","Wood studs","fiberboard","Gypsum","Gap","InsideSurface"]
typeR=["conv","cond","cond","cond","cond","cond","gap","conv"]
ResistanceL=[None,0.013,0.09,0.09,0.013,0.013,0.02,None]
Resistance_RValues=[0.03,0.14,0.70,0.63,0.23,0.079,R_gap,0.12]

resistances_listoflists=[namesR,typeR,ResistanceL,Resistance_RValues]
resistance_Dataframe=pd.DataFrame(resistances_listoflists, index=["name","Type","L","R"],columns=R)
#DataFrame=resistance_Dataframe

def checkRes(MaterialName):

    
    R_value=ThermalConRes[MaterialName]["R"]
    return(R_value)

def checkLength(MaterialLength):

    L_value=ThermalConRes[MaterialLength]["length"]
    return(L_value)


    
#calculation Insulation
R_raw_ins=resistance_Dataframe.loc["name"].apply(checkRes)
NominalL_insulation=resistance_Dataframe.loc["name"][resistance_Dataframe.loc["Type"]=="cond"].apply(checkLength)
R_raw_ins[resistance_Dataframe.loc["name"]=="Wood studs"]=0
ratio_ins=resistance_Dataframe.loc["L"][resistance_Dataframe.loc["Type"]=="cond"]/NominalL_insulation
R_real_ins=R_raw_ins
R_real_ins[resistance_Dataframe.loc["Type"]=="cond"]=ratio_ins*R_raw_ins[resistance_Dataframe.loc["Type"]=="cond"]
resistance_Dataframe.loc["R_insulation"]=R_real_ins
#calculation Wood
R_raw_wood=resistance_Dataframe.loc["name"].apply(checkRes)
NominalL_wood=resistance_Dataframe.loc["name"][resistance_Dataframe.loc["Type"]=="cond"].apply(checkLength)
R_raw_wood[resistance_Dataframe.loc["name"]=="Glass Fiber Insulation"]=0
ratio_wood=resistance_Dataframe.loc["L"][resistance_Dataframe.loc["Type"]=="cond"]/NominalL_wood
R_real_wood=R_raw_wood
R_real_wood[resistance_Dataframe.loc["Type"]=="cond"]=ratio_wood*R_raw_wood[resistance_Dataframe.loc["Type"]=="cond"]
resistance_Dataframe.loc["R_wood"]=R_real_wood

R_tot_ins=resistance_Dataframe.loc["R_insulation"].sum()
R_tot_wood=resistance_Dataframe.loc["R_wood"].sum()

U_tot=1/R_tot_ins*0.75+1/R_tot_wood*0.25
Q=U_tot*A*DT

print("the heat transfer is "+ str(Q)+ " W")


import os

os.chdir(r"C:\Users\elbar\Desktop\universita\magistrale\Primo Anno\Building System\Python")

resistance_Dataframe.to_excel("Assignment6Result.xlsx")
