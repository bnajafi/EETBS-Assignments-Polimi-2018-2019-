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

AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23},
                   0.040:{0.03:0.063,0.05:0.59,0.5:0.25}}
    
def epsilonEffective(epsilon1=0.05, epsilon2=0.9):
    result=round(1/(1/epsilon1+1/epsilon2-1),2)  
    return result
    

def TotalResistances (ResistanceList):
    R_tot=0
    Results={}

    for i in ResistanceList:
        if i["type"]=="Cond":
            material=i["Material"]
            length=i["Length"]
            lengthT=ThermalConRes[material]["length"] #use concatenated libraries # the material is that found at line 42
            # take the element lenght related to the n material of the library ThermalConRes
            R=ThermalConRes[material]["R"]*length/lengthT 
            Results[i["Name"]]=R # I'm adding to the empty library Results l'i[Name] and I put it equal to R
            R_tot=R_tot+R
        elif i["type"]=="Conv":
            material=i["Material"]
            R=ThermalConRes[material]["R"]
            R_tot=R_tot+R
            Results[i["Name"]]=R
            R_tot=R_tot+R
        elif i["type"]=="Gap":
            effectiveEpsilon=epsilonEffective(i["epsilon1"],i["epsilon2"])
            RValue_i = AirGapResDict[i["length"]][effectiveEpsilon]
            i["RValue"]=RValue_i 
            Results[i["name"]]= i["RValue"]
            R_tot=R_tot+RValue_i
    Results["R_tot"]=R_tot
    return Results
        