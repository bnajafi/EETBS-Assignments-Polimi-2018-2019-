#assignment5
#funaro_eleonora


import numpy as np   

Awood=0.25
Ainsulation=0.75
Atot=100 
dT=24

R_1 = ["glass_fiber","cond",2.52, 0.09]
R_2 = ["wood_stud","cond",0.63, 0.09]
R_3 = ["wood_fiberBoard","cond",0.23, 0.013]
R_4 = ["wood_bevelLappedSiding","cond",0.14,0.013]
R_5 = ["gypsum_wallboard","cond",0.079,0.013]
R_i = ["inside_surface","conv",0.12]
R_o = ["outside_surface","conv",0.03]

resistance_namesGlass=np.array(["glass_fiber","wood_fiberBoard","wood_bevelLappedSiding","gypsum_wallboard","inside_surface","outside_surface"])
resistance_namesWood=np.array(["wood_stud","wood_fiberBoard","wood_bevelLappedSiding","gypsum_wallboard","inside_surface","outside_surface"])
resistance_types=np.array(["cond","cond","cond","cond","conv","conv"])
resistance_RWood=np.array([0.63,0.23,0.14,0.079,0.12,0.03])
resistance_RGlass=np.array([0.7,0.23,0.14,0.079,0.12,0.03])
resistance_LReal=np.array([0.09,0.013,0.013,0.013,None,None])
resistance_LWood=np.array([0.09,0.013,0.013,0.013,None,None])
resistance_LGlass=np.array([0.025,0.013,0.013,0.013,None,None])

resistance_Wood=np.array(np.zeros(6))
resistance_Glass=np.array(np.zeros(6))

resistance_Wood[resistance_types=="cond"]=(resistance_RWood[resistance_types=="cond"]*resistance_LWood[resistance_types=="cond"])/resistance_LReal[resistance_types=="cond"]    
resistance_Wood[resistance_types=="conv"]=resistance_RWood[resistance_types=="conv"]
RWood=resistance_Wood.sum()

resistance_Glass[resistance_types=="cond"]=(resistance_RGlass[resistance_types=="cond"]*resistance_LReal[resistance_types=="cond"])/resistance_LGlass[resistance_types=="cond"]    
resistance_Glass[resistance_types=="conv"]=resistance_RGlass[resistance_types=="conv"]
RGlass=resistance_Glass.sum()

print("Rwood: " +str(RWood))  
print("Rinsulation: " +str(RGlass))

Uinsulation=1/RGlass
Uwood=1/RWood
Utot=(Uinsulation*Ainsulation)+(Uwood*Awood)
Rtot=1/Utot

print("Rtot: " +str(Rtot))

Q=(Atot*dT)/Rtot
        
print("Q: " +str(Q))       
