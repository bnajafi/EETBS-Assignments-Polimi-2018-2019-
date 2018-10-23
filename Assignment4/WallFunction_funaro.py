#assignment4
#funaro_eleonora


def epsilonEffective(epsilon1, epsilon2):
    result=1/(1/epsilon1+1/epsilon2-1)
    return result
    

def ResistanceOfLayersInSeries(ListOfResistances):
    ThermalResDict = {"glass_fiber":{"R":0.7, "length":0.025}
    , "woodStud_90mm":{"R":0.63, "length":0.09}
    , "woodFiberBoard":{"R":0.23, "length":0.013}
    , "woodLappedSiding":{"R":0.14, "length":0.013}
    , "gypsum":{"R":0.079, "length":0.013}
    , "insideSurface":{"R":0.12}
    , "outsideSurface":{"R":0.03}
    }
    
    AirGapResDict={0.020:{0.03:0.51,0.049723756906077346:0.49,0.5:0.23},
                   0.040:{0.03:0.63,0.05:0.59,0.5:0.25}}
                   
    ResultsDictionary={}
    Rtot=0
    for anyResistance in ListOfResistances:
        if anyResistance["type"]=="cond":
            material_anyResistance = anyResistance["material"]
            length_anyResistance = anyResistance["length"]
            lengthOfThisMaterialInTheLibrary = ThermalResDict[material_anyResistance]["length"]
            RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
            anyResistance["RValue"]=RValue_anyResistance
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
            Rtot=Rtot+RValue_anyResistance
        elif anyResistance["type"]=="conv":
            material_anyResistance = anyResistance["material"]
            RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]
            anyResistance["RValue"]=RValue_anyResistance   
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
            Rtot=Rtot+RValue_anyResistance
        elif anyResistance["type"]=="gap":
            effectiveEpsilon=epsilonEffective(anyResistance["epsilon1"],anyResistance["epsilon2"])
            RValue_anyResistance = AirGapResDict[anyResistance["length"]][effectiveEpsilon]
            anyResistance["RValue"]=RValue_anyResistance 
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
            Rtot=Rtot+RValue_anyResistance
    ResultsDictionary["Rtot"]=Rtot
    return ResultsDictionary