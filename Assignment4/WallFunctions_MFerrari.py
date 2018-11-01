def epsilonEffective(epsilon1=0.9,epsilon2=0.9):
    """This is a function that, given two input values for epsilon1 and epsilon2, returns the 
    corresponding epsilon effective."""
    result = 1/(1/epsilon1+1/epsilon2 -1)
    return result
    

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
    ResultDict = {}
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



def HeatTransferCoefficient(R):
    """This is a function which takes the value of a resistance and simply gives the corresponding heat
    transfer coefficient value."""
    U = 1/float(R)
    return U