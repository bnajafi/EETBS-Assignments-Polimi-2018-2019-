#Example 1 Unit 1.2

#Calculate the overall unit thermal resistance (Rtotal) and overall heat transfer coefficient (Utotal)
#Data:
ThermalResDict={"GlassFiberInsulation":{"R":2.52,"length":0.09},
                "WoodStud_90mm":{"R":0.63,"length":0.09},
                "WoodFiberBoard":{"R":0.23,"length":0.013},
                "WoodLappedSiding":{"R":0.14,"length":0.013},
                "Gypsum":{"R":0.079,"length":0.013},
                "InsideSurface":{"R":0.12},
                "OutsideSurface":{"R":0.03},}

Ri=["InsideSurface","conv",0.12]
R2=["WoodLappedSiding","cond",0.013,0.14,0.013]
R3=["WoodFiberBoard","cond",0.013,0.23,0.013]
R4=["GlassFiberInsulation","cond",0.09,2.52,0.09]
R5=["WoodStuds","cond",0.09,0.63,0.09]
R6=["Gypsum","cond",0.013,0.079,0.013]
Ro=["OutsideSurface","conv",0.03]

ResistanceList_withWood=[Ri,R2,R3,R5,R6,Ro]
ResistanceList_withInsulation=[Ri,R2,R3,R4,R6,Ro]

#Transforming the data into arrays:

import numpy as np
names= np.array(["InsideSurface","WoodLappedSiding","WoodFiberBoard","GlassFiberInsulation","WoodStuds","Gypsum","OutsideSurface"])
types=np.array(["conv","cond","cond","cond","cond","cond","conv"])
length=np.array([1,0.013,0.013,0.09,0.09,0.013,1]) #I write '1' for convection type
resistance=np.array([0.12,0.14,0.23,2.52,0.63,0.079,0.03])
length_library=np.array([1,0.013,0.013,0.09,0.09,0.013,1]) #I write '1' for convection type. This way I don't consider them
list_withWood=np.array(["Yes","Yes","Yes","No","Yes","Yes","Yes"])
list_withInsulation=np.array(["Yes","Yes","Yes","Yes","No","Yes","Yes"])


RValues_withWood=np.array(np.zeros(7))
RValues_withWood[list_withWood=="Yes"]=resistance[list_withWood=="Yes"]*(length[list_withWood=="Yes"]/length_library[list_withWood=="Yes"])
Rtot_withWood=RValues_withWood.sum()

RValues_withInsulation=np.array(np.zeros(7))
RValues_withInsulation[list_withInsulation=="Yes"]=resistance[list_withInsulation=="Yes"]*(length[list_withInsulation=="Yes"]/length_library[list_withInsulation=="Yes"])
Rtot_withInsulation=RValues_withInsulation.sum()


U_wood=1/Rtot_withWood
U_insulation=1/Rtot_withInsulation
Utotal=0.25*U_wood+0.75*U_insulation
print("The total heat transfer coefficient is Utotal= "+str(Utotal))
Rtotal=1/Utotal
print("The total thermal resistance is Rtotal= "+str(Rtotal))

#Rate of heat loss through the walls
Area=50*2.5*0.8
T_1=22
T_2=-2
Q=Utotal*Area*(T_1-T_2)
print("The rate of heat loss through the walls is Q= "+str(Q))