# -*- coding: utf-8 -*-
#EXAMPLE B
R1=["R_conv1","conv", 0.0, 10, 1.2]
R2=["R_glass","cond", 0.008, 0.78, 1.2]
R3=["R_con2","conv", 0.0, 40, 1.2]

ListOfResistances=[R1,R2,R3]
R_total=0.0
for AnyResistance in ListOfResistances:
	type=AnyResistance[1]
	if type=="cond":
    		L=AnyResistance[2]
    		k=AnyResistance[3]
    		A=AnyResistance[-1]
    		print("Name:" +AnyResistance[0])
    		print("Type:" +AnyResistance[1])
    		print("L=" +str(L))
    		print("k=" +str(k))
    		print("A=" +str(A))
    		resistance_R=float(L)/(float(k)*float(A))
    		print("R=" +str(resistance_R))
    		R_total=R_total+resistance_R
		print("R_total=" +str(R_total))
    		print("________________")

	else:
    		h=AnyResistance[3]
    		A=AnyResistance[-1]
    		print("Name:" +AnyResistance[0])
    		print("Type:" +AnyResistance[1])
    		print("h=" +str(h))
    		print("A=" +str(A))
    		resistance_R=1/(float(h)*float(A))
    		print("R=" +str(resistance_R))
    		R_total=R_total+resistance_R
    		print("R_total=" +str(R_total))
    		print("________________")

T1=20
T2=-10
Q=(T1-T2)/R_total
print("Total heat transfer through the glass is Q[W]=" +str(Q))
R1=1/(10*1.2)
T_inner=T1-Q*R1
print("The temperature of its inner surface is T[ºC]=" +str(T_inner))