# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

Tin=22
Tout=-2
A=50*2.5*0.8


resistance_name=["Outside Air","Wood Bevel Lapped Siding","Wood Fiberboard","Glass Fiber Insulation","Wood Stud","Gypsum","Inside Air","air_gap","epsilon1","epsilon2"]
resistance_material=["Outside Air","Wood Bevel Lapped Siding","Wood Fiberboard","Glass Fiber Insulation","Wood Stud","Gypsum","Inside Air","air_gap",0,0]
resistance_type=["conv","cond","cond","cond","cond","cond","conv",None,"Airgap","Airgap"]
resistance_length=[None,0.013,0.013,0.09,0.9,0.013,None,None,None,None]
resistance_index=["type","length","material","R","L_dict","R_real","resistance_Epsilon"]
resistance_value=[0,0,0,0,0,0,0,0,0]                                   
resistance_L_dict=[0,0,0,0,0,0,0,0.020,0,0]
resistance_R_real=[0,0,0,0,0,0,0,0,0,0]
resistance_Epsilon=[0,0,0,0,0,0,0,0,0.05,0.9]

resistance_matrix=pd.DataFrame([resistance_type,resistance_length,resistance_material,resistance_value,resistance_L_dict,resistance_R_real,resistance_Epsilon],index=resistance_index,columns=resistance_name)


def resistance_calculus(inputValue):
     ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}}

     outputvalue=ThermalResDict[inputValue]["R"]
     return outputvalue

#applying the function
resistance_matrix.loc["R"][resistance_matrix.loc["type"]=="cond"]=resistance_matrix.loc["material"][resistance_matrix.loc["type"]=="cond"].apply(resistance_calculus)


def raw_length_calculus(inputValue):
     ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}}

     outputvalue=ThermalResDict[inputValue]["l"]
     return outputvalue

resistance_matrix.loc["L_dict"][resistance_matrix.loc["type"]=="cond"]=resistance_matrix.loc["material"][resistance_matrix.loc["type"]=="cond"].apply(raw_length_calculus)
resistance_matrix.loc["R_real"][resistance_matrix.loc["type"]=="cond"]=resistance_matrix.loc["R"][resistance_matrix.loc["type"]=="cond"]*resistance_matrix.loc["length"][resistance_matrix.loc["type"]=="cond"]/resistance_matrix.loc["L_dict"][resistance_matrix.loc["type"]=="cond"]
resistance_matrix.loc["R_real"][resistance_matrix.loc["type"]=="conv"]=resistance_matrix.loc["material"][resistance_matrix.loc["type"]=="conv"].apply(resistance_calculus)

Epsilon1=resistance_matrix.loc["resistance_Epsilon","epsilon1"]
Epsilon2=resistance_matrix.loc["resistance_Epsilon","epsilon2"]

def epsilonEffective(epsilon1,epsilon2):
    """This function, given the values of epsilon1 and epsilon2,calculates the epsilon effective """
    result=(1/(1/epsilon1+1/epsilon2-1))
    return result
resistance_matrix.loc["R","air_gap"]=epsilonEffective(Epsilon1,Epsilon2)


def EpsilonEffectiveReal(InputValue):
    outputValue=0.51+((0.49-0.51)/(0.05-0.03))*(InputValue-0.03)
    return outputValue
    
resistance_matrix.loc["R_real","air_gap"]=EpsilonEffectiveReal(resistance_matrix.loc["R","air_gap"])
RtotWood=resistance_matrix.loc["R_real"][resistance_matrix.loc["material"]!="Glass Fiber Insulation"].sum()
RtotFiber=resistance_matrix.loc["R_real"][resistance_matrix.loc["material"]!="Wood Stud"].sum()
U1=1/float(RtotWood)
U2=1/float(RtotFiber)
U_overall=U1*0.25+U2*0.75
Q=U_overall*(Tin-Tout)*A
print ("La U totale è: "+str(U_overall))
print ("La Q totale è: "+str(Q))
                