#assignment6
#funaro_eleonora

Awood=0.25
Ainsulation=0.75
Atot=100 
dT=24

import pandas as pd

resistance_names=["wood_stud","wood_fiber","wood_bevel","gypsum","inside_surface","outside_surface","glass"]
resistance_types=["cond","cond","cond","cond","conv","conv","cond"]
resistance_RWood=[0.63,0.23,0.14,0.079,0.12,0.03,0.7]
resistance_LReal=[0.09,0.013,0.013,0.013,None,None,0.09]


def RValue_material(input_material):
    ThermalResDic={"wood_stud":{"R":0.63,"length":0.09}
    ,"wood_fiber":{"R":0.23,"length":0.013}
    ,"wood_bevel":{"R":0.14,"length":0.013}
    ,"glass":{"R":0.7,"length":0.025}
    ,"gypsum":{"R":0.079,"length":0.013}
    ,"inside_surface":{"R":0.12}
    ,"outside_surface":{"R":0.03}
    }
    RValue_thisMaterial=ThermalResDic[input_material]["R"]
    return RValue_thisMaterial

def standardLength(input_material):
    ThermalResDic={"wood_stud":{"R":0.63,"length":0.09}
    ,"wood_fiber":{"R":0.23,"length":0.013}
    ,"wood_bevel":{"R":0.14,"length":0.013}
    ,"glass":{"R":0.7,"length":0.025}
    ,"gypsum":{"R":0.079,"length":0.013}
    ,"inside_surface":{"R":0.12}
    ,"outside_surface":{"R":0.03}
    }
    standardLength_thisMaterial=ThermalResDic[input_material]["length"]
    return standardLength_thisMaterial
       
                   
resistance_listOfLists=[resistance_names,resistance_types,resistance_RWood,resistance_LReal]
resistance_DataFrame=pd.DataFrame(resistance_listOfLists,index=["material","type","Rwood","Lreal"], columns=["R1","R2","R3","R4","R5","R6","R7"])

RValue_raw=resistance_DataFrame.loc["material",:].apply(RValue_material)
standardLength=resistance_DataFrame.loc["material",:][resistance_DataFrame.loc["type",:]=="cond"].apply(standardLength) 
RValue_corrected=RValue_raw 
RValue_corrected[resistance_DataFrame.loc["type",:]=="cond"]=RValue_corrected[resistance_DataFrame.loc["type",:]=="cond"]*resistance_DataFrame.loc["Lreal",:][resistance_DataFrame.loc["type",:]=="cond"]/standardLength
resistance_DataFrame.loc["Rvalue",:]=RValue_corrected
resistance_DataFrame.transpose()

Rtot_wood=resistance_DataFrame.loc["Rvalue"][resistance_DataFrame.loc["material"] != "glass"].sum()
Rtot_glass=resistance_DataFrame.loc["Rvalue"][resistance_DataFrame.loc["material"] != "wood_stud"].sum()


print("Rwood: " +str(Rtot_wood))  
print("Rinsulation: " +str(Rtot_glass))

Uwood=1/Rtot_wood
Uinsulation=1/Rtot_glass
Utot=(Uinsulation*Ainsulation)+(Uwood*Awood)
Rtot=1/Utot

print("Rtot: " +str(Rtot))

Q=(Atot*dT)/Rtot
        
print("Q: " +str(Q))    

