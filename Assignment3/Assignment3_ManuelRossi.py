#Heat Transfer through a wall with gap

A=50*2.5*0.8  #m^2
DT=24 #K

def epsilonEffective(eps1,eps2):
    result=1/(1/eps1+1/eps2-1)
    return result

ResistanceDict={"Outside_surface":{"R": 0.03}, 
"Wood_bevel_lapped_siding":{"R": 0.14, "length": 0.013},
"Wood_fiberboard_13mm":{"R": 0.23, "length": 0.013},
"Glass_fiber_25mm":{"R":0.7, "length": 0.025},
"Wood_stud_90mm":{"R":0.63, "length": 0.09},
"Gypsum_13mm":{"R":0.079, "length":0.013},
"Inside_surface":{"R":0.12}}

AirGapResDict={0.02:{0.03:0.51,0.05:0.49,0.5:0.23,0.82:0.18},0.04:{0.03:0.45,0.05:0.43,0.5:0.22,0.82:0.16},0.09:{0.03:0.47,0.05:0.45,0.5:0.22,0.82:0.16}}

R_1 = {"name":"outside surface","type":"conv","material":"Outside_surface"}
R_2 = {"name":"wood bevel lapped siding","type":"cond","material":"Wood_bevel_lapped_siding", "length":0.013}
R_3 = {"name":"wood fiberboard sheeting","type":"cond","material":"Wood_fiberboard_13mm", "length":0.013}
R_4 = {"name":"glass fiber insulation","type":"cond","material":"Glass_fiber_25mm", "length":0.09}
R_5 = {"name":"wood stud","type":"cond","material":"Wood_stud_90mm", "length":0.09}
R_6 = {"name":"gypsum wallboard","type":"cond","material":"Gypsum_13mm", "length":0.013}
R_7 = {"name":"inside surface","type":"conv","material":"Inside_surface"}
R_gap = {"name":"air gap","type":"gap","eps1": 0.05, "eps2": 0.9, "length":0.02}

RListFiber = [R_1,R_2,R_3,R_4,R_6,R_7,R_gap]
RListWood = [R_1,R_2,R_3,R_5,R_6,R_7,R_gap]


def ResistanceInSeries(ListOfResistance):
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

Utot=0.25*(1/ResistanceInSeries(RListWood)["Rtot"])+0.75*(1/ResistanceInSeries(RListFiber)["Rtot"])
Rtot=1/Utot

Qtot=Utot*A*DT

print ("U tot: " +str(Utot)+ " W/m^2")
print ("R tot: " +str(Rtot)+ " m^2/W")
print ("Q tot: " +str(Qtot) +(" W"))