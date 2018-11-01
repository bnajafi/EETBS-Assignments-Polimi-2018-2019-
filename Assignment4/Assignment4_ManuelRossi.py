#New way ro import funcions

A=50*2.5*0.8  #m^2
DT=24 #K

R_1 = {"name":"outside surface","type":"conv","material":"Outside_surface"}
R_2 = {"name":"wood bevel lapped siding","type":"cond","material":"Wood_bevel_lapped_siding", "length":0.013}
R_3 = {"name":"wood fiberboard sheeting","type":"cond","material":"Wood_fiberboard_13mm", "length":0.013}
R_4 = {"name":"glass fiber insulation","type":"cond","material":"Glass_fiber_25mm", "length":0.09}
R_5 = {"name":"wood stud","type":"cond","material":"Wood_stud_90mm", "length":0.09}
R_6 = {"name":"gypsum wallboard","type":"cond","material":"Gypsum_13mm", "length":0.013}
R_7 = {"name":"inside surface","type":"conv","material":"Inside_surface"}
R_gap = {"name":"air gap","type":"gap","eps1": 0.05, "eps2": 0.9, "length":0.02}

RListFiber = [R_1,R_2,R_3,R_4,R_6,R_7,R_gap]
RListWood = [R_1,R_2,R_3,R_5,R_6,R_7,R_gap]
#RList_in_parallel=[{"name":RListFiber, "percentage":0.75},{"name":RListWood, "percentage":0.25}]


import os
import sys
thisFileDirectory = os.path.dirname(sys.argv[0])
os.chdir(thisFileDirectory)
#print os.getcwd()


### First way

import WallFunctions_ManuelRossi as WallF

RList_in_parallel=[{"name":RListFiber, "percentage":0.75},{"name":RListWood, "percentage":0.25}]

Utot1=WallF.Calculate_Utot(RList_in_parallel)
Rtot1=1/Utot1
Qtot1=Utot1*A*DT

print ("U tot1: " +str(Utot1)+ " W/m^2")
print ("R tot1: " +str(Rtot1)+ " m^2/W")
print ("Q tot1: " +str(Qtot1) +(" W"))


### Second way

from WallFunctions_ManuelRossi import Calculate_Utot

RList_in_parallel=[{"name":RListFiber, "percentage":0.75},{"name":RListWood, "percentage":0.25}]

Utot2=WallF.Calculate_Utot(RList_in_parallel)
Rtot2=1/Utot2
Qtot2=Utot2*A*DT

print ("U tot2: " +str(Utot2)+ " W/m^2")
print ("R tot2: " +str(Rtot2)+ " m^2/W")
print ("Q tot2: " +str(Qtot2) +(" W"))