import os

os.chdir(r"/Users/apple/Desktop/POLIMI LESSONS/Energy")


import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()


import pandas as pd

DF_Input = pd.read_excel("InputData_buketozcan.xlsx",index_col=0,header=0)

def epsilonEffective(epsilon1=0.9, epsilon2=0.9):
    result=1/(1/epsilon1+1/epsilon2-1)
    return result
    
epsilon_eff=epsilonEffective(0.5,0.9)

def RValue_material(input_material):
    ThermalResDict={"Outside Air":{"R":0.03},
            "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
            "Wood Fiberboard":{"R":0.23,"l":0.013},
            "Glass Fiber Insulation":{"R":0.7,"l":0.025},
            "Wood Stud":{"R":0.63,"l":0.9},
            "Gypsum":{"R":0.079,"l":0.013},
            "Inside Air":{"R":0.12}
            }

    RValue_thisMaterial = ThermalResDict[input_material]["R"]
    return RValue_thisMaterial


def standardLength_material(input_material):
    ThermalResDict={"Outside Air":{"R":0.03},
            "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
            "Wood Fiberboard":{"R":0.23,"l":0.013},
            "Glass Fiber Insulation":{"R":0.7,"l":0.025},
            "Wood Stud":{"R":0.63,"l":0.9},
            "Gypsum":{"R":0.079,"l":0.013},
            "Inside Air":{"R":0.12}
            }
    standardLength_thisMaterial = ThermalResDict[input_material]["l"]
    return standardLength_thisMaterial

RValue_raw = DF_Input.loc[:,"Material"].apply(RValue_material)
standardLength_material = DF_Input.loc[:,"Material"][DF_Input.loc[:,"Type"]=="cond"].apply(standardLength_material)
RValue_corrected = RValue_raw
RValue_corrected[DF_Input.loc[:,"Type"]=="cond"]=RValue_corrected[DF_Input.loc[:,"Type"]=="cond"]*DF_Input.loc[:,"Length"][DF_Input.loc[:,"Type"]=="cond"]/standardLength_material
DF_Input.loc[:,"Rvalue"] = RValue_corrected
DF_Input.to_excel("InputData_buketozcan.xlsx")


Rtot_withWood =sum(DF_Input.loc[:,"Rvalue"][DF_Input.loc[:,"Material"] != "Glass Fiber Insulation"])
Rtot_withInsulation = sum(DF_Input.loc[:,"Rvalue"][DF_Input.loc[:,"Material"] != "Wood Stud"])

Atot=100
Awood=25
Ains=75
DeltaT=24
Uwood=1/float(Rtot_withWood)
Uins=1/float(Rtot_withInsulation)
Utot=(Uwood*(float(Awood)/Atot))+(Uins*(float(Ains)/Atot))
Rtot=1/float(Utot)
Qtot=Utot*Atot*DeltaT
print("R total is "+str(Rtot)+" m2.degC/W")
print("U overall is "+str(Utot)+" W/m2.degC")
print("Q total is "+str(Qtot)+" W")