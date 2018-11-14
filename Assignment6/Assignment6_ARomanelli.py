import pandas as pd 

resistance_names = ["R1","R2","R3","R4ins","R4wood","R5","R6","Rgap"]
resistances_types = ["conv","cond","cond","cond","cond","cond","conv","gap"]
resistances_L= [None,0.013,0.013,0.09,0.09,0.013,None,0.020]

R_1={"name":"outsidesurfaceWinter","type":"conv"}
R_2={"name":"woodLappedSiding","type":"cond","length":0.013}
R_3={"name":"woodFiberBoard","type":"cond","length":0.013}
R_4a={"name":"glassfiber","type":"cond","length":0.09}
R_4b={"name":"WoodStud_90mm","type":"cond","length":0.09}
R_5={"name":"gypsum","type":"cond","length":0.013}
R_6={"name":"insideSurface","type":"conv",}
R_gap={"name":"air gap","type":"gap","epsilon1":0.05,"epsilon2":0.9,"length":0.020}

resistances_listOfLists = [R_1,R_2,R_3,R_4a,R_4b,R_5,R_6,R_gap]
resistances_DataFrame = pd.DataFrame(resistances_listOfLists,index=resistance_names, columns =["name","type","length"])  
ThermalResDict = {"FaceBrick":{"R":0.075,"length":0.1},
                  "WoodStud_90mm":{"R":0.63,"length":0.09},
                  "woodFiberBoard":{"R":0.23,"length":0.013},
                  "woodLappedSiding":{"R":0.14,"length":0.013},
                  "gypsum":{"R":0.079,"length":0.013},
                  "insideSurface":{"R":0.12},
                  "outsidesurfaceWinter":{"R":0.03},
                  "outsidesurfaceSummer":{"R":0.044},
                  "glassfiber":{"R":0.70,"length":0.025},
                  } 


def RValue_material(input_material):
    
    RValue_thismaterial = ThermalResDict[input_material]["R"]
           
    return RValue_thismaterial                

def standardLength_material(input_material):
    
    standardLength_thisMaterial = ThermalResDict[input_material]["length"]
    return standardLength_thisMaterial 


#calculation of wood resistences cond
RValue_wood = resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"name"]!="air gap"][resistances_DataFrame.loc[:,"name"]!="glassfiber"].apply(RValue_material)
standardLength_wood = resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"type"]=="cond"][resistances_DataFrame.loc[:,"name"]!="air gap"][resistances_DataFrame.loc[:,"name"]!="glassfiber"].apply(standardLength_material)
R_wood=RValue_wood*resistances_DataFrame.loc[:,"length"][resistances_DataFrame.loc[:,"type"]=="cond"]/standardLength_wood

#calculation of insulation resistences cond
RValue_ins = resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"name"]!="air gap"][resistances_DataFrame.loc[:,"name"]!="WoodStud_90mm"].apply(RValue_material)
standardLength_ins = resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"type"]=="cond"][resistances_DataFrame.loc[:,"name"]!="air gap"][resistances_DataFrame.loc[:,"name"]!="WoodStud_90mm"].apply(standardLength_material)
R_ins=RValue_ins*resistances_DataFrame.loc[:,"length"][resistances_DataFrame.loc[:,"type"]=="cond"]/standardLength_ins


#adding them to the DataFrame
resistances_DataFrame.loc[:,"R_wood"] = R_wood         
resistances_DataFrame.loc[:,"R_ins"] = R_ins         




#adding R conv to values of Rwood
resistances_DataFrame.iloc[0:1,4]=resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"type"]=="conv"].apply(RValue_material)
resistances_DataFrame.iloc[6:7,4]=resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"type"]=="conv"].apply(RValue_material)
#adding R conv to values of Rins
resistances_DataFrame.iloc[0:1,3]=resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"type"]=="conv"].apply(RValue_material)
resistances_DataFrame.iloc[6:7,3]=resistances_DataFrame.loc[:,"name"][resistances_DataFrame.loc[:,"type"]=="conv"].apply(RValue_material)

#Rgap

AirGapResDict={0.020:{0.03:0.051,0.049723756906077346:0.49,0.5:0.23},
                   0.040:{0.03:0.63,0.05:0.59,0.5:0.25}}
epsilon1=0.05
epsilon2=0.9

epseff=1/(1/epsilon1+1/epsilon2-1)


def ResistenceWithGap(length):
     Rvalue = AirGapResDict[length][epseff]
     return Rvalue
     
RAirGap = resistances_DataFrame.loc[:,"length"][resistances_DataFrame.loc[:,"type"]=="gap"].apply(ResistenceWithGap)
#adding Air gap value to two columns
resistances_DataFrame.iloc[7:8,3]=RAirGap
resistances_DataFrame.iloc[7:8,4]=RAirGap

#final sum of resistences
resistances_wood=resistances_DataFrame.loc[:,"R_wood"].sum()
resistances_ins=resistances_DataFrame.loc[:,"R_ins"].sum()


#calculation of U
U_wood=1/resistances_wood
U_ins=1/resistances_ins

A=50*0.8*2.5
DeltaT=24

U_tot=U_wood*0.25+U_ins*0.75
R_tot=1/U_tot
Q=U_tot*A*DeltaT


