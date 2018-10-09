#assignment 2
#funaro_eleonora

Awood=0.25
Ainsulation=0.75
Atot=100 
dT=24

MaterialsDictionary={"outside_air":{"R":0.03, "length":0}, "wood_siding":{"R":0.14, "length":0.013},
"wood_fiber":{"R":0.23, "length":0.013},"glass_fiber":{"R":0.7, "length":0.025}, "wood_studs":{"R":0.63, "length":0.09}, 
"gypsum": {"R":0.079, "length":0.013}, "inside_air":{"R":0.12,"length":0}}

R1={"material":"outside_air", "type":"general", "length":0}
R2={"material":"wood_siding", "type":"general", "length":0.013}
R3={"material":"wood_fiber", "type":"general", "length":0.013}
R4={"material":"glass_fiber", "type":"insulation", "length":0.09}
R5={"material":"wood_studs", "type":"wood", "length":0.09}
R6={"material":"gypsum", "type":"general", "length":0.013}
R7={"material":"inside_air", "type":"general", "length":0}

ResistanceList=[R1,R2,R3,R4,R5,R6,R7]

Rinsulation=0
Rwood=0

for anyresistance in ResistanceList:
    if anyresistance["type"]=="insulation" or anyresistance["type"]=="general":
        material_resistance=anyresistance["material"]
        length_resistance=anyresistance["length"]
        resistance_dictionary=MaterialsDictionary[material_resistance]["R"]
        length_dictionary=MaterialsDictionary[material_resistance]["length"]
        if length_dictionary != length_resistance:
            Rvalue=(resistance_dictionary*length_resistance)/length_dictionary
            Rinsulation=Rinsulation+Rvalue
        if length_dictionary == length_resistance:
            Rvalue=resistance_dictionary
            Rinsulation=Rinsulation+Rvalue
    if anyresistance["type"]=="wood" or anyresistance["type"]=="general":
        material_resistance=anyresistance["material"]
        length_resistance=anyresistance["length"]
        resistance_dictionary=MaterialsDictionary[material_resistance]["R"]
        length_dictionary=MaterialsDictionary[material_resistance]["length"]
        if length_dictionary != length_resistance:
            Rvalue=(resistance_dictionary*length_resistance)/length_dictionary
            Rwood=Rwood+Rvalue
        if length_dictionary == length_resistance:
            Rvalue=resistance_dictionary
            Rwood=Rwood+Rvalue
    
print("Rwood: " +str(Rwood))  
print("Rinsulation: " +str(Rinsulation))

Uinsulation=1/Rinsulation
Uwood=1/Rwood
Utot=(Uinsulation*Ainsulation)+(Uwood*Awood)
Rtot=1/Utot

print("Rtot: " +str(Rtot))

Q=(Atot*dT)/Rtot
        
print("Q: " +str(Q))       

        
