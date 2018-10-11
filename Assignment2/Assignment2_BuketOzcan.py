#example A

ThermalResDict={"FaceBrick":{"R":0.075, "length":0.1}, 
"Gypsum":{"R":0.079, "length":0.013}, 
"woodStud_90mm":{"R":0.63, "length":0.09}, 
"woodFiberBoard":{"R":0.23, "length":0.013},
"woodLappedSiding":{"R":0.14, "length":0.013},
"glassFiberInsulation":{"R":0.7, "length":0.025},
"insideSurface":{"R":0.12},
"outsideSurfaceWinter":{"R":0.03},
"outsideSurfaceSummer":{"R":0.044}} 

R_1= {"name":"Outside surface", "type":"conv", "material":"outsideSurfaceWinter"}
R_2= {"name":"Wood bevel lapped siding", "type":"cond", "material":"woodLappedSiding","length":0.013}
R_3= {"name":"Wood FiberBoard", "type":"cond", "material":"woodFiberBoard","length":0.013}
R_4= {"name":"Glass Fiber Insulation", "type":"cond", "material":"glassFiberInsulation","length":0.09}
R_5= {"name":"Wood stud", "type":"cond", "material":"woodStud_90mm","length":0.09}
R_6= {"name":"Gypsum WallBoard", "type":"cond", "material":"Gypsum","length":0.013}
R_7= {"name":"Inside surface", "type":"conv", "material":"insideSurface"}

ResistanceList_withWood=[R_1,R_2,R_3,R_5,R_6,R_7]

Rtot_withWood=0
for anyResistance in ResistanceList_withWood:
    if anyResistance["type"]=="cond":
        material_anyResistance= anyResistance["material"]
        length_anyResistance= anyResistance["length"]
        lengthOfThisMaterialInTheLibrary= ThermalResDict[material_anyResistance]["length"]
        RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
        Rtot_withWood=Rtot_withWood+RValue_anyResistance
    elif anyResistance["type"]=="conv":
        material_anyResistance= anyResistance["material"]
        RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]
        Rtot_withWood=Rtot_withWood+RValue_anyResistance

print("R total with wood is "+ str(Rtot_withWood)+" m2.degC/W")
        
ResistanceList_withInsulation=[R_1,R_2,R_3,R_4,R_6,R_7]
Rtot_withInsulation=0
for anyResistance in ResistanceList_withInsulation:
    if anyResistance["type"]=="cond":
        material_anyResistance= anyResistance["material"]
        length_anyResistance= anyResistance["length"]
        lengthOfThisMaterialInTheLibrary= ThermalResDict[material_anyResistance]["length"]
        RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
        Rtot_withInsulation=Rtot_withInsulation+RValue_anyResistance
    elif anyResistance["type"]=="conv":
        material_anyResistance= anyResistance["material"]
        RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]
        Rtot_withInsulation=Rtot_withInsulation+RValue_anyResistance
        
print("R total with insulation is "+ str(Rtot_withInsulation)+" m2.degC/W")
        
Atot=100
Awood=25
Ains=75
DeltaT=24
Uwood=1/float(Rtot_withWood)
Uins=1/float(Rtot_withInsulation)
Utot=(Uwood*(float(Awood)/Atot))+(Uins*(float(Ains)/Atot))
Rtot=1/float(Utot)
Qtot=Utot*Atot*DeltaT
print("R total is "+str(Rtot)+" m2.degC/W")
print("U overall is "+str(Utot)+" W/m2.degC")
print("Q total is "+str(Qtot)+" W")