# -*- coding: utf-8 -*-
#
Tin=22       #Temperature in the inside
Tout=-2     #Temperature in the outside
A=50*2.5*0.8 #Portion of area made by wall
A_wood=A*0.25 
A_fiber=A*0.75

ThermalResDict={"Outside Air":{"R":0.03},
                "Wood Bevel Lapped Siding":{"R":0.14,"l":0.013},
                "Wood Fiberboard":{"R":0.23,"l":0.013},
                "Glass Fiber Insulation":{"R":0.7,"l":0.025},
                "Wood Stud":{"R":0.63,"l":0.9},
                "Gypsum":{"R":0.079,"l":0.013},
                "Inside Air":{"R":0.12}
                }
 
AirGapResDict={0.020:{0.03:0.051,0.05:0.49,0.5:0.23},0.040:{0.03:0.45,0.05:0.43,0.5:0.22},
              0.090:{0.03:0.47,0.05:0.45,0.5:0.22}}                                                         
              
def epsilonEff(epsilon1,epsilon2):
    """This function, given the values of epsilon1 and epsilon2,calculates the epsilon effective """
    result=(1/(1/epsilon1+1/epsilon2-1))
    return result 
    
                                  
R1={"name":"Outside Air","type":"conv","A":A}
R2={"name":"Wood Bevel Lapped Siding","type":"cond","l":0.013,"area":A}
R3={"name":"Wood Fiberboard","type":"cond","l":0.013,"area":A}
R4={"name":"Glass Fiber Insulation","type":"cond","l":0.09,"area":A}
R5={"name":"Wood Stud","type":"cond","l":0.9,"area":A}
R6={"name":"Gypsum","type":"cond","l":0.013,"area":A}
R7={"name":"Inside Air","type":"conv","area":A}
R_gap={"name":"air-gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

resistancesListWithWood=[R1,R2,R_gap,R3,R5,R6,R7]
resistanceListFiberGlass=[R1,R2,R_gap,R3,R4,R6,R7]

dictio={}

def resistanceFunction(List):
    """This function, given a list of resistances, computes the Total Resistance and creates a dictionary (dictio)
       in which there are all the layers and the corrisponding resistance just calculated"""
    R_tot=0
    for anyresistance in List:
        if anyresistance["type"]=="cond":
            material=anyresistance["name"]
            length=anyresistance["l"]
            resistance=ThermalResDict[material]["R"]*length/ThermalResDict[material]["l"]
            R_tot=R_tot+resistance
            anyresistance["Rvalue"]=resistance
            dictio[anyresistance["name"]]=anyresistance["Rvalue"]
        elif anyresistance["type"]=="conv":
            material=anyresistance["name"]
            resistance=ThermalResDict[material]["R"]
            R_tot=R_tot+resistance
            anyresistance["Rvalue"]=resistance
            dictio[anyresistance["name"]]=anyresistance["Rvalue"]
        elif anyresistance["type"]=="gap":
            eps1=anyresistance["epsilon1"]
            eps2=anyresistance["epsilon2"]
            effectiveEpsilon=epsilonEff(eps1,eps2)
            d1=abs(effectiveEpsilon-0.03)
            d2=abs(effectiveEpsilon-0.05)
            d3=abs(effectiveEpsilon-0.5)
            
            if (d1<d2 and d1<d3):
                effectiveEpsilon=0.03
            elif (d2<d1 and d2<d3):
                effectiveEpsilon=0.05
            else:
                effectiveEpsilon=0.5
                
                
            length=anyresistance["length"]
            resistance=AirGapResDict[length][effectiveEpsilon]         
            R_tot=R_tot+resistance
            anyresistance["Rvalue"]=resistance
            dictio[anyresistance["name"]]=anyresistance["Rvalue"]
        else: 
            print("It seems that there is a problem with the resistance")
            print(anyresistance["name"])

    return R_tot
            
 
R_tot1=resistanceFunction(resistancesListWithWood)
R_tot2=resistanceFunction(resistanceListFiberGlass)

U1=1/float(R_tot1)
U2=1/float(R_tot2)
U_overall=U1*0.25+U2*0.75
Q=U_overall*(Tin-Tout)*A
print ("La U totale è: "+str(U_overall))
print ("La Q totale è: "+str(Q))
                                                                                 