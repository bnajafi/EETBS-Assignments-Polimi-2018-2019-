# -*- coding: utf-8 -*-
#Assigment 1
#Exemple B

R1= ["R_in","conv",10,0.8,1.5] #R_conv=["R","conv",h,wall_height,wall_wide]
R2= ["R_glass","cond",0.78,0.8,1.5,0.008] #R_cond=["R","cond",k,wall_height,wall_wide,L]
R3= ["R_out","conv",40,0.8,1.5]
ListOfResistances= [R1,R2,R3]
Rtot=0

#Determine the steady rate of heat transfer throgh the glass
#Determine the temperature of its inner surface

for Ri in ListOfResistances:
    if Ri[1] == "conv":
        h=Ri[2]
        wall_height=Ri[3]
        wall_wide=Ri[-1]
        A=wall_height*wall_wide
        print("name: "+Ri[0])
        print("type: "+Ri[1])
        print("h: "+str(h)+" W/(m*°C)")
        print("A: "+str(A)+" m^2")
        R_thisResistance= 1/(h*A)
        Rtot=Rtot+R_thisResistance
        Ri.append(R_thisResistance)
        print(str(Ri[0])+"= "+str(R_thisResistance)+ " °C/W")
        print("**********************************")
    else :
        k=Ri[2]
        wall_height=Ri[3]
        wall_wide=Ri[4]
        L= Ri[-1]
        A=wall_height*wall_wide
        print("name: "+Ri[0])
        print("type: "+Ri[1])
        print("L: "+str(L)+" m")
        print("k: "+str(k)+" W/(m*°C)")
        print("A: "+str(A)+" m^2")
        R_thisResistance=float(L)/(k*A)
        Rtot=Rtot+R_thisResistance
        Ri.append(R_thisResistance)
        print(str(Ri[0])+"= "+str(R_thisResistance)+ " °C/W")
        print("**********************************")
print("Rtotal: "+str(Rtot)+ " °C/W")

T_in=20 #°C
T_out=-10 #°C
T=[T_in,T_out]

Q=float(T[0]-T[-1])/Rtot #W

T1=T[0]-Q*R1[-1]
T2=T1-Q*R2[-1]
T.append(T1)
T.append(T2)

print"Q [W] value : "+str (Q)
print"T1 [°C] inner surface value: "+str (T[2])
print"T2 [°C] outside surface value: "+str (T[3])