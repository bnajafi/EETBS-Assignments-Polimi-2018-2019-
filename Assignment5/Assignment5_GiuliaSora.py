# -*- coding: utf-8 -*-
Tin=22       #Temperature in the inside
Tout=-2     #Temperature in the outside
A=50*2.5*0.8 #Portion of area made by wall


import numpy as np
ResistanceName=np.array(["Outside Air","Wood Bevel Lapped Siding","Wood Fiberboard","Wood Stud","Gypsum","Inside Air"])
ResistanceType=np.array(["conv","cond","cond","cond","cond","conv"])
ResistanceR=np.array([0.03,0.14,0.23,0.63,0.079,0.12])
RtotWood=ResistanceR.sum()
ResistanceNameFiber=np.array(["Outside Air","Wood Bevel Lapped Siding","Wood Fiberboard","Glass Fiber Insulation","Gypsum","Inside Air"])
Resistance_fiber=np.array([0.03,0.14,0.23,2.52,0.079,0.12])
RtotFiber=Resistance_fiber.sum()
U=np.array([1/RtotWood,1/RtotFiber])
Areas=np.array([25,75])
A_tot=np.array([100,100])
Utot=(U*Areas/A_tot).sum()
Q=Utot*(Tin-Tout)*A
print ("La U totale è: "+str(Utot))
print ("La Q totale è: "+str(Q))
