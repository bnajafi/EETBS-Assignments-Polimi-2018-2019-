# -*- coding: utf-8 -*-
L=0.8
w=1.5
L_glass=0.004
k_glass=0.78
L_air=0.01
k_air=0.026
h1=10
h2=40
T1inf=20
T2inf=-10

A=L*w


R1=["R_glass","cond", L_glass,k_glass,A]
R2=["R_glass","cond", L_glass,k_glass,A]
R3=["R_air","cond", L_air,k_air,A]
R4=["R_in","conv",h1,A]
R5=["R_out","conv",h2,A]

Rtot_cond=0
Rtot_conv=0

ListOfResistances =[R1,R2,R3,R4,R5]

for anyResistance in ListOfResistances :
    if anyResistance[1]=="cond":
        L=anyResistance[2]
        k=anyResistance[3]
        A=anyResistance[-1]
        print("name:"+anyResistance[0])
        print("type:"+anyResistance[1])
        print("L:"+str(L))
        print("k:"+str(k))
        print("A:"+str(A))
        R_condResistance=float(L)/float(k*A)
        print("R:"+str(R_condResistance))
        Rtot_cond=Rtot_cond+R_condResistance
        anyResistance.append(R_condResistance)
    elif anyResistance[1]=="conv":
        h=anyResistance[2]
        A=anyResistance[-1]
        print("name:"+anyResistance[0])
        print("type:"+anyResistance[1])
        print("h:"+str(h))
        print("A:"+str(A))
        R_convResistance=1/float(h*A)
        print("R:"+str(R_convResistance))
        Rtot_conv=Rtot_conv+R_convResistance
        anyResistance.append(R_convResistance)
    else :
        print("Error!") 

print("*****************************")

print("The final total resistance is:")
R_total= Rtot_cond+Rtot_conv
print("R: "+str(R_total)+ " degC/W")

R_conv1=1/float(h1*A)

Q=(T1inf-T2inf)/R_total
T2=T1inf-Q*R_conv1


