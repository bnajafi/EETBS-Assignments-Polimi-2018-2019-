A=50*0.8*2.5
DT=24

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

R_1={"Name":"Gypsum","type":"Cond","Material":"Gypsum","Length":0.013}
R_2={"Name":"Wood bevel lapped siding","type":"Cond","Material":"Wood bevel lapped siding","Length":0.013}
R_3={"Name":"Glass Fiber Insulation","type":"Cond","Material":"Glass Fiber Insulation","Length":0.090}
R_4={"Name":"Wood studs","type":"Cond","Material":"Wood studs","Length":0.090}
R_5={"Name":"fiberboard","type":"Cond","Material":"fiberboard","Length":0.013}
R_o={"Name":"OutsideSurfaceWinter","type":"Conv","Material":"OutsideSurfaceWinter"}
R_i={"Name":"inside surface","type":"Conv","Material":"InsideSurface"}


ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i]
ResistanceList_insulation=[R_1,R_2,R_3,R_5,R_o,R_i]

R_tot_wood=0
Result_wood={}

for i in ResistanceList_wood:
    if i["type"]=="Cond":
        material=i["Material"]
        length=i["Length"]
        lengthT=ThermalConRes[material]["length"]
        R=ThermalConRes[material]["R"]*length/lengthT
        Result_wood[i["Name"]]=R
        R_tot_wood=R_tot_wood+R
    elif i["type"]=="Conv":
        material=i["Material"]
        R=ThermalConRes[material]["R"]
        R_tot_wood=R_tot_wood+R
        Result_wood[i["Name"]]=R
Result_wood["R_tot_wood"]=R_tot_wood

print("The total Resistance considering the wood studs is ")
print(str(Result_wood["R_tot_wood"]))

R_tot_insulation=0
Result_insulation={}

for i in ResistanceList_insulation:
    if i["type"]=="Cond":
        material=i["Material"]
        length=i["Length"]
        lengthT=ThermalConRes[material]["length"]
        R=ThermalConRes[material]["R"]*length/lengthT
        Result_insulation[i["Name"]]=R
        R_tot_insulation=R_tot_insulation+R
    elif i["type"]=="Conv":
        material=i["Material"]
        R=ThermalConRes[material]["R"]
        R_tot_insulation=R_tot_insulation+R
        Result_insulation[i["Name"]]=R
Result_insulation["R_tot_insulation"]=R_tot_insulation

print("The total Resistance considering insulation is ")
print(Result_insulation[R_tot])


U_wood=1/Result_wood["R_tot_wood"]
U_insulation=1/Result_insulation["R_tot_insulation"]   
print("The heat transfer coefficient, considering the wood studs is "+str(U_wood)+ "  W/m^2")   
print("The heat transfer coefficient, considering the glass fiber insulation is "+str(U_insulation)+ "  W/m^2")  
U_tot=U_wood*0.25+U_insulation*0.75
print("The OVERALL heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
print("The OVERALL resistance is "+str(R_Tot)+ "  m^2/W")
Q_tot=U_tot*A*DT
print("The OVERALL heat tranfer is "+str(Q_tot)+ "  W")
