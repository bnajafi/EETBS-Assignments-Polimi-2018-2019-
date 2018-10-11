#Assignment-2

ThermalResDict = {"FaceBrick":{"R":0.075, "length":0.1}
, "woodStud_90mm":{"R":0.63, "length":0.09}
, "woodFiberBoard":{"R":0.23, "length":0.013}
, "woodLappedSiding":{"R":0.14, "length":0.013}
, "gypsum":{"R":0.079, "length":0.013}
, "glassFiberInsulation":{"R":0.7,"length":0.025}
, "insideSurface":{"R":0.12}
, "outsideSurfaceWinter":{"R":0.03}
, "outsideSurfaceSummer":{"R":0.044}
}

R_1 = {"name":"outside surface","type":"conv","material":"outsideSurfaceWinter"}
R_2 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}
R_3 = {"name":"wood fider board","type":"cond","material":"woodFiberBoard","length":0.013}
R_4 = {"name":"glass fiber insulation","type":"cond","material":"glassFiberInsulation", "length":0.09}  
R_5 = {"name":"wood stud","type":"cond","material":"woodStud_90mm", "length":0.09}
R_6 = {"name":"Gypsum Wallboard","type":"cond","material":"gypsum", "length":0.013}
R_7 = {"name":"inside surface","type":"conv","material":"insideSurface"}


ResistanceList_withWood = [R_1,R_2,R_3,R_5,R_6,R_7]
Rtot_withWood=0

for anyResistance in ResistanceList_withWood:
    if anyResistance["type"]=="cond":
        material_anyResistance = anyResistance["material"]
        length_anyResistance = anyResistance["length"]
        lengthOfThisMaterialInTheLibrary = ThermalResDict[material_anyResistance]["length"]
        RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
        Rtot_withWood=Rtot_withWood+RValue_anyResistance
    elif anyResistance["type"]=="conv":
        material_anyResistance=anyResistance["material"]
        RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]
        Rtot_withWood=Rtot_withWood+RValue_anyResistance
    else:
        print("Please check your data")

print("R total with wood is "+ str(Rtot_withWood)+" m2.degC/W")

resistanceList_withInsulation=[R_1,R_2,R_3,R_4,R_6,R_7]
Rtot_withInsulation=0

for anyResistance in resistanceList_withInsulation:
    if anyResistance["type"]=="cond":
        material_anyResistance = anyResistance["material"]
        length_anyResistance = anyResistance["length"]
        lengthOfThisMaterialInTheLibrary = ThermalResDict[material_anyResistance]["length"]
        RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthOfThisMaterialInTheLibrary
        Rtot_withInsulation=Rtot_withInsulation+RValue_anyResistance
    elif anyResistance["type"]=="conv":
        material_anyResistance=anyResistance["material"]
        RValue_anyResistance=ThermalResDict[material_anyResistance]["R"]
        Rtot_withInsulation=Rtot_withInsulation+RValue_anyResistance
    else:
        print("Please check your data")
        
print("R total with insulation is "+ str(Rtot_withWood)+" m2.degC/W")

Atot=100
Awood=25
Ains=75
deltaT=24
Uwood=1/float(Rtot_withWood)
Uins=1/float(Rtot_withInsulation)
Utot=(Uwood*(float(Awood)/Atot))+(Uins*(float(Ains)/Atot))
Rtot=1/float(Utot)
Qtot=Utot*Atot*deltaT
print("R total is "+str(Rtot)+"m2.degC/W")
print("U overall is "+str(Utot)+"W/m2.degC")
print("Q total is "+str(Qtot)+"W")
        
        
        