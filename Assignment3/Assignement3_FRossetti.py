# -*- coding: utf-8 -*-
A=50*0.8*2.5
DeltaT=24

ThermalConRes={"FaceBrick":{"R":0.75, "length":0.1},
"Wood bevel lapped siding":{"R":0.14, "length":0.013},
"Wood studs":{"R":0.63 ,"length":0.090},
"fiberboard":{"R":0.23 ,"length":0.013},
"Glass Fiber Ins":{"R":0.70 ,"length":0.025},
"Gypsum":{"R":0.079 ,"length":0.013},
"InsideSurface":{"R":0.12},
"OutsideSurfaceWinter":{"R":0.03},
"OutsideSurfaceSummer":{"R":0.44},
}

AirGapResDict={0.020:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
                   0.040:{0.03:0.063,0.05:0.59,0.5:0.25}}

R_1={"Name":"Gypsum","type":"Cond","Material":"Gypsum","Length":0.013}
R_2={"Name":"Wood bevel lapped siding","type":"Cond","Material":"Wood bevel lapped siding","Length":0.013}
R_3={"Name":"Glass Fiber Ins","type":"Cond","Material":"Glass Fiber Ins","Length":0.090}
R_4={"Name":"Wood studs","type":"Cond","Material":"Wood studs","Length":0.090}
R_5={"Name":"fiberboard","type":"Cond","Material":"fiberboard","Length":0.013}
R_o={"Name":"OutsideSurfaceWinter","type":"Conv","Material":"OutsideSurfaceWinter"}
R_i={"Name":"inside surface","type":"Conv","Material":"InsideSurface"}
R_gap ={"name":"air-Gap","type":"Gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

def epsilonEffective(epsilon1=0.05, epsilon2=0.9):
    result=1/(1/epsilon1+1/epsilon2-1)  
    return result
    
ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i,R_gap] # considering wood
ResistanceList_ins=[R_1,R_2,R_3,R_5,R_o,R_i,R_gap] # considering insulation

def TotalWoodResistances (ResistanceList_wood):
    R_tot_wood=0
    Result_wood={}

    for i in ResistanceList_wood:
        if i["type"]=="Cond":
            material=i["Material"]
            length=i["Length"]
            lengthT=ThermalConRes[material]["length"] #use concatenated libraries # the material is that found at line 42
            # take the element lenght related to the n material of the library ThermalConRes
            R=ThermalConRes[material]["R"]*length/lengthT 
            Result_wood[i["Name"]]=R # I'm adding to the empty library Result_wood l'i[Name] and I put it equal to R
            R_tot_wood=R_tot_wood+R
        elif i["type"]=="Conv":
            material=i["Material"]
            R=ThermalConRes[material]["R"]
            R_tot_wood=R_tot_wood+R
            Result_wood[i["Name"]]=R
            R_tot_wood=R_tot_wood+R
        elif i["type"]=="Gap":
            effectiveEpsilon=epsilonEffective(i["epsilon1"],i["epsilon2"])
            RValue_i = AirGapResDict[i["length"]][effectiveEpsilon]
            i["RValue"]=RValue_i 
            Result_wood[i["name"]]= i["RValue"]
            R_tot_wood=R_tot_wood+RValue_i
    Result_wood["R_tot_wood"]=R_tot_wood
    return Result_wood

    
print("The total Resistance considering the wood studs is ")
print(str(TotalWoodResistances (ResistanceList_wood)))

def TotalInsResistances (ResistanceList_ins):
    R_tot_ins=0
    Result_ins={}

    for i in ResistanceList_ins:
        if i["type"]=="Cond":
            material=i["Material"]
            length=i["Length"]
            lengthT=ThermalConRes[material]["length"]
            R=ThermalConRes[material]["R"]*length/lengthT
            Result_ins[i["Name"]]=R
            R_tot_ins=R_tot_ins+R
        elif i["type"]=="Conv":
            material=i["Material"]
            R=ThermalConRes[material]["R"]
            R_tot_ins=R_tot_ins+R
            Result_ins[i["Name"]]=R
        elif i["type"]=="Gap":
            effectiveEpsilon=epsilonEffective(i["epsilon1"],i["epsilon2"])
            RValue_i = AirGapResDict[i["length"]][effectiveEpsilon]
            print(RValue_i)
            i["RValue"]=RValue_i 
            Result_ins[i["name"]]= i["RValue"]
            R_tot_ins=R_tot_ins+RValue_i
    Result_ins["R_tot_ins"]=R_tot_ins
    return Result_ins
    
print("The total Resistance considering ins is "+str(TotalInsResistances (ResistanceList_ins)))


U_wood=1/TotalWoodResistances (ResistanceList_wood)["R_tot_wood"]
U_ins=1/TotalInsResistances (ResistanceList_ins)["R_tot_ins"]  
print("The heat transfer coefficient, considering the wood is " + str(U_wood)+ "  W/m^2")  
print("The heat transfer coefficient, considering the insulation is "+str(U_ins)+ "  W/m^2")
U_tot=U_wood*0.25+U_ins*0.75
print("The overall heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
print("The overall resistance is "+str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DeltaT
print("The overall heat tranfer is "+str(Q_tot)+ "  W")
