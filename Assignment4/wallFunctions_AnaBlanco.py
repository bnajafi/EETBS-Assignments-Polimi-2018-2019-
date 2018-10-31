
ThermalResDict = {"GlassFiberInsulation":{"R":2.52,"length":0.09},
"WoodStud_90mm":{"R":0.63,"length":0.09},
"WoodFiberBoard":{"R":0.23,"length":0.013},
"WoodLappedSiding":{"R":0.14,"length":0.013},
"Gypsum":{"R":0.079,"length":0.013},
"InsideSurface":{"R":0.12},
"OutsideSurface":{"R":0.03}
}

AirGapResDict = {0.02:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
                0.04:{0.03:0.063,0.05:0.59,0.5:0.25},
                0.06:{0.03:0.051,0.05:0.49,0.5:0.23}}


def ResistanceOfWall_wood(ResistanceList_withWood):

                
    def epsilonEffective(epsilon1, epsilon2):
        result=1/(1/epsilon1+1/epsilon2-1)
        return result
    
    result_wood={}
    Rtot_withWood=0

    for AnyResistance in ResistanceList_withWood:
    
        if AnyResistance["type"]=="cond":
            material_AnyResistance=AnyResistance["material"]
            length_AnyResistance=AnyResistance["length"]
            lengthOnLibrary=ThermalResDict[material_AnyResistance]["length"]
            RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]*length_AnyResistance/lengthOnLibrary
            AnyResistance["RValue"]=RValue_AnyResistance
            result_wood[AnyResistance["name"]]=AnyResistance["RValue"]
            Rtot_withWood=Rtot_withWood+RValue_AnyResistance
        elif AnyResistance["type"]=="conv":
            material_AnyResistance=AnyResistance["material"]
            RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]
            AnyResistance["RValue"]=RValue_AnyResistance
            result_wood[AnyResistance["name"]]=AnyResistance["RValue"]
            Rtot_withWood=Rtot_withWood+RValue_AnyResistance
        elif AnyResistance["type"]=="gap":
            epsilon=epsilonEffective(AnyResistance["epsilon1"],AnyResistance["epsilon2"])
            RValue_AnyResistance=AirGapResDict[AnyResistance["length"]][epsilon]
            AnyResistance["RValue"]=RValue_AnyResistance
            result_wood[AnyResistance["name"]]=AnyResistance["RValue"]
            Rtot_withWood=Rtot_withWood+RValue_AnyResistance
            result_wood["Rtot_withWood"]=Rtot_withWood
    print(result_wood)
    return result_wood
    

def ResistanceOfWall_insulation(ResistanceList_withInsulation):
    
    def epsilonEffective(epsilon1, epsilon2):
        result=1/(1/epsilon1+1/epsilon2-1)
        return result
    
    
    
    result_insulation={}
    Rtot_withInsulation=0

    for AnyResistance in ResistanceList_withInsulation:
    
        if AnyResistance["type"]=="cond":
            material_AnyResistance=AnyResistance["material"]
            length_AnyResistance=AnyResistance["length"]
            lengthOnLibrary=ThermalResDict[material_AnyResistance]["length"]
            RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]*length_AnyResistance/lengthOnLibrary
            AnyResistance["RValue"]=RValue_AnyResistance
            result_insulation[AnyResistance["name"]]=AnyResistance["RValue"]
            Rtot_withInsulation=Rtot_withInsulation+RValue_AnyResistance
        elif AnyResistance["type"]=="conv":
            material_AnyResistance=AnyResistance["material"]
            RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]
            AnyResistance["RValue"]=RValue_AnyResistance
            result_insulation[AnyResistance["name"]]=AnyResistance["RValue"]
            Rtot_withInsulation=Rtot_withInsulation+RValue_AnyResistance
        elif AnyResistance["type"]=="gap":
            epsilon=epsilonEffective(AnyResistance["epsilon1"],AnyResistance["epsilon2"])
            RValue_AnyResistance=AirGapResDict[AnyResistance["length"]][epsilon]
            AnyResistance["RValue"]=RValue_AnyResistance
            result_insulation[AnyResistance["name"]]=AnyResistance["RValue"]
            Rtot_withInsulation=Rtot_withInsulation+RValue_AnyResistance
            result_insulation["Rtot_withInsulation"]=Rtot_withInsulation
    
    return result_insulation


