#assignment3
#funaro_eleonora


Awood=0.25
Ainsulation=0.75
Atot=100 
dT=24


def epsilonEffective(epsilon1, epsilon2):
    result=1/(1/epsilon1+1/epsilon2-1)
    return result

R_1 = {"name":"glass fiber","type":"cond","material":"glass_fiber", "length":0.09}
R_2 = {"name":"wood stud","type":"cond","material":"woodStud_90mm", "length":0.09}
R_3 = {"name":"wood fiber board","type":"cond","material":"woodFiberBoard", "length":0.013}
R_4 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}
R_5 = {"name":"gypsum wallboard","type":"cond","material":"gypsum", "length":0.013}
R_i = {"name":"inside surface","type":"conv","material":"insideSurface"}
R_o = {"name":"outside surface","type":"conv","material":"outsideSurface"}
R_gap = {"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

ResistanceList_withWood = [R_2,R_3,R_4,R_5,R_i,R_o,R_gap]
ResistanceList_withInsulation = [R_1,R_3,R_4,R_5,R_i,R_o,R_gap]

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
   
    
DictWood=ResistanceOfLayersInSeries(ResistanceList_withWood)
Rwood=DictWood['Rtot']
print("R Wood: " +str(Rwood))

DictGlass=ResistanceOfLayersInSeries(ResistanceList_withInsulation)
Rinsulation=DictGlass['Rtot']
print("R Insulation: " +str(Rinsulation))


Uinsulation=1/Rinsulation
Uwood=1/Rwood
Utot=(Uinsulation*Ainsulation)+(Uwood*Awood)
RTot=1/Utot

print("R Tot: " +str(RTot))

Q=(Atot*dT)/RTot
        
print("Q: " +str(Q)) 




