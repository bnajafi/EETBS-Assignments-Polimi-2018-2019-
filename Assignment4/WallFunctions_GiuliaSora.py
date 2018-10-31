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

def resistanceFunction(List):
    """This function, given a list of resistances, computes the Total Resistance and creates a dictionary (dictio)
       in which there are all the layers and the corrisponding resistance just calculated"""
    dictio={}
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
                    effectiveEpsilon=0.05                      #verificare dalla tab che efettivamente i valori siano soloquei3
                else:
                    effectiveEpsilon=0.5
                    
                    
                length=anyresistance["length"]
                resistance=AirGapResDict[length][effectiveEpsilon]                   #verificare che ponendo il dictio      
                R_tot=R_tot+resistance                                  #dentro la def prima del for non fa danni
                anyresistance["Rvalue"]=resistance
                dictio[anyresistance["name"]]=anyresistance["Rvalue"]
            else: 
                print("It seems that there is a problem with the resistance")
                print(anyresistance["name"])
        
    return R_tot,dictio

def Utot(Tin,Tout,A,R_tot1,R_tot2):
     U1=1/float(R_tot1)
     U2=1/float(R_tot2)
     U_overall=U1*0.25+U2*0.75
     Q=U_overall*(Tin-Tout)*A

     return U_overall,Q
    
        
        #creo una funzione che prende le due R e calcola U,Q?