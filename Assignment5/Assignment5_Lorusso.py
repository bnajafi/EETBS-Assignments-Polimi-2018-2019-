# -*- coding: utf-8 -*-
#Assignment 5

import numpy as np

Tin=2
Tout=-2
A=50*0.8 

ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}
                }

Ri=["Rin","conv","InsideAir"]
R1=["R1","cond","WoodLappedSiding",0.013]
R2=["R2","cond","WoodFiberBoard",0.013]
R3=["R3","cond","GlassFiberIsulation",0.09]
R4=["R4","cond","WoodStud_90mm",0.09]
R5=["R5","cond","Gypsum",0.013]
Ro=["Rout","conv","outsideSurfaceWinter"]

#Series Layer 1
R_series_names = np.array(["Rin","R1","R2","R3","R5","Rout"])
R_series_types = np.array(["conv","cond","cond","cond","cond","conv"])
R_series_Rvalue_Tab = np.array([0.12,0.14,0.23,0.7,0.079,0.03])
R_series_Lvalue_Tab = np.array([None,0.013,0.013,0.025,0.013,None])
R_series_Lvalue_real= np.array([None,0.013,0.013,0.09,0.013,None])
R_series_values= np.array(np.zeros(6))
R_series_values[R_series_types=="cond"] = R_series_Rvalue_Tab[R_series_types=="cond"] *R_series_Lvalue_real[R_series_types=="cond"]/(R_series_Lvalue_Tab[R_series_types=="cond"]) 
R_series_values[R_series_types=="conv"] = R_series_Rvalue_Tab[R_series_types=="conv"]
R_Ins_tot=R_series_values.sum()
U_Ins_tot=1./R_Ins_tot

#Series Layer 2
R_series_names = np.array([ "Rin","R1","R2","R4","R5","Rout" ])
R_series_types = np.array([ "conv","cond","cond","cond","cond","conv" ])
R_series_Rvalue_Tab = np.array([ 0.12,0.14,0.23,0.63,0.079,0.03 ])
R_series_Lvalue_Tab = np.array([ None,0.013,0.013,0.9,0.013,None ])
R_series_Lvalue_real= np.array([ None,0.013,0.013,0.9,0.013,None])
R_series_values= np.array(np.zeros(6))
R_series_values[R_series_types == "cond"] = R_series_Rvalue_Tab[R_series_types=="cond"] * R_series_Lvalue_real[R_series_types=="cond"]/(R_series_Lvalue_Tab[R_series_types=="cond"]) 
R_series_values[R_series_types == "conv"] = R_series_Rvalue_Tab[R_series_types=="conv"]
R_Wood_tot=R_series_values.sum()
U_Wood_tot=1./R_Wood_tot

#
U_tot=U_Wood_tot*0.25+U_Ins_tot*0.75
Q=U_tot*(Tin-Tout)*A

print "Total U is: " +str(U_tot) + " W*m^2/K"
print("the heat transfer Q though the wall is : "+str(Q)+" W")