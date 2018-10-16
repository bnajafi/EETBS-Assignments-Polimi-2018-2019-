#Assignment 3

Tin=2
Tout=-2
A=50*0.8 
A_wood=A*0.25    #25%
A_fiber=A*0.75   #75%

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

Ri={"name":"Inside Air","type":"conv","material":"InsideAir","area":A}
R1={"name":"Wood blevel lapped Siding","type":"cond","material":"WoodLappedSiding","area":A,"lenght":0.013}
R2={"name":"WoodFiberBoard","type":"cond","material":"WoodFiberBoard","area":A,"lenght":0.013}
R3={"name":"Glass Fiber Insulation","type":"cond","material":"GlassFiberIsulation","area":A,"lenght":0.09}
R4={"name":"WoodStud_90mm","type":"cond","material":"WoodStud_90mm","area":A,"lenght":0.9}
R5={"name":"Gypsum Wallboard","type":"cond","material":"Gypsum","area":A,"lenght":0.013}
Ro={"name":"OutSide Surface","type":"conv","material":"outsideSurfaceWinter","area":A}
R_gap={"name":"air gap","type":"gap","epsilon1":0.5,"lenght":0.020}


#with Wood Resistance

R_Wood=[Ri,R1,R2,R4,R5,Ro,R_gap]
R_Ins=[Ri,R1,R2,R3,R5,Ro,R_gap]

def EpsilonEffectiveVectorialOtherOneNormalWay(epsilon1=0.9,epsilon2=0.9):
    """
    this function calculate the effective epsilonEffective.
    if one epsilon is not specified, it cosider the other one as costant = 0.9
    it return the effective epsilon
    """
    result=1/(1/epsilon1+1/epsilon2-1)
    return result

def ResistanceOfLayersInSeries(ListOfResistances):
    """
    ResistanceOfLayersInSeries take a list of Resistance in input and give in output the equivalant Resistance 
    only if the Resistance are in series
    
    """
    resultDictonary={}
    Rtot=0
    
    for Ri in ListOfResistances:
        
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
            effectiveEpsilon=EpsilonEffectiveVectorialOtherOneNormalWay(R_gap["epsilon1"])
            
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
            
    resultDictonary["Rtot"]=Rtot
    return resultDictonary

Rtot1=ResistanceOfLayersInSeries(R_Wood)
Rtot2=ResistanceOfLayersInSeries(R_Ins)

print("the total R_Wood resistance value with wood is "+str(Rtot1["Rtot"])+" ohm")
print("the total R_Ins resistance value with glass isulation is "+str(Rtot2["Rtot"])+" ohm")

U1=1/float(Rtot1["Rtot"])
U2=1/float(Rtot2["Rtot"])
Utot=U1*0.25+U2*0.75
Q=Utot*(Tin-Tout)*A

print("the heat transfer Q though the wall is : "+str(Q)+" W")