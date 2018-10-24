#Assignment 3
Tin=2
Tout=-2
A=50*0.8 
A_wood=A*0.25    #25%
A_fiber=A*0.75   #75%

ThermalResDic={"FaceBrick":{"R":0.075,"lenght":0.1}
,"WoodStud_90mm":{"R":0.36,"lenght":0.09}
,"WoodFiberBoard":{"R":0.24,"lenght":0.013}
,"GlassFiberIsulation":{"R":0.7,"lenght":0.025}
,"WoodLappedSiding":{"R":0.14,"lenght":0.013}
,"Gypsum":{"R":0.079,"lenght":0.013}
,"InsideAir":{"R":0.12}
,"outsideSurfaceWinter":{"R":0.03}
,"outsideSurfaceSummer":{"R":0.044}
}

Ri={"name":"Inside Air","type":"conv","material":"InsideAir","area":A}
R1={"name":"Wood blevel lapped Siding","type":"cond","material":"WoodLappedSiding","area":A,"lenght":0.013}
R2={"name":"WoodFiberBoard","type":"cond","material":"WoodFiberBoard","area":A,"lenght":0.013}
R3={"name":"Glass Fiber Insulation","type":"cond","material":"GlassFiberIsulation","area":A,"lenght":0.09}
R4={"name":"WoodStud_90mm","type":"cond","material":"WoodStud_90mm","area":A,"lenght":0.9}
R5={"name":"Gypsum Wallboard","type":"cond","material":"Gypsum","area":A,"lenght":0.013}
Ro={"name":"OutSide Surface","type":"conv","material":"outsideSurfaceWinter","area":A}

#with Wood Resistance

Rtot1=0
Rtot2=0
R_Wood=[Ri,R1,R2,R4,R5,Ro]
R_Ins=[Ri,R1,R2,R3,R5,Ro]

for Ri in R_Wood:
    if Ri["type"]=="cond":
        material=Ri["material"]
        lenght=Ri["lenght"]
        R_Value= ThermalResDic[material]["R"]*lenght/ThermalResDic[material]["lenght"]
        Rtot1=Rtot1+R_Value
        print("resistence's type "+str(Ri["type"]))
        print("material "+str(Ri["material"]))
        print("R= "+str(R_Value))
        print("**********************")
    elif Ri["type"]=="conv":
        material=Ri["material"]
        R_Value= ThermalResDic[material]["R"]
        Rtot1=Rtot1+R_Value
        print("resistence's type "+str(Ri["type"]))
        print("material "+str(Ri["material"]))
        print("R= "+str(R_Value))
        print("**********************")
    else :
        print("the resitance "+str(Ri["name"])+"has its type not corretly define")
print("the total resisance value with wood is "+str(Rtot1)+" ohm")

for Ri in R_Ins:
    if Ri["type"]=="cond":
        material=Ri["material"]
        lenght=Ri["lenght"]
        R_Value= ThermalResDic[material]["R"]*lenght/ThermalResDic[material]["lenght"]
        Rtot2=Rtot2+R_Value
        print("resistence's type "+str(Ri["type"]))
        print("material "+str(Ri["material"]))
        print("R= "+str(R_Value))
        print("**********************")
    elif Ri["type"]=="conv":
        material=Ri["material"]
        R_Value= ThermalResDic[material]["R"]
        Rtot2=Rtot2+R_Value
        print("resistence's type "+str(Ri["type"]))
        print("material "+str(Ri["material"]))
        print("R= "+str(R_Value))
        print("**********************")
    else :
        print("the resitance "+str(Ri["name"])+"has its type not corretly define")
print("the total resisance value with isulation is "+str(Rtot2)+" ohm")

U1=1/float(Rtot1)
U2=1/float(Rtot2)
Utot=U1*0.25+U2*0.75
Q=Utot*(Tin-Tout)*A
print("the heat transfer thought the wall is : "+str(Q)+"W")
