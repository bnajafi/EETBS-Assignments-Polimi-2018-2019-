#wallFunctions

def epsilonEffective(epsilon1=0.9, epsilon2=0.9):
    """ This function simply calculates the epsilon effective """
    result=1/(1/epsilon1+1/epsilon2-1)
    return result



def ResistanceOfLayersInSeries(ListOfResistances):
    ThermalResDict={"FaceBrick":{"R":0.075, "length":0.1}, 
    "Gypsum":{"R":0.079, "length":0.013}, 
    "woodStud_90mm":{"R":0.36, "length":0.09}, 
    "woodFiberBoard":{"R":0.23, "length":0.013},
    "woodLappedSiding":{"R":0.14, "length":0.013},
    "glassFiberInsulation":{"R":0.7, "length":0.025},
    "insideSurface":{"R":0.12},
    "outsideSurfaceWinter":{"R":0.03},
    "outsideSurfaceSummer":{"R":0.044}} 
    
    AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23}, 
    0.040:{0.03:0.063,0.05:0.59,0.5:0.25}} 
    
    ResultsDictionary= {}
    Rtot=0
    for anyResistance in ListOfResistances:
        if anyResistance["type"]== "cond":
            material_anyResistance= anyResistance["material"]
            length_anyResistance= anyResistance["length"]
            lengthOfThisMaterialInTheLibrary= ThermalResDict[material_anyResistance]["length"]
            RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
            anyResistance["RValue"]=RValue_anyResistance
            ResultsDictionary[anyResistance["name"]]=anyResistance["RValue"]
        elif anyResistance["type"]== "conv":
            material_anyResistance= anyResistance["material"]
            RValue_anyResistance= ThermalResDict[material_anyResistance]["R"]
            anyResistance["RValue"]=RValue_anyResistance
            ResultsDictionary[anyResistance["name"]]=anyResistance["RValue"]
        elif anyResistance["type"]== "gap":
            effectiveEpsilon=round(epsilonEffective(anyResistance["epsilon1"],anyResistance["epsilon2"]),2)
            RValue_anyResistance=AirGapResDict[anyResistance["length"]][effectiveEpsilon] 
            anyResistance["RValue"]=RValue_anyResistance
            ResultsDictionary[anyResistance["name"]]=anyResistance["RValue"]
            
        Rtot=Rtot+RValue_anyResistance
        ResultsDictionary["Rtot"]=Rtot
    return ResultsDictionary
    







