delta_t= 24
A_insulation=0.75
A_wood=0.25

R_i = ["insidesurface","conv",0.12]
R_O = ["outsidesurface","conv",0.03]
R_1 = ["Glassfiberinsulation","cond",2.52, 0.09]
R_2 = ["woodStud_90mm","cond",0.63, 0.09]
R_3 = ["woodfiber_Board","cond",0.23, 0.013]
R_4 = ["wood_bevelLappedSiding","cond",0.14,0.013]
R_5 = ["gypsum","cond",0.079,0.013]

namesforinsulation=np.array(["Glassfiberinsulation","woodfiber_Board","wood_bevelLappedSiding","gypsum","insidesurface","outsidesurface"])
namesforwood=np.array(["woodStud_90mm","woodfiber_Board","wood_bevelLappedSiding","gypsum","insidesurface","outsidesurface"])
types=np.array(["cond","cond","cond","cond","conv","conv"])
Rwoodresistance=np.array([0.63,0.23,0.14,0.079,0.12,0.03])
Rinsulationresistance=np.array([0.7,0.23,0.14,0.079,0.12,0.03])
resistance_Length=np.array([0.09,0.013,0.013,0.013,None,None])
resistance_LWood=np.array([0.09,0.013,0.013,0.013,None,None])
resistance_LInsulation=np.array([0.025,0.013,0.013,0.013,None,None])
Rwood=np.array(np.zeros(6))
Rinsulation=np.array(np.zeros(6))
Rwood[types=="cond"]=(Rwoodresistance[types=="cond"]*resistance_LWood[types=="cond"])/resistance_Length[types=="cond"]    
Rwood[types=="conv"]=Rwoodresistance[types=="conv"]
R_Wood=Rwood.sum()
Rinsulation[types=="cond"]=(Rinsulationresistance[types=="cond"]*resistance_Length[types=="cond"])/resistance_LInsulation[types=="cond"]    
Rinsulation[types=="conv"]=Rinsulationresistance[types=="conv"]
R_Insulation=Rinsulation.sum()


U_insulation= 1/(R_Insulation)
U_wood= 1/(R_Wood)


U_total= U_insulation*A_insulation + (U_wood*A_wood)#This is the second answer
R_total= 1/U_total  #This is the first answer
print("The Total resistance for the problem is " + str(R_total))
print("The Total U for the problem is " + str(U_total))
#Now we have the area that is not covered by glazin

A_noglazing= 0.8*2.5*50

#We have the temperature difference

#Now we can determine the rate of heat loss through the walls

Q_total= U_total*A_noglazing*delta_t

print("the rate of heat loss through the walls " + str(Q_total))