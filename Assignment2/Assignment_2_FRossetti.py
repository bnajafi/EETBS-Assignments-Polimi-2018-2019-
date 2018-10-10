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

R_1={"Name":"Gypsum","type":"Cond","Material":"Gypsum","Length":0.013}
R_2={"Name":"Wood bevel lapped siding","type":"Cond","Material":"Wood bevel lapped siding","Length":0.013}
R_3={"Name":"Glass Fiber Ins","type":"Cond","Material":"Glass Fiber Ins","Length":0.090}
R_4={"Name":"Wood studs","type":"Cond","Material":"Wood studs","Length":0.090}
R_5={"Name":"fiberboard","type":"Cond","Material":"fiberboard","Length":0.013}
R_o={"Name":"OutsideSurfaceWinter","type":"Conv","Material":"OutsideSurfaceWinter"}
R_i={"Name":"inside surface","type":"Conv","Material":"InsideSurface"}


ResistanceList_wood=[R_1,R_2,R_4,R_5,R_o,R_i] # considering wood
ResistanceList_ins=[R_1,R_2,R_3,R_5,R_o,R_i] # considering insulation

R_tot_wood=0
Result_wood={}

for i in ResistanceList_wood:
    if i["type"]=="Cond":
        material=i["Material"]
        length=i["Length"]
        lengthT=ThermalConRes[material]["length"] #use concatenated libraries # il material è quello trovato alla linea 32
        # prendo l'elemento lenght relativo al materiale ennesimo della libreria ThermalConRes
        R=ThermalConRes[material]["R"]*length/lengthT 
        Result_wood[i["Name"]]=R # aggiungo alla libreria vuota Result_wood l'i[Name] e lo pongo uguale a R
        R_tot_wood=R_tot_wood+R
    elif i["type"]=="Conv":
        material=i["Material"]
        R=ThermalConRes[material]["R"]
        R_tot_wood=R_tot_wood+R
        Result_wood[i["Name"]]=R
Result_wood["R_tot_wood"]=R_tot_wood

print("The total Resistance considering the wood studs is ")
print(str(Result_wood["R_tot_wood"]))

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
Result_ins["R_tot_ins"]=R_tot_ins

print("The total Resistance considering ins is ")
print(str(Result_ins["R_tot_ins"]))


U_wood=1/Result_wood["R_tot_wood"]
U_ins=1/Result_ins["R_tot_ins"]   
print("The heat transfer coefficient, considering the wood is " + str(U_wood)+ "  W/m^2")  
print("The heat transfer coefficient, considering the insulation is "+str(U_ins)+ "  W/m^2")
U_tot=U_wood*0.25+U_ins*0.75
print("The overall heat transfer coefficient, is"+str(U_tot)+ "  W/m^2")
R_Tot=1/U_tot
print("The overall resistance is "+str(R_Tot)+ " m^2/W")
Q_tot=U_tot*A*DeltaT
print("The overall heat tranfer is "+str(Q_tot)+ "  W")

