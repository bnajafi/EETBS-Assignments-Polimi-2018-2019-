#some important resistences in a dictionary
ThermalResDict = {"FaceBrick":{"R":0.075,"length":0.1},
                  "WoodStud_90mm":{"R":0.63,"length":0.09},
                  "woodFiberBoard":{"R":0.23,"length":0.013},
                  "woodLappedSiding":{"R":0.14,"length":0.013},
                  "gypsum":{"R":0.079,"length":0.013},
                  "insideSurface":{"R":0.12},
                  "outsidesurfaceWinter":{"R":0.03},
                  "outsidesurfaceSummer":{"R":0.044},
                  "glassfiber":{"R":0.70,"length":0.025}}   

#resistences that we need
R_1={"name":"outside surface","type":"conv","material":"outsidesurfaceWinter"}
R_2={"name":"wood bevel lapped siding","type":"cond","material":"woodLappedSiding","length":0.013}
R_3={"name":"fiberboard","type":"cond","material":"woodFiberBoard","length":0.013}
R_4a={"name":"glass fiber insulation","type":"cond","material":"glassfiber","length":0.09}
R_4b={"name":"wood stud","type":"cond","material":"WoodStud_90mm","length":0.09}
R_5={"name":"Gypsum Wallboard","type":"cond","material":"gypsum","length":0.013}
R_6={"name":"inside surface","type":"conv","material":"insideSurface"}

#value of total resistence with wood
ResistenceList_withWood=[R_1,R_2,R_3,R_4b,R_5,R_6]

WoodResults={"Rtot_wood":0} 
Rtot_wood=0
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
        
WoodResults["Rtot_wood"]=Rtot_wood

print("The total resistence with wood is "+ str(Rtot_wood)+ " degC/W")


#value of total resistence with insulation
ResistenceList_withInsulation=[R_1,R_2,R_3,R_4a,R_5,R_6]

InsulationResults={"Rtot_insulation":0}
Rtot_ins=0
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
        
InsulationResults["Rtot_ins"]=Rtot_ins

print("The total resistence with insulation is "+ str(Rtot_ins)+ " degC/W")

A=50*0.8*2.5
DeltaT=24

U_wood=1/Rtot_wood
U_ins= 1/Rtot_ins

print("The heat  transfer  coefficient with wood is "+ str(U_wood)+ "W/degC" )
print("The heat  transfer  coefficient with insulation is "+ str(U_ins)+ "W/degC" )


U_tot=U_wood*0.25+U_ins*0.75

print("The overall  heat  transfer  coefficient  is "+ str(U_tot)+ "W/degC" )

R_tot=1/U_tot

print("The overall  unit  thermal  resistance is "+ str(R_tot)+ "degC/W" )

Q=U_tot*A*DeltaT

print("The rate  of  heat  loss  through  the  walls is "+str(Q)+ "W")

                                                       
        
        
        