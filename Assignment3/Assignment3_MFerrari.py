# -*- coding: utf-8 -*-
def epsilonEffective(epsilon1=0.9,epsilon2=0.9):
    """This is a function that, given two input values for epsilon1 and epsilon2, returns the 
    corresponding epsilon effective."""
    result = 1/(1/epsilon1+1/epsilon2 -1)
    return result

#Definition of the list of layers
R1 = {"name":"Outside Surface","type":"conv","material":"OutsideSurfaceWinter"}
R2 = {"name":"Wood Bevel Lapped Siding","type":"cond","material":"WoodLappedSiding","length":0.013}
R3 = {"name":"Fiber Board","type":"cond","material":"WoodFiberboard","length":0.013}
R4 = {"name":"Glass Fiber Insulation","type":"cond","material":"GlassFiberInsulation","length":0.09}
R5 = {"name":"Wood Stud","type":"cond","material":"WoodStud_90mm","length":0.09}
R6 = {"name":"Gypsum Wallboard","type":"cond","material":"Gypsum","length":0.013}
R7 = {"name":"Inside Surface","type":"conv","material":"InsideSurface"}

#I add an air gap of length 40 mm , with epsilon1 equal to 0.05 and epsilon2 equal to 0.9

R_gap = {"name":"Air Gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.04}          

#Initialization of the two different wall structures

ListWithWood = [R1,R2,R3,R5,R6,R7,R_gap] 
ListWithInsulation = [R1,R2,R3,R4,R6,R7,R_gap] 

#Definition of a new function

ResultDict = {}
def ResistanceOfLayersInSeries(ListOfResistances):
    """This function takes a list of layers of a wall as input, for each layer finds the corresponding
    resistance value from a set of data and returns the total resistance value of the entire wall."""
    ThermalResDict = {"GlassFiberInsulation":{"R":0.7, "length":0.025},
    "WoodStud_90mm":{"R":0.63, "length":0.09},
    "InsideSurface":{"R":0.12},
    "OutsideSurfaceWinter":{"R":0.03},
    "Gypsum":{"R":0.079,"length":0.013},
    "WoodLappedSiding":{"R":0.14,"length":0.013},
    "WoodFiberboard":{"R":0.23,"length":0.013},
    }
    AirGapResDict = {0.02:{0.03:0.051,0.05:0.49,0.5:0.23},
    0.04:{0.03:0.063,0.05:0.59,0.5:0.25},
    0.06:{0.03:0.051,0.05:0.49,0.5:0.23}
    }
    Rtot=0
    for any_resistance in ListOfResistances:
        if any_resistance["type"] == "cond":
            Material_resistance = any_resistance["material"]
            Length_resistance = any_resistance["length"]
            ReferenceLength = ThermalResDict[Material_resistance]["length"]
            RValue_resistance = ThermalResDict[Material_resistance]["R"]*Length_resistance/ReferenceLength
            any_resistance["RValue"] = RValue_resistance
            ResultDict[any_resistance["name"]] = any_resistance["RValue"]
        elif any_resistance["type"] == "conv":
            Material_resistance = any_resistance["material"]
            RValue_resistance = ThermalResDict[Material_resistance]["R"]
            any_resistance["RValue"] = RValue_resistance
            ResultDict[any_resistance["name"]] = any_resistance["RValue"]
        elif any_resistance["type"] == "gap":
            EffEpsilon = round(epsilonEffective(any_resistance["epsilon1"],any_resistance["epsilon2"]),2)
            RValue_resistance = AirGapResDict[any_resistance["length"]][EffEpsilon]
            any_resistance["RValue"] = RValue_resistance
            ResultDict[any_resistance["name"]] = any_resistance["RValue"]
        else:
            print ("Error! ")
        Rtot=Rtot+RValue_resistance
        ResultDict["Rtot"]=Rtot
    return ResultDict

#Calculation for the total resistance of the wall in the case of no insulation

ResistanceOfLayersInSeries(ListWithWood) 
RtotWood = ResultDict["Rtot"]

#Calculation for the total resistance of the wall in the case of the presence of insulation

ResultDict = {}
ResistanceOfLayersInSeries(ListWithInsulation)
RtotInsulation = ResultDict["Rtot"]

#Calculation of the heat transfer coefficients and of the overall unit thermal resistance 

def HeatTransferCoefficient(R):
    """This is a function which takes the value of a resistance and simply gives the corresponding heat
    transfer coefficient value."""
    U = 1/R
    return U
UWood = HeatTransferCoefficient(RtotWood)
UInsulation = HeatTransferCoefficient(RtotInsulation)
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

#From the results we can see that with respect to the previous assignment, where there wasn't the air gap,
#the heat flux through the wall, keeping deltaT equal to the previous one, is significantly reduced.
