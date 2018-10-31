# -*- coding: utf-8 -*-
#Example_B new method
L=0.8 #m
w=1.5 #m
L_glass=0.004 #m
k_glass=0.78 #W/(°C*m)
L_air=0.01 #m
k_air=0.026 #W/(°C*m)
h1=10 #W/(°C*m^2)
h2=40 #W/(°C*m^2)
T1inf=20 #°C
T2inf=-10 #°C

A=L*w #m^2
 
R1=["R_int","conv", 8.9, A]
R2=["R_foam","cond", 0.06, 0.05,A]
R3=["R_wood","cond", 0.1, 0.4,A]
R4=["R_plaster","cond",0.01,1,A ]
R5=["R_ext","conv", 20, A]
import numpy as np

Res_names=np.array(["R_int", "R_foam", "R_wood","R_plaster","R_ext" ])
Res_types=np.array(["conv","cond","cond","cond", "conv"])
Res_k=np.array([None, 0.06,0.1,0.01, None ])
Res_L=np.array([None, 0.05,0.4,1, None ])
Res_A=np.array([15,15,15,15,15])
Res_h=np.array([8.9, None, None, None, 20 ])

Res_RValues=np.array(np.zeros(5))
Res_RValues[Res_types=="cond"]=Res_L[Res_types=="cond"]/(Res_A[Res_types=="cond"]*Res_k[Res_types=="cond"])
Res_RValues[Res_types=="conv"]=1.0/(Res_A[Res_types=="conv"]*Res_h[Res_types=="conv"])
Res_tot=Res_RValues.sum()


Rtot_cond=0
Rtot_conv=0

ListR=[R1,R2,R3,R4,R5]
print ("The area is common to each layer and its value is: " +str(A))
print ("The list of resistances are: ")
for anyR in ListR:
    if anyR [1]=="cond":
        L=anyR[2]
        k=anyR[-1]
        print("* name: "+anyR[0])
        print("  type: "+anyR[1])
        print("  L: "+str(L))
        print("  k: "+str(k))
        R_cond=float(L)/float(k*A)
        print("  R: " +str(R_cond))
        Rtot_cond=Rtot_cond+R_cond
        anyR.append(R_cond)
    elif anyR [1]=="conv":
        h=anyR[-1]
        print("* name: "+anyR[0])
        print("  type: "+anyR[1])
        print("  h: "+str(h))
        R_conv=1/float(h*A)
        print("  R: " +str(R_conv))
        Rtot_conv=Rtot_conv+R_conv
        anyR.append(R_conv)
    else: print("Error")
    
print ("-----------------------")

print ("The total resistance is: ")
R_tot=Rtot_cond+Rtot_conv
print("Rtot: " +str(R_tot) +"°C/W")
