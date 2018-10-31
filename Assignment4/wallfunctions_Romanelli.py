ThermalResDict = {"FaceBrick":{"R":0.075,"length":0.1},
                  "WoodStud_90mm":{"R":0.63,"length":0.09},
                  "woodFiberBoard":{"R":0.23,"length":0.013},
                  "woodLappedSiding":{"R":0.14,"length":0.013},
                  "gypsum":{"R":0.079,"length":0.013},
                  "insideSurface":{"R":0.12},
                  "outsidesurfaceWinter":{"R":0.03},
                  "outsidesurfaceSummer":{"R":0.044},
                  "glassfiber":{"R":0.70,"length":0.025},
                  } 
                  
AirGapResDict={0.020:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
                   0.040:{0.03:0.63,0.05:0.59,0.5:0.25}}
                   
                                     
def epsilonEffective(epsilon1=0.05,epsilon2=0.9):

    result=1/(1/epsilon1+1/epsilon2-1)
    return result

def ResistenceWithWood(ResistenceList_withWood):
    Rtot_wood=0
    WoodResults={} 
    
    for anyResistence in ResistenceList_withWood:
        if anyResistence["type"]=="cond":
           material_anyResistence=anyResistence["material"]
           length_anyResistence=anyResistence["length"]
           lengthOfThisMaterialInTheLibrary=ThermalResDict[material_anyResistence]["length"]
           RValue=ThermalResDict[material_anyResistence]["R"]*length_anyResistence/lengthOfThisMaterialInTheLibrary
           WoodResults[anyResistence["name"]]=RValue
           Rtot_wood=Rtot_wood+RValue
        elif anyResistence["type"]=="conv":
            material_anyResistence=anyResistence["material"]
            RValue=ThermalResDict[material_anyResistence]["R"]
            WoodResults[anyResistence["name"]]=RValue
            Rtot_wood=Rtot_wood+RValue
        elif anyResistence["type"]=="gap":
            effectiveEpsilon=epsilonEffective(anyResistence["epsilon1"],anyResistence["epsilon2"])
            RValue_anyResistence=AirGapResDict[anyResistence["length"]][effectiveEpsilon]
            anyResistence["RValue"]=RValue_anyResistence
            WoodResults[anyResistence["name"]]=anyResistence["RValue"]
            Rtot_wood=Rtot_wood+RValue_anyResistence

    WoodResults["Rtot_wood"]=Rtot_wood             
    
    
    print("The total resistence with wood is "+ str(WoodResults["Rtot_wood"])+ " degC/W")
    return WoodResults
    
def ResistenceWithIns(ResistenceList_withInsulation):
    Rtot_ins=0
    InsulationResults={"Rtot_insulation":0}
    for anyResistence in ResistenceList_withInsulation:
        if anyResistence["type"]=="cond":
           material_anyResistence=anyResistence["material"]
           length_anyResistence=anyResistence["length"]
           lengthOfThisMaterialInTheLibrary=ThermalResDict[material_anyResistence]["length"]
           RValue=ThermalResDict[material_anyResistence]["R"]*length_anyResistence/lengthOfThisMaterialInTheLibrary
           InsulationResults[anyResistence["name"]]=RValue
           Rtot_ins=Rtot_ins+RValue
        elif anyResistence["type"]=="conv":
              material_anyResistence=anyResistence["material"]
              RValue=ThermalResDict[material_anyResistence]["R"]
              InsulationResults[anyResistence["name"]]=RValue
              Rtot_ins=Rtot_ins+RValue
        elif anyResistence["type"]=="gap":
              effectiveEpsilon=epsilonEffective(anyResistence["epsilon1"],anyResistence["epsilon2"])
              RValue_anyResistence=AirGapResDict[anyResistence["length"]][effectiveEpsilon] 
              anyResistence["RValue"]=RValue_anyResistence
              InsulationResults[anyResistence["name"]]=anyResistence["RValue"]
              Rtot_ins=Rtot_ins+RValue_anyResistence
              

        
    InsulationResults["Rtot_ins"]=Rtot_ins
    print("The total resistence with insulation is "+ str(InsulationResults["Rtot_ins"])+ " degC/W")
                            
    return InsulationResults
    
                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                           