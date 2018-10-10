#Example 1: Heat Transfer through a wall

A=50*2.5*0.8  #m^2
DT=24 #K


ResistanceDict={"Outside_surface":{"R": 0.03}, 
"Wood_bevel_lapped_siding":{"R": 0.14, "length": 0.013},
"Wood_fiberboard_13mm":{"R": 0.23, "length": 0.013},
"Glass_fiber_25mm":{"R":0.7, "length": 0.025},
"Wood_stud_90mm":{"R":0.63, "length": 0.09},
"Gypsum_13mm":{"R":0.079, "length":0.013},
"Inside_surface":{"R":0.12}}

R_1 = {"name":"outside surface","type":"conv","material":"Outside_surface"}
R_2 = {"name":"wood bevel lapped siding","type":"cond","material":"Wood_bevel_lapped_siding", "length":0.013}
R_3 = {"name":"wood fiberboard sheeting","type":"cond","material":"Wood_fiberboard_13mm", "length":0.013}
R_4 = {"name":"glass fiber insulation","type":"cond","material":"Glass_fiber_25mm", "length":0.09}
R_5 = {"name":"wood stud","type":"cond","material":"Wood_stud_90mm", "length":0.09}
R_6 = {"name":"gypsum wallboard","type":"cond","material":"Gypsum_13mm", "length":0.013}
R_7 = {"name":"inside surface","type":"conv","material":"Inside_surface"}

RList = [R_1,R_2,R_3,R_4,R_5,R_6,R_7]

RtotWood=0
RtotFiber=0
ResultsFiber={}
ResultsWood={}

for anyR in RList:
    if anyR["type"]=="cond":
        material_anyR = anyR["material"]
        length_anyR = anyR["length"]
        lengthOfThisMaterialInTheLibrary = ResistanceDict[material_anyR]["length"]
        RValue_anyR = ResistanceDict[material_anyR]["R"]*length_anyR/lengthOfThisMaterialInTheLibrary
        anyR["RValue"]=RValue_anyR
        if (material_anyR != "Wood_stud_90mm" and material_anyR != "Glass_fiber_25mm"):
             RtotWood=RtotWood+RValue_anyR
             RtotFiber=RtotFiber+RValue_anyR
             ResultsFiber[anyR["name"]]=anyR["RValue"]
             ResultsWood[anyR["name"]]=anyR["RValue"]
        elif material_anyR=="Glass_fiber_25mm":
            RtotFiber=RtotFiber+RValue_anyR
            ResultsFiber[anyR["name"]]=anyR["RValue"]
            
        elif material_anyR=="Wood_stud_90mm":
            RtotWood=RtotWood+RValue_anyR
            ResultsWood[anyR["name"]]=anyR["RValue"]
            
            
    elif anyR["type"]=="conv":
         material_anyR = anyR["material"]
         RValue_anyR = ResistanceDict[material_anyR]["R"]
         anyR["RValue"]=RValue_anyR
         RtotFiber=RtotFiber+RValue_anyR
         RtotWood=RtotWood+RValue_anyR
         ResultsFiber[anyR["name"]]=anyR["RValue"]
         ResultsWood[anyR["name"]]=anyR["RValue"]
        
       
    else:
        print("Pay attention that this resistance hasn't a valid type")
        print(anyR["name"])
        
ResultsWood["Rtot with Wood"] = RtotWood
ResultsFiber["Rtot without Wood"] = RtotFiber

Utot=0.25*(1/RtotWood)+0.75*(1/RtotFiber)

Rtot=1/Utot

Qtot=Utot*A*DT

print ("U tot: " +str(Utot))
print ("R tot: " +str(Rtot))
print ("Q tot: " +str(Qtot) +(" W"))


