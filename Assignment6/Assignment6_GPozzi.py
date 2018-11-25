import pandas as pd
A=50*0.8*2.5
DT=24

thermalResDic= {"Gypsum":{"R":0.079, "length":0.013}, "Plywood":{"R":0.11, "length":0.013},
"InsideSurface":{"R":0.12}, "OutsideSurfaceWinter":{"R":0.03}, "outsideSurfaceSummer":{"R":0.044},"Wood bevel lapped siding":{"R":0.14, "length":0.013},
"fiberboard":{"R":0.23, "length":0.013}, "Wood studs":{"R":0.63, "length":0.09},"Glass Fiber Insulation":{"R":0.7, "length":0.025}}

AirGapResDict={0.02:{0.03:0.051, 0.8181818181818181:0.17, 0.5:0.23},
            0.04:{0.03:0.63, 0.05:0.59, 0.5:0.25}}    #Dictionary with tabulated values of R for different distances end epsilons in an air gap

epsilon1=0.9
epsilon2=0.9
eps_effective=1/(1/epsilon1+1/epsilon2-1)
L_gaP=0.02
R_gap=AirGapResDict[L_gaP][eps_effective]
gap={"R":R_gap}
thermalResDic["Gap"]=gap

R=["Rout","Rwood","Rins","Rstud","Rfiberboard","Rgypsum","Rgap","Rin"]
namesR= ["OutsideSurfaceWinter","Wood bevel lapped siding","Glass Fiber Insulation","Wood studs","fiberboard","Gypsum","Gap","InsideSurface"]
typeR=["conv","cond","cond","cond","cond","cond","gap","conv"]
ResistanceL=[None,0.013,0.09,0.09,0.013,0.013,0.02,None]
Resistance_RValues=[0.03,0.14,0.70,0.63,0.23,0.079,R_gap,0.12]

resistances_listoflists=[namesR,typeR,ResistanceL,Resistance_RValues]
resistance_Dataframe=pd.DataFrame(resistances_listoflists, index=["name","Type","L","R"],columns=R)



def checkRes(MaterialName):

    
    R_value=thermalResDic[MaterialName]["R"]
    return(R_value)

def checkLength(MaterialLength):

    L_value=thermalResDic[MaterialLength]["length"]
    return(L_value)


    
#Insulation

R_raw_ins=resistance_Dataframe.loc["name"].apply(checkRes)
NominalL_insulation=resistance_Dataframe.loc["name"][resistance_Dataframe.loc["Type"]=="cond"].apply(checkLength)
R_raw_ins[resistance_Dataframe.loc["name"]=="Wood studs"]=0
ratio_ins=resistance_Dataframe.loc["L"][resistance_Dataframe.loc["Type"]=="cond"]/NominalL_insulation
R_real_ins=R_raw_ins
R_real_ins[resistance_Dataframe.loc["Type"]=="cond"]=ratio_ins*R_raw_ins[resistance_Dataframe.loc["Type"]=="cond"]
resistance_Dataframe.loc["R_insulation"]=R_real_ins

#Wood Studs

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

print("")
print("Total Resistance with wood studs is "+ str(R_tot_wood)+ " K*m^2/W")
print("")
print("Total Resistance with the insulation is "+ str(R_tot_ins)+ " K*m^2/W")
print("")
print("Total R is " + str(1/U_tot) + "K*m^2/W")
print("")
print("Total U  is "+ str(U_tot)+ " W/K*m^2")
print("")
print("the heat transfer rate is "+ str(Q)+ " W")


resistance_Dataframe.to_excel("Assignment6_GPozzi_Resistances_Results.xlsx")