#
Tin=22       #Temperature in the inside
Tout=-2     #Temperature in the outside
A=50*2.5*0.8 #Portion of area made by wall
A_wood=A*0.25 
A_fiber=A*0.75

ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}
                }
                
R1={"name":"Outside Air","type":"conv","A":A}
R2={"name":"Wood Bevel Lapped Siding","type":"cond","l":0.013,"area":A}
R3={"name":"Wood Fiberboard","type":"cond","l":0.013,"area":A}
R4={"name":"Glass Fiber Insulation","type":"cond","l":0.09,"area":A}
R5={"name":"Wood Stud","type":"cond","l":0.9,"area":A}
R6={"name":"Gypsum","type":"cond","l":0.013,"area":A}
R7={"name":"Inside Air","type":"conv","area":A}

#With Wood Resistance
R_tot1=0
resistancesListWithWood=[R1,R2,R3,R5,R6,R7]
resistanceListFiberGlass=[R1,R2,R3,R4,R6,R7]
for anyresistance in resistancesListWithWood:
    if anyresistance["type"]=="cond":
        material=anyresistance["name"]
        length=anyresistance["l"]
        resistance=ThermalResDict[material]["R"]*length/ThermalResDict[material]["l"]
        R_tot1=R_tot1+resistance
    elif anyresistance["type"]=="conv":
        material=anyresistance["name"]
        resistance=ThermalResDict[material]["R"]
        R_tot1=R_tot1+resistance
    else: 
        print("It seems that there is a problem with the resistance")
        print(anyresistance["name"])

#With Fiber Resistance
R_tot2=0
for anyresistance in resistanceListFiberGlass:
    if anyresistance["type"]=="cond":
        material=anyresistance["name"]
        length=anyresistance["l"]
        resistance=ThermalResDict[material]["R"]*length/ThermalResDict[material]["l"]
        R_tot2=R_tot2+resistance
    elif anyresistance["type"]=="conv":
        material=anyresistance["name"]
        resistance=ThermalResDict[material]["R"]
        R_tot2=R_tot2+resistance
    else: 
        print("It seems that there is a problem with the resistance")
        print(anyresistance["name"])

U1=1/float(R_tot1)
U2=1/float(R_tot2)
U_overall=U1*0.25+U2*0.75
Q=U_overall*(Tin-Tout)*A


