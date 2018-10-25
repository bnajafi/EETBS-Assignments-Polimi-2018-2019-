# -*- coding: utf-8 -*-
#Heat Transfer through a wall

A=50*2.5*0.8  #m^2
DT=24 #K

import numpy as np

Res_names=np.array(["outside_surface", "wood_bevel_lapped_siding", "wood_fiberboard_sheeting","glass_fiber_insulation","wood_stud", "gypsum_wallboard", "inside_surface" ])
Res_types=np.array(["conv","cond","cond","cond","cond","cond", "conv"])

Res_LReal=np.array([None, 0.013, 0.013, 0.09, 0.09 ,0.013, None ])
Res_LDict=np.array([None, 0.013, 0.013, 0.025, 0.09 ,0.013, None ])
Res_RValuesDict=np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])

Res_RValues=np.array(np.zeros(7))
Res_RValues[Res_types=="cond"]=Res_LReal[Res_types=="cond"]/Res_LDict[Res_types=="cond"]*Res_RValuesDict[Res_types=="cond"]
Res_RValues[Res_types=="conv"]=Res_RValuesDict[Res_types=="conv"]

index_wood=Res_names!="glass_fiber_insulation"
index_fiber=Res_names!="wood_stud"

Res_totWood=Res_RValues[index_wood].sum()
Res_totFiber=Res_RValues[index_fiber].sum()

Utot=0.25*(1/Res_totWood)+0.75*(1/Res_totFiber)

Rtot=1/Utot

Qtot=Utot*A*DT

print ("U tot: " +str(Utot) +" W/(°C*m^2)" )
print ("R tot: " +str(Rtot) +" °C/W")
print ("Q tot: " +str(Qtot) +" W")


