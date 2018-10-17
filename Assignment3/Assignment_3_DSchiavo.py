def resistanceoflayer(ResistanceList):
    
                       
    def epsilonEffective(epsilon1, epsilon2):
        result=1/(1/epsilon1+1/epsilon2-1)
        return result

   
    
    Result=[]
    for j in ResistanceList:
        R_tot=0
        result={}
        for i in j:
            if i["type"]=="Cond":
                material=i["Material"]
                length=i["Length"]
                lengthT=ThermalConRes[material]["length"]
                R=ThermalConRes[material]["R"]*length/lengthT
                result[i["Name"]]=R
                R_tot=R_tot+R
            elif i["type"]=="Conv":
                material=i["Material"]
                R=ThermalConRes[material]["R"]
                result[i["Name"]]=R
                R_tot=R_tot+R
            elif i["type"]=="gap":
                epsilon=epsilonEffective(i["epsilon1"],i["epsilon2"])
                R=AirGapResDict[i["length"]][epsilon]
                result[i["Name"]]=R
                R_tot=R_tot+R           
            result["R_tot"]=R_tot    
        Result.append(result)


    return Result

ThermalConRes={"FaceBrick":{"R":0.75, "length":0.1},
"Wood bevel lapped siding":{"R":0.14, "length":0.013},
"Wood studs":{"R":0.63 ,"length":0.090},
"fiberboard":{"R":0.23 ,"length":0.013},
"Glass Fiber Insulation":{"R":0.70 ,"length":0.025},
"Gypsum":{"R":0.079 ,"length":0.013},
"InsideSurface":{"R":0.12},
"OutsideSurfaceWinter":{"R":0.03},
"OutsideSurfaceSummer":{"R":0.44},
}

AirGapResDict={0.02:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
            0.04:{0.03:0.63,0.05:0.59,0.5:0.25}}    

R_1={"Name":"Gypsum","type":"Cond","Material":"Gypsum","Length":0.013}
R_2={"Name":"Wood bevel lapped siding","type":"Cond","Material":"Wood bevel lapped siding","Length":0.013}
R_3={"Name":"Glass Fiber Insulation","type":"Cond","Material":"Glass Fiber Insulation","Length":0.090}
R_4={"Name":"Wood studs","type":"Cond","Material":"Wood studs","Length":0.090}
R_5={"Name":"fiberboard","type":"Cond","Material":"fiberboard","Length":0.013}
R_o={"Name":"OutsideSurfaceWinter","type":"Conv","Material":"OutsideSurfaceWinter"}
R_i={"Name":"inside surface","type":"Conv","Material":"InsideSurface"}
R_gap={"Name":"Gap","type":"gap","epsilon1":0.05, "epsilon2":0.9, "length":0.020}
ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i,R_gap]
ResistanceList_insulation=[R_1,R_2,R_3,R_5,R_o,R_i,R_gap]
ResistanceList=[ResistanceList_wood,ResistanceList_insulation]
    
R=resistanceoflayer(ResistanceList) 

A=50*0.8*2.5
DT=24

R_wood=R[0]["R_tot"]
R_insulation=R[1]["R_tot"]
U_wood=1/R_wood
U_insulation=1/R_insulation
print("The heat transfer coefficient, considering the wood studs is ")
print(str(U_wood)+ "  W/m^2")   
print("The heat transfer coefficient, considering the glass fiber insulation is ")
print(str(U_insulation)+ "  W/m^2")  
U_tot=U_wood*0.25+U_insulation*0.75
print("The OVERALL heat transfer coefficient, is")
print(str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
print("The OVERALL resistance is ")
print(str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DT
print("The OVERALL heat tranfer is ")
print(str(Q_tot)+ "  W")