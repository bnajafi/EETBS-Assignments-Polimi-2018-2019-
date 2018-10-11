#Example 1 Unit 1.2

#Overall unit thermal resistance (Rtotal) and overall heat transfer coefficient (Utotal)
ThermalResDict={"GlassFiberInsulation":{"R":2.52,"length":0.09},
                "WoodStud_90mm":{"R":0.63,"length":0.09},
                "WoodFiberBoard":{"R":0.23,"length":0.013},
                "WoodLappedSiding":{"R":0.14,"length":0.013},
                "Gypsum":{"R":0.079,"length":0.013},
                "InsideSurface":{"R":0.12},
                "OutsideSurface":{"R":0.03},
                }

R_i={"name":"inside surface", "type":"conv", "material":"InsideSurface"}
R_2={"name":"Wood bevel lapped Siding", "type":"cond", "material":"WoodLappedSiding", "length":0.013}
R_3={"name":"Wood fiberboard", "type":"cond", "material":"WoodFiberBoard", "length":0.013}
R_4={"name":"Glass fiber insulation", "type":"cond", "material":"GlassFiberInsulation", "length":0.09}
R_5={"name":"Wood studs", "type":"cond", "material":"WoodStud_90mm", "length":0.09}          
R_6={"name":"Gypsum Wallboard","type":"cond", "material":"Gypsum", "length":0.013}
R_o={"name":"Outside surface", "type":"conv", "material":"OutsideSurface"}


ResistanceList_withWood=[R_i,R_2,R_3,R_5,R_6,R_o]
ResistanceList_withInsulation=[R_i,R_2,R_3,R_4,R_6,R_o]
Rtot_withWood=0
Rtot_withInsulation=0

for AnyResistance in ResistanceList_withWood:
    if AnyResistance["type"]=="cond":
        material_AnyResistance=AnyResistance["material"]
        length_AnyResistance=AnyResistance["length"]
        lengthOnLibrary=ThermalResDict[material_AnyResistance]["length"]
        RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]*length_AnyResistance/lengthOnLibrary
        AnyResistance["RValue"]=RValue_AnyResistance
        Rtot_withWood=Rtot_withWood+RValue_AnyResistance
    elif AnyResistance["type"]=="conv":
        material_AnyResistance=AnyResistance["material"]
        RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]
        AnyResistance["RValue"]=RValue_AnyResistance
        Rtot_withWood=Rtot_withWood+RValue_AnyResistance

for AnyResistance in ResistanceList_withInsulation:
    if AnyResistance["type"]=="cond":
        material_AnyResistance=AnyResistance["material"]
        length_AnyResistance=AnyResistance["length"]
        lengthOnLibrary=ThermalResDict[material_AnyResistance]["length"]
        RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]*length_AnyResistance/lengthOnLibrary
        AnyResistance["RValue"]=RValue_AnyResistance
        Rtot_withInsulation=Rtot_withInsulation+RValue_AnyResistance
    elif AnyResistance["type"]=="conv":
        material_AnyResistance=AnyResistance["material"]
        RValue_AnyResistance=ThermalResDict[material_AnyResistance]["R"]
        AnyResistance["RValue"]=RValue_AnyResistance
        Rtot_withInsulation=Rtot_withInsulation+RValue_AnyResistance

U_wood=1/Rtot_withWood
U_insulation=1/Rtot_withInsulation
Utotal=0.25*U_wood+0.75*U_insulation
print("The total heat transfer coefficient is Utotal= "+str(Utotal))
Rtotal=1/Utotal
print("The total thermal resistance is Rtotal= "+str(Rtotal))

#Rate of heat loss through the walls
Area=50*2.5*0.8
T_1=22
T_2=-2
Q=Utotal*Area*(T_1-T_2)
print("The rate of heat loss through the walls is Q= "+str(Q))