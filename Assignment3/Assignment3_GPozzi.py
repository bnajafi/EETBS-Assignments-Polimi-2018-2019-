#ASSIGNEMENT 3  Gilberto Pozzi:

thermalResDic= {"gypsum":{"R":0.079, "length":0.013}, "Plywood":{"R":0.11, "length":0.013},
"insideSurface":{"R":0.12}, "outsideSurfaceWinter":{"R":0.03}, "outsideSurfaceSummer":{"R":0.044},"woodLappedSiding":{"R":0.14, "length":0.013},
"woodFiberBoard":{"R":0.23, "length":0.013}, "woodStud":{"R":0.63, "length":0.09},"glassfiber":{"R":0.7, "length":0.025}}

AirGapResDict={0.02:{0.03:0.051, 0.8181818181818181:0.17, 0.5:0.23},
            0.04:{0.03:0.63, 0.05:0.59, 0.5:0.25}}    #Dictionary with tabulated values of R for different distances end epsilons in an air gap

Rgyp={"name":"Gypsum Wallboard", "material":"gypsum", "length":0.013, "type":"cond"}
Rwood={"name":"wood bevel lapped siding", "material":"woodLappedSiding", "length":0.013, "type":"cond"}
Rin={"name":"inside surface", "material":"insideSurface", "type":"conv"}
Rfib={"name":"fiberboard", "material":"woodFiberBoard", "length":0.013, "type":"cond"}
Rins={"name":"insulation", "material":"glassfiber", "length":0.09, "type":"cond"}
Rstud={"name":"wood stud", "material":"woodStud", "length":0.09, "type":"cond"}
RoutS={"name":"Summer Out", "material":"outsideSurfaceSummer", "type":"conv"}
RoutW={"name":"Winter Out", "material":"outsideSurfaceWinter", "type":"conv"}
R_gap={"name":"Gap","type":"gap","epsilon1":0.9, "epsilon2":0.9, "length":0.020}

ResistanceList_withWood=[Rin, Rgyp, Rwood, Rfib, R_gap, Rstud,RoutW]
ResistanceList_withIns=[Rin, Rgyp, Rwood, Rfib,R_gap, Rins, RoutW]

ResistanceList=[ResistanceList_withWood,ResistanceList_withIns]
    
def resistanceoflayer(ResistanceList):
    
                       
    def epsilonEffective(epsilon1, epsilon2):
        epsilon=1/(1/epsilon1+1/epsilon2-1)
        return epsilon

    Result=[]
    
    for j in ResistanceList:
        R_tot=0
        resistances_series={}
        
        for i in j: #for any resistance of any list of resistances in series:
            if i["type"]=="cond":
                material=i["material"]
                length=i["length"]
                lengthT=thermalResDic[material]["length"]
                R=thermalResDic[material]["R"]*length/lengthT
                resistances_series[i["name"]]=R 
                R_tot=R_tot+R
            elif i["type"]=="conv":
                material=i["material"]
                R=thermalResDic[material]["R"]
                resistances_series[i["name"]]=R  
                R_tot=R_tot+R
            elif i["type"]=="gap":
                epsilon=epsilonEffective(i["epsilon1"],i["epsilon2"])
                R=AirGapResDict[i["length"]][epsilon]
                R_tot=R_tot+R
                resistances_series[i["name"]]=R 
                           
            resistances_series["R_tot"]=R_tot
                
        Result.append(resistances_series)
        
    
    return Result #list of 2 dictionaries of resistances in series (0:wood, 1:ins), including the total one for each series (Rtot_wood, Rtot_ins)
    

    
R=resistanceoflayer(ResistanceList) 

DT=24
A=2.5*50*0.8

R_wood=R[0]["R_tot"]
R_ins=R[1]["R_tot"]
U_wood=1/R_wood
U_ins=1/R_ins

U_tot=U_wood*0.25+U_ins*0.75
R_tot=1/U_tot

Q_tot=U_tot*A*DT

print("U with wood studs: " + str(U_wood)+ "  W/(m^2K)")
print("") 
print("U with glass fiber insulation: " + str(U_ins)+ "  W/m^K2")
print("")
print("U_tot: "+ str(U_tot)+ "  W/m^2K")
print("")
print("Rtot: " + str(R_tot)+ " m^2*K/W")
print("")

print("The OVERALL HEAT TRANSFER RATE is:  Q_tot = " + str(Q_tot)+ "  W")

