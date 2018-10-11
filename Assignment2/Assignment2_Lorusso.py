# -*- coding: utf-8 -*-
#Assignment 2
#Exemple B 

R1 = {
    "name":"R_Indoor","type":"conv",
    "h":10,"wall_height":0.8,"wall_wide":1.5
    }
R2 = {
    "name":"R_glass_Indoor","type":"cond","lenght":0.004,
    "k":0.78,"wall_height":0.8,"wall_wide":1.5
    }
R3 = {
    "name":"R_gap_StagnantAir","type":"cond","lenght":0.01,
    "k":0.026,"wall_height":0.8,"wall_wide":1.5
    }
R4 = {
    "name":"R_glass_Outdoor","type":"cond","lenght":0.004,
    "k":0.78,"wall_height":0.8,"wall_wide":1.5
    }
R5 = {
    "name":"R_Outdoor","type":"conv",
    "h":40,"wall_height":0.8,"wall_wide":1.5
    }

ListOfResistances= [R1,R2,R3,R4,R5]
Rtot=0

#Determine the steady rate of heat transfer throgh the wall
#Determine the temperature of its inner surface

for Ri in ListOfResistances:
    if Ri["type"] == "conv":
        A=Ri["wall_height"]*Ri["wall_wide"]
        Ri["Area"]=A
        print("name: "+Ri["name"])
        print("type: "+Ri["type"])
        print("h: "+str(Ri["h"])+" W/(m*°C)")
        print("A: "+str(Ri["Area"])+" m^2")
        R_thisResistance= 1/(Ri["h"]*Ri["Area"])
        Ri["RValue"]=R_thisResistance
        Rtot=Rtot+R_thisResistance
        print(str(Ri["name"])+"= "+str(Ri["RValue"])+ " °C/W")
        print("**********************************")
    elif Ri["type"] == "cond":
        A=Ri["wall_height"]*Ri["wall_wide"]
        Ri["Area"]=A 
        print("name: "+Ri["name"])
        print("type: "+Ri["type"])
        print("L: "+str(Ri["lenght"])+" m")
        print("k: "+str(Ri["k"])+" W/(m*°C)")
        print("A: "+str(Ri["Area"])+" m^2")
        R_thisResistance=float(Ri["lenght"])/(Ri["k"]*Ri["Area"])
        Ri["RValue"]=R_thisResistance
        Rtot=Rtot+R_thisResistance
        print(str(Ri["name"])+"= "+str(Ri["RValue"])+ " °C/W")
        print("**********************************")
    else:
        print("Pay attention that the resistence "+Ri["name"]+" has is type  corretly definite")
print("Rtotal: "+str(Rtot)+ " °C/W")
ListOfResistances.append(Rtot)

T0 = {
    "name":"T_indoor","TValue":20,"unit":"Celsius"
}
T1 = {
    "name":"T_InnerSurface","unit":"Celsius"
}
T2 = {
    "name":"T_Glass_StagnantAir","unit":"Celsius"
}
T3 = {
    "name":"T_StagnatAir_Glass","unit":"Celsius"
}
T4 = {
    "name":"T_OutsideSurface","unit":"Celsius"
}
T5 = {
    "name":"T_Outdoor","TValue":-10,"unit":"Celsius"
}
T=[T0,T1,T2,T3,T4,T5]

Q=float(T[0]["TValue"]-T[-1]["TValue"])/Rtot #W

T1["TValue"]=T0["TValue"]-Q*R1["RValue"]
T2["TValue"]=T1["TValue"]-Q*R2["RValue"]
T3["TValue"]=T2["TValue"]-Q*R3["RValue"]
T4["TValue"]=T3["TValue"]-Q*R4["RValue"]

print"Q [W] value : "+str (Q)
print"T1 [°C] inner surface value: "+str (T1["TValue"])
print"T4 [°C] outside surface value: "+str (T4["TValue"])