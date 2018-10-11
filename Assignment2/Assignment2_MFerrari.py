# -*- coding: utf-8 -*-
#Definition of the table for the resistances
ThermalResDict = {"GlassFiberInsulation":{"R":0.7, "length":0.025},
"WoodStud_90mm":{"R":0.63, "length":0.09},
"InsideSurface":{"R":0.12},
"OutsideSurfaceWinter":{"R":0.03},
"Gypsum":{"R":0.079,"length":0.013},
"WoodLappedSiding":{"R":0.14,"length":0.013},
"WoodFiberboard":{"R":0.23,"length":0.013}
}
#Definition of the list of resistances
R1 = {"name":"Outside Surface","type":"conv","material":"OutsideSurfaceWinter"}
R2 = {"name":"Wood Bevel Lapped Siding","type":"cond","material":"WoodLappedSiding","length":0.013}
R3 = {"name":"Fiber Board","type":"cond","material":"WoodFiberboard","length":0.013}
R4 = {"name":"Glass Fiber Insulation","type":"cond","material":"GlassFiberInsulation","length":0.09}
R5 = {"name":"Wood Stud","type":"cond","material":"WoodStud_90mm","length":0.09}
R6 = {"name":"Gypsum Wallboard","type":"cond","material":"Gypsum","length":0.013}
R7 = {"name":"Inside Surface","type":"conv","material":"InsideSurface"}
RTotWood = 0
RTotInsulation = 0
#Calculation of the equivalent resistance in the case of only wood stud in the internal layer
ListWithWood = [R1,R2,R3,R5,R6,R7]
for any_resistance in ListWithWood:
    if any_resistance["type"] == "cond":
            Material_resistance = any_resistance["material"]
            Length_resistance = any_resistance["length"]
            ReferenceLength = ThermalResDict[Material_resistance]["length"]
            RValue_resistance = ThermalResDict[Material_resistance]["R"]*Length_resistance/ReferenceLength
            any_resistance["RValue"] = RValue_resistance
    elif any_resistance["type"] == "conv":
            Material_resistance = any_resistance["material"]
            RValue_resistance = ThermalResDict[Material_resistance]["R"]
            any_resistance["RValue"] = RValue_resistance
    else:
            print ("Error! ")
    RTotWood = RTotWood + RValue_resistance
#Calculation of the equivalent resistance in the case of only insulation in the internal layer
ListWhithInsulation = [R1,R2,R3,R4,R6,R7]
for any_resistance in ListWhithInsulation:
    if any_resistance["type"] == "cond":
            Material_resistance = any_resistance["material"]
            Length_resistance = any_resistance["length"]
            ReferenceLength = ThermalResDict[Material_resistance]["length"]
            RValue_resistance = ThermalResDict[Material_resistance]["R"]*Length_resistance/ReferenceLength
            any_resistance["RValue"] = RValue_resistance
    elif any_resistance["type"] == "conv":
            Material_resistance = any_resistance["material"]
            RValue_resistance = ThermalResDict[Material_resistance]["R"]
            any_resistance["RValue"] = RValue_resistance
    else:
            print ("Error! ")
    RTotInsulation = RTotInsulation + RValue_resistance
#Calculation of the heat transfer coefficients and of the overall unit thermal resistance 
UWood = 1/RTotWood
UInsulation = 1/RTotInsulation
UWall = UWood*0.25 + UInsulation*0.75
RWall = 1/UWall
#Calculation of the heat flux through the wall
T_IN = 22
T_OUT = -2
DT = (T_IN - T_OUT)
A = 50*(1-0.2)*2.5
Q = UWall*A*DT
#Print the results
print ("The overall heat transfer coefficient of the wall is: " + str(UWall) + " W/(m^2°C)")
print ("The overall thermal resistance of the wall is " + str(RWall) + " (m^2°C)/W")
print ("The heat flux through the wall is " + str(Q) + " W")
