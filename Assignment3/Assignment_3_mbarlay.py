#Assignment 3
#Assisgnment 3 was built according to assignment 2. Also, air gap and epsilons were added.


R_1 = {"name":"outside surface","type":"conv","material":"outsideSurfaceWinter"}
R_2 = {"name":"wood bevel lapped Siding","type":"cond","material":"woodLappedSiding", "length":0.013}
R_3 = {"name":"wood fider board","type":"cond","material":"woodFiberBoard","length":0.013}
R_4 = {"name":"glass fiber insulation","type":"cond","material":"glassFiberInsulation", "length":0.09}  
R_5 = {"name":"wood stud","type":"cond","material":"woodStud_90mm", "length":0.09}
R_6 = {"name":"Gypsum Wallboard","type":"cond","material":"gypsum", "length":0.013}
R_7 = {"name":"inside surface","type":"conv","material":"insideSurface"}
R_gap ={"name":"air-gap","type":"gap","epsilon_1":0.05,"epsilon_2":0.9,"length":0.020}

ResistanceList_withWood = [R_1,R_2,R_3,R_5,R_6,R_7,R_gap]
ResistanceList_withInsulation = [R_1,R_2,R_3,R_4,R_6,R_7,R_gap]

def epsilonEffective(epsilon_1=0.05,epsilon_2=0.9):
    result = 1/(1/epsilon_1+1/epsilon_2-1)
    return result

ResultsDictionary={}
def resistanceOfLayersInSeries(listOfResistance):
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
    AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23},
               0.040:{0.03:0.063,0.05:0.59,0.5:0.25},0.06:{0.03:0.51,0.05:0.49,0.5:0.23}}
    Rtot=0 
    for anyResistance in listOfResistance:
        if anyResistance["type"]=="cond":
            material_anyResistance = anyResistance["material"]
            length_anyResistance = anyResistance["length"]
            lengthInTheLibrary = ThermalResDict[material_anyResistance]["length"]
            RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]*length_anyResistance/lengthInTheLibrary
            anyResistance["RValue"] = RValue_anyResistance
            ResultsDictionary[anyResistance["name"]] = anyResistance["RValue"]
        elif anyResistance["type"]=="conv":
            material_anyResistance = anyResistance["material"]
            RValue_anyResistance = ThermalResDict[material_anyResistance]["R"]
            anyResistance["RValue"]=RValue_anyResistance   
            ResultsDictionary[anyResistance["name"]]= anyResistance["RValue"]
        elif anyResistance["type"]=="gap":
            effectiveEpsilon = round (epsilonEffective(anyResistance["epsilon_1"],anyResistance["epsilon_2"]),2)
            RValue_anyResistance = AirGapResDict[anyResistance["length"]][effectiveEpsilon]
            anyResistance["RValue"] = RValue_anyResistance 
            ResultsDictionary[anyResistance["name"]] = anyResistance["RValue"]
        else:
            print("please check your values!")
        Rtot = Rtot + RValue_anyResistance
        ResultsDictionary["Rtot"] = Rtot
    return ResultsDictionary

resistanceOfLayersInSeries(ResistanceList_withWood)
Rtot_wood = ResultsDictionary["Rtot"]

ResultsDictionary = {}
resistanceOfLayersInSeries(ResistanceList_withInsulation)
Rtot_insulation = ResultsDictionary["Rtot"]

A_tot = 100
A_wood = 25
A_ins = 75
delta_T = 24
U_wood = 1/float(Rtot_wood)
U_ins = 1/float(Rtot_insulation)
U_tot = (U_wood*(float(A_wood)/A_tot))+(U_ins*(float(A_ins)/A_tot))
R_total = 1/float(U_tot)
Q_tot = U_tot*A_tot*delta_T

print("R overall is: "+str(R_total)+"m2.degC/W")
print("U overall is: "+str(U_tot)+"W/(m^2C)")
print("Q total is "+str(Q_tot)+"W")