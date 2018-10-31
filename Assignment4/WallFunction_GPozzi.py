thermalResDic= {"gypsum":{"R":0.079, "length":0.013}, "Plywood":{"R":0.11, "length":0.013},
"insideSurface":{"R":0.12}, "outsideSurfaceWinter":{"R":0.03}, "outsideSurfaceSummer":{"R":0.044},"woodLappedSiding":{"R":0.14, "length":0.013},
"woodFiberBoard":{"R":0.23, "length":0.013}, "woodStud":{"R":0.63, "length":0.09},"glassfiber":{"R":0.7, "length":0.025}}

AirGapResDict={0.02:{0.03:0.051, 0.8181818181818181:0.17, 0.5:0.23},
            0.04:{0.03:0.63, 0.05:0.59, 0.5:0.25}}    #Dictionary with tabulated values of R for different distances end epsilons in an air gap
            
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
