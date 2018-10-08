# Determine the overall unit thermal resistance (the R-value) 
#and the overall heat transfer coefficient (the U-factor) 


ThermalResistance= { 
"woodStud_90mm":{"R":0.63, "length":0.09},
"woodFiberBoard":{"R":0.23, "length":0.013},
"woodLappedSiding":{"R":0.14, "length":0.013},
"insideSurface":{"R":0.12, "length":0},
"outsideSurfaceWinter":{ "R":0.03, "length":0},
"gypsum":{"R":0.079, "length":0.013},
"glass fiber insulation" : {"R":0.7, "length":0.025}

}

R_1={"name": "Gypsum Wallboard", "use":"both", "material": "gypsum", "length":0.013}
R_2={"name": "Outside Air", "use":"both", "material": "outsideSurfaceWinter", "length":0}
R_3={"name": "Wood Studs", "use":"wood", "material": "woodStud_90mm", "length":0.09}

R_4={"name": "wood fiberboard", "use":"both", "material": "woodFiberBoard", "length":0.013}
R_5={"name": "wood bevel lapped siding", "use":"both", "material": "woodLappedSiding", "length":0.013}
R_6={"name": "Inside air", "use":"both", "material": "insideSurface", "length":0}
R_7={"name": "Glass fiber insulation", "use":"insulation", "material": "glass fiber insulation", "length":0.09} 

ResistancesList= [R_1, R_2, R_3, R_4, R_5, R_6, R_7]

Rinsulation=0
Rwood=0 


for anyresistance in ResistancesList:
        if  anyresistance["use"] == "insulation" or anyresistance["use"] == "both":
            material_anyresistance= anyresistance["material"]
            length_anyresistance= anyresistance ["length"]
            lengthofdictionary= ThermalResistance[material_anyresistance]["length"]
            RValue_dictionary=ThermalResistance[material_anyresistance]["R"]
            if lengthofdictionary == length_anyresistance:
                Resistanceofthematerial=RValue_dictionary
                Rinsulation= Rinsulation+Resistanceofthematerial
            if lengthofdictionary != length_anyresistance:
                Resistanceofthematerial= (RValue_dictionary * length_anyresistance)/lengthofdictionary
                Rinsulation= Rinsulation+Resistanceofthematerial
                
        if  anyresistance["use"] == "wood" or anyresistance["use"] == "both":
            material_anyresistance= anyresistance["material"]
            length_anyresistance= anyresistance ["length"]
            lengthofdictionary= ThermalResistance[material_anyresistance]["length"]
            RValue_dictionary=ThermalResistance[material_anyresistance]["R"]
            if lengthofdictionary == length_anyresistance:
                Resistanceofthematerial=RValue_dictionary
                Rwood= Rwood+Resistanceofthematerial
            if lengthofdictionary != length_anyresistance:
                Resistanceofthematerial= (RValue_dictionary * length_anyresistance)/lengthofdictionary
                Rwood= Rwood+Resistanceofthematerial
                
print("The R' for the wood is " + str(Rwood))
print("The R' for insulation is " + str(Rinsulation))            
            

U_insulation= 1/(Rinsulation)
U_wood= 1/(Rwood)
A_insulation=0.75
A_wood=0.25

U_total= U_insulation*A_insulation + (U_wood*A_wood)#This is the second answer
R_total= 1/U_total  #This is the first answer
print("The Total resistance for the problem is " + str(R_total))
print("The Total U for the problem is " + str(U_total))
#Now we have the area that is not covered by glazin

A_noglazing= 0.8*2.5*50

#We have the temperature difference

delta_t= 24

#Now we can determine the rate of heat loss through the walls

Q_total= U_total*A_noglazing*delta_t

print("the rate of heat loss through the walls " + str(Q_total))




            
            
                     
              