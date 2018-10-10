# -*- coding: utf-8 -*-

#Assignement2: 

#Thermal resistance dictionay: tabulated values of the resistances of different materials with defined lengths :
thermalResDic= {"gypsum":{"R":0.079, "length":0.013}, "Plywood":{"R":0.11, "length":0.013},
"insideSurface":{"R":0.12}, "outsideSurfaceWinter":{"R":0.03}, "outsideSurfaceSummer":{"R":0.044},"woodLappedSiding":{"R":0.14, "length":0.013},
"woodFiberBoard":{"R":0.23, "length":0.013}, "woodStud":{"R":0.63, "length":0.09},"glassfiber":{"R":0.7, "length":0.025}}

#Definition of all resistances :
Rgyp={"name":"Gypsum Wallboard", "material":"gypsum", "length":0.013, "type":"cond"}
Rwood={"name":"wood bevel lapped siding", "material":"woodLappedSiding", "length":0.013, "type":"cond"}
Rin={"name":"inside surface", "material":"insideSurface", "type":"conv"}
Rfib={"name":"fiberboard", "material":"woodFiberBoard", "length":0.013, "type":"cond"}
Rins={"name":"insulation", "material":"glassfiber", "length":0.09, "type":"cond"}
Rstud={"name":"wood stud", "material":"woodStud", "length":0.09, "type":"cond"}
RoutS={"name":"Summer Out", "material":"outsideSurfaceSummer", "type":"conv"}
RoutW={"name":"Winter Out", "material":"outsideSurfaceWinter", "type":"conv"}

#Calculation of the resistances in series:
ResistanceList_withWood=[Rin, Rgyp, Rwood,Rfib, Rstud,RoutW]

RtotWood=0;
RtotIns=0;
for i in ResistanceList_withWood:
    if i["type"]=="cond":
        material=i["material"]
        material_length=i["length"]
        length_inLibrary=thermalResDic[material]["length"]
        Rvalue_i=thermalResDic[material]["R"]*material_length/length_inLibrary
        i ["Rvalue"]=Rvalue_i
        RtotWood=RtotWood+Rvalue_i
    elif i["type"]=="conv":
        material = i["material"]
        Rvalue_i=thermalResDic[material]["R"]
        RtotWood=RtotWood+Rvalue_i

        
ResistanceList_withIns=[Rin, Rgyp, Rwood, Rfib, Rins, RoutW]

for i in ResistanceList_withIns:
    if i["type"]=="cond":
        material=i["material"]
        material_length=i["length"]
        length_inLibrary=thermalResDic[material]["length"]
        Rvalue_i=thermalResDic[material]["R"]*material_length/length_inLibrary
        i ["Rvalue"]=Rvalue_i
        RtotIns=RtotIns+Rvalue_i
    elif i["type"]=="conv":
        material = i["material"]
        Rvalue_i=thermalResDic[material]["R"]
        RtotIns=RtotIns+Rvalue_i
    else :
        print("resistance type not valid")
        
#Calculation of the overall Resistance and heat transfer coefficient:
#Assuming Area = 1:
Atot=1
Ains=0.75*Atot
Awood=0.25*Atot

Uwood=1/RtotWood #W/(K*m^2)
Uins=1/RtotIns   #W/(K*m^2)

Utot=Uwood*(Awood/Atot) + Uins*(Ains/Atot) #W/(K*m^2)

Rtot=1/Utot # m^2 * K/W

print("The overall unit thermal resistance value is: " +str(Rtot)+ " m^2 * K/W")
print("The overall heat transfer coefficient is: " +str(Utot)+ " W/K*m^2")

#Heat loss through the walls of an house in Nevada:
A= 50*2.5 #m^2
Tout=-2 #°C
Tin =22 #°C
Awall=0.8*A 


Q=Utot*Awall*(Tin-Tout)
QkW=Q*10**(-3)
print("Rate of heat loss rate of the house is: " + str(Q) + "W, or " + str(QkW)+ "kW")


