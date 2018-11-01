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


    
    