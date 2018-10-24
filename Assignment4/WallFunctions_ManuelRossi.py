


def epsilonEffective(eps1,eps2):
    result=1/(1/eps1+1/eps2-1)
    return result

def ResistanceInSeries(ListOfResistance):
    ResistanceDict={"Outside_surface":{"R": 0.03}, 
"Wood_bevel_lapped_siding":{"R": 0.14, "length": 0.013},
"Wood_fiberboard_13mm":{"R": 0.23, "length": 0.013},
"Glass_fiber_25mm":{"R":0.7, "length": 0.025},
"Wood_stud_90mm":{"R":0.63, "length": 0.09},
"Gypsum_13mm":{"R":0.079, "length":0.013},
"Inside_surface":{"R":0.12}}
   

    AirGapResDict={0.02:{0.03:0.51,0.05:0.49,0.5:0.23,0.82:0.18},0.04:{0.03:0.45,0.05:0.43,0.5:0.22,0.82:0.16},0.09:{0.03:0.47,0.05:0.45,0.5:0.22,0.82:0.16}}

    Rtot=0
    Results={}
    for anyR in ListOfResistance:
        if anyR["type"]=="cond":
            material_anyR = anyR["material"]
            length_anyR = anyR["length"]
            lengthOfThisMaterialInTheLibrary = ResistanceDict[material_anyR]["length"]
            RValue_anyR = ResistanceDict[material_anyR]["R"]*length_anyR/lengthOfThisMaterialInTheLibrary
            anyR["RValue"]=RValue_anyR
            Rtot=Rtot+RValue_anyR
            Results[anyR["name"]]=anyR["RValue"]
        
        elif anyR["type"]=="conv":
            material_anyR = anyR["material"]
            RValue_anyR = ResistanceDict[material_anyR]["R"]
            anyR["RValue"]=RValue_anyR
            Rtot=Rtot+RValue_anyR
            Results[anyR["name"]]=anyR["RValue"]
        
        elif anyR["type"]=="gap":
            effectiveEps=round(epsilonEffective(anyR["eps1"],anyR["eps2"]),2)
            RValue_anyR=AirGapResDict[anyR["length"]][effectiveEps]
            anyR["RValue"]=RValue_anyR
            Rtot=Rtot+RValue_anyR
            Results[anyR["name"]]=anyR["RValue"]
       
        else:
            print("Pay attention that this resistance hasn't a valid type")
            print(anyR["name"])
        
    return {"Rtot":Rtot,"Results":Results}


def Calculate_Utot(RListparallel):
     UTot=0
     for anyList in RListparallel:
         UTot=UTot+anyList["percentage"]*1/ResistanceInSeries(anyList["name"])["Rtot"] #Important: wtrite brackets in right positions
     return  UTot