# -*- coding: utf-8 -*-
Tinf1 = 20
Tinf2 = -10
H = 0.8
W = 1.5
A = H*W
R1 = ["R_conv_I" , "conv" , 10 , A]
R2 = ["R_conv_O" , "conv" , 40 , A]
R3 = ["R_glass" , "cond" , 0.004 , 0.78 , A]
R4 = ["R_glass" , "cond" , 0.004 , 0.78 , A]
R5 = ["R_air" , "cond" , 0.01 , 0.026 , A]
R_tot = 0
List = [R1 , R2 , R3 , R4 , R5]

for resistance in List:
    if resistance[1] == "cond":
        L = resistance[2]
        k = resistance[3]
        A = resistance [-1]
        R_thisResistance = float(L)/(k*A)
        resistance.append(R_thisResistance)
    elif resistance[1] == "conv":
        h = resistance[2]
        A = resistance[-1]
        R_thisResistance = 1/(h*A)
        resistance.append(R_thisResistance)   
    else:
        print ("There is something wrong: ")
    R_tot = R_tot + R_thisResistance
print ("The total resistance is: " + str(R_tot) + "C°/W")

Q = A*(Tinf1 - Tinf2)/R_tot
print ("The heat flux through the wall is " + str(Q) + " W ")

T1 = Tinf1 - (Q/A)*R1[-1]
print ("The temperature of the inner wall is " + str(T1) + " °C ")