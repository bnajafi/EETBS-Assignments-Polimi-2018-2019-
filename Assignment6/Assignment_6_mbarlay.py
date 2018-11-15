#Assignment-6



import os 
import sys
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import os
currentDirectory=os.getcwd()
os.chdir(r"C:\Users\My\Desktop\Laurea Magistrale\ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS\Energy and environmental tech for building systems\Polimi-Asssignments")

import pandas as pd

DF_Input = pd.read_excel("InputData_MeltemBarlay.xlsx",index_col=0,header=0)

def epsilonEffective(epsilon1=0.9,epsilon2=0.9):
    result=1/(1/epsilon1+1/epsilon2-1)
    return result   
    
epsilon_eff=epsilonEffective(0.5,0.9)

def standardLength_material(input_Material):
    ThermalResDict={"Outside Air":{"R":0.03},
            "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
            "Wood Fiberboard":{"R":0.23,"l":0.013},
            "Glass Fiber Insulation":{"R":0.7,"l":0.025},
            "Wood Stud":{"R":0.63,"l":0.9},
            "Gypsum":{"R":0.079,"l":0.013},
            "Inside Air":{"R":0.12}
            }
    standardLength_thisMaterial = ThermalResDict[input_Material]["l"]
    return standardLength_thisMaterial

def RValue_material(input_Material):
    ThermalResDict={"Outside Air":{"R":0.03},
            "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
            "Wood Fiberboard":{"R":0.23,"l":0.013},
            "Glass Fiber Insulation":{"R":0.7,"l":0.025},
            "Wood Stud":{"R":0.63,"l":0.9},
            "Gypsum":{"R":0.079,"l":0.013},
            "Inside Air":{"R":0.12}
            }
    RValue_thisMaterial = ThermalResDict[input_Material]["R"]
    return RValue_thisMaterial

RValue_raw = DF_Input.loc[:,"Material"].apply(RValue_material)
standardLength_material = DF_Input.loc[:,"Material"][DF_Input.loc[:,"Type"]=="cond"].apply(standardLength_material)
RValue_corrected = RValue_raw
RValue_corrected[DF_Input.loc[:,"Type"]=="cond"]=RValue_corrected[DF_Input.loc[:,"Type"]=="cond"]*DF_Input.loc[:,"Length"][DF_Input.loc[:,"Type"]=="cond"]/standardLength_material
DF_Input.loc[:,"Rvalue"] = RValue_corrected
DF_Input.to_excel("InputData_MeltemBarlay.xlsx")

Rtot_withWood =sum(DF_Input.loc[:,"Rvalue"][DF_Input.loc[:,"Material"] != "Glass Fiber Insulation"])
Rtot_withInsulation = sum(DF_Input.loc[:,"Rvalue"][DF_Input.loc[:,"Material"] != "Wood Stud"])

A_tot=100
A_wood=25
A_ins=75
delta_T=24
U_wood = 1/float(Rtot_withWood)
U_ins = 1/float(Rtot_withInsulation)
U_tot = (U_wood*(float(A_wood)/A_tot))+(U_ins*(float(A_ins)/A_tot))
R_tot = 1/float(U_tot)
Q_tot = U_tot*A_tot*delta_T

print("R total is "+str(R_tot)+" m2.degC")
print("U overall is "+str(U_tot)+" m2.degC")
print("Q total is "+str(Q_tot)+" m2.degC")
