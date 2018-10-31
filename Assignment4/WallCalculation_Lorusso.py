#Assignment 4

#WallCalculations


ThermalResDic={"FaceBrick":{"R":0.075,"lenght":0.1}
,"WoodStud_90mm":{"R":0.36,"lenght":0.09}
,"WoodFiberBoard":{"R":0.24,"lenght":0.013}
,"GlassFiberIsulation":{"R":0.7,"lenght":0.025}
,"WoodLappedSiding":{"R":0.14,"lenght":0.013}
,"Gypsum":{"R":0.079,"lenght":0.013}
,"InsideAir":{"R":0.12}
,"outsideSurfaceWinter":{"R":0.03}
,"outsideSurfaceSummer":{"R":0.044}
}

AirGapDict={
            0.020:{0.03:0.05,0.05:0.49,0.5:0.23},
            0.040:{0.03:0.063,0.05:0.59,0.5:0.25}
            }

def EpsilonEffective(epsilon1=0.9,epsilon2=0.9):
    """
    
    this function calculate the effective epsilonEffective.
    if one epsilon is not specified, it cosider the other one as costant = 0.9
    it return the effective epsilon
    
    """
    result=1/(1/epsilon1+1/epsilon2-1)
    return result

def ResistanceOfLayersInSeries(ResistancesInSeries):
    """
    ResistanceOfLayersInSeries take a Dict of Resistance in input and give in output the equivalant Resistance 
    only if the Resistance are in series
    
    """
    resultDictonary={}
    Rtot=0
    Rserie=ResistancesInSeries["serie"]
    for Ri in Rserie:
        
        if Ri["type"]=="cond":
            material=Ri["material"]
            lenght=Ri["lenght"]
            R_Value= ThermalResDic[material]["R"]*lenght/ThermalResDic[material]["lenght"]
            Ri["RValue"]=R_Value
            resultDictonary[Ri["name"]]= Ri["RValue"]
            Rtot=Rtot+R_Value
        elif Ri["type"]=="conv":
            material=Ri["material"]
            R_Value= ThermalResDic[material]["R"]
            Ri["RValue"]=R_Value
            resultDictonary[Ri["name"]]= Ri["RValue"]
            Rtot=Rtot+R_Value
        elif Ri["type"]=="gap":
            effectiveEpsilon=EpsilonEffective(Ri["epsilon1"])
            
            for Eps in AirGapDict[Ri["lenght"]]:
                
                if effectiveEpsilon > 0.5:
                    if (effectiveEpsilon-Eps)/effectiveEpsilon < 0.2:
                        effectiveEpsilon=Eps
                        print("Effective Epsilon is = "+str(Eps)+" with an error < 0.2")
                    else:
                        print("epsilon effective is not inside the dictory, please correct the input")
                elif (Eps-effectiveEpsilon)>0 :
                    if (Eps-effectiveEpsilon)/Eps < 0.01: #error < 1%
                        effectiveEpsilon=Eps
                        print("Effective Epsilon is = "+str(Eps)+" with an error < 0.01")
                    elif (Eps-effectiveEpsilon)/Eps > 0.01:
                        if (Eps-effectiveEpsilon)/Eps < 0.1:#error < 10%
                            effectiveEpsilon=Eps
                            print("Effective Epsilon is = "+str(Eps)+" with an error < 0.1")
                    else :
                        print("epsilon effective is not inside the dictory, please correct the input")
                
                        
            RValue_anyResistance = AirGapDict[Ri["lenght"]][effectiveEpsilon]
            Ri["RValue"]=RValue_anyResistance 
            resultDictonary[Ri["name"]]= Ri["RValue"]
            Rtot=Rtot+RValue_anyResistance
            
        else :
            print("the resitance "+str(Ri["name"])+"has its type not corretly define")
            
    resultDictonary["Name" ]=ResistancesInSeries["Name"]
    resultDictonary["Rtot"]=Rtot
    resultDictonary["Uvalue"]=1/float(Rtot)
    resultDictonary["Area"]=ResistancesInSeries["Area"]
    return resultDictonary



def HeatTransfer(T1,T2,Utot,A):
    Q=Utot*A*(T1-T2)
    result=Q
    return result
