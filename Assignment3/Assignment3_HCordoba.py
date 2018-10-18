#Doing the assignment  #3
#We are going to use list, dictionary and functions for the previous assignment

# Determine the overall unit thermal resistance (the R-value) 
#and the overall heat transfer coefficient (the U-factor) 


ThermalResDict= { 
"woodStud_90mm":{"R":0.63, "length":0.09},
"woodFiberBoard":{"R":0.23, "length":0.013},
"woodLappedSiding":{"R":0.14, "length":0.013},
"insideSurface":{"R":0.12},
"outsideSurfaceWinter":{ "R":0.03},
"gypsum":{"R":0.079, "length":0.013},
"glass fiber insulation" : {"R":0.7, "length":0.025}

}



AirGapResDict={0.020:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},0.040:{
                0.040:{0.03:0.063,0.05:0.59,0.5:0.25}}}




R_1={"name": "Gypsum Wallboard", "type":"cond", "material": "gypsum", "length":0.013}
R_2={"name": "Outside Air", "type":"conv", "material": "outsideSurfaceWinter"}
R_3={"name": "Wood Studs", "type":"cond", "material": "woodStud_90mm", "length":0.09}

R_4={"name": "wood fiberboard", "type":"cond", "material": "woodFiberBoard", "length":0.013}
R_5={"name": "wood bevel lapped siding", "type":"cond", "material": "woodLappedSiding", "length":0.013}
R_6={"name": "Inside air", "type":"conv", "material": "insideSurface"}
R_7={"name": "Glass fiber insulation", "type":"cond", "material": "glass fiber insulation", "length":0.09} 
R_gap={"name":"air.gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}



def epsilonEffective(epsilon1,epsilon2): 
    result=1/(1/epsilon1+1/epsilon2-1)              
    return result
epsilonEffective(R_gap["epsilon1"],R_gap["epsilon2"])

resistancesListWithWood=[R_1,R_2,R_3,R_5,R_6,R_4, R_gap]
resistancesListWithInsulation=[R_1,R_2,R_7,R_5,R_6,R_4, R_gap]

def ResistanceOfLayerInSeries(ListofResistances):
    resultDictionary={}
    nameDictionary={}
    Rtot=0
    for anyresistance in ListofResistances:
        if anyresistance["type"]=="cond":
            material_anyresistance=anyresistance["material"]
            length_anyresistance=anyresistance["length"]
            name_anyresistance=anyresistance["name"]
            lengthofThisMaterialInTheLibrary=ThermalResDict[material_anyresistance]["length"]
            RValue_anyresistance=ThermalResDict[material_anyresistance]["R"]*(length_anyresistance/lengthofThisMaterialInTheLibrary)
            anyresistance["RValue"]=RValue_anyresistance
            resultDictionary[anyresistance["name"]]=RValue_anyresistance
            Rtot=Rtot+RValue_anyresistance
        elif anyresistance["type"]=="conv":
            material_anyresistance=anyresistance["material"]
            name_anyresistance=anyresistance["name"]
            RValue_anyresistance=ThermalResDict[material_anyresistance]["R"]
            anyresistance["RValue"]=RValue_anyresistance
            resultDictionary[anyresistance["name"]]=RValue_anyresistance
            Rtot=Rtot+RValue_anyresistance
        elif anyresistance["type"]=="gap":
            effectiveEpsilon=epsilonEffective(anyresistance["epsilon1"],anyresistance["epsilon2"])
            RValue_anyresistance=AirGapResDict[anyresistance["length"]][effectiveEpsilon]
            resultDictionary[anyresistance["name"]]=RValue_anyresistance
            Rtot=Rtot+RValue_anyresistance          
    resultDictionary["Rtot"]=Rtot
    return resultDictionary
    
    
    
D_Wood=ResistanceOfLayerInSeries(resistancesListWithWood)
Rwood=D_Wood['Rtot']
print(D_Wood)
print("Rwood: " + str(Rwood))

D_Insulation=ResistanceOfLayerInSeries(resistancesListWithInsulation)
Rinsulation=D_Insulation['Rtot']
print(D_Insulation)
print("Rinsulation: " + str(Rinsulation))


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




            
            
                     
              
