#Assignment - 5

import numpy as np

R_names=np.array(["outside_surface","wood_bevel_lapped_Siding","wood_fider_board","glass_fiber_insulation","wood_stud","Gypsum_Wallboard","inside_surface"])
R_types=np.array(["conv","cond","cond","cond","cond","cond","conv"])
R_lengths=np.array([None,0.013,0.013,0.09,0.09,0.013,None])
R_LengthRated=np.array([None,0.013,0.013,0.025,0.09,0.013,None])
R_values=np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])
R_val=np.array(np.zeros(7))
R_val[R_types=="cond"]=R_lengths[R_types=="cond"]/R_LengthRated[R_types=="cond"]*R_values[R_types=="cond"]
R_val[R_types=="conv"]=R_values[R_types=="conv"]
indexWood=R_names!="glass_fiber_insulation"
indexFiber=R_names!="wood_stud"
Rtot_withWood=R_val[indexWood].sum()
Rtot_withInsulation=R_val[indexFiber].sum()

Atot=100
Awood=25
Ains=75
deltaT=24

Uwood=1/Rtot_withWood
Uins=1/Rtot_withInsulation
Utot=(Uwood*(float(Awood)/Atot))+(Uins*(float(Ains)/Atot))
Rtot=1/float(Utot)
Qtot=Utot*Atot*deltaT
print("R total is "+str(Rtot)+"m2.degC/W")
print("U overall is "+str(Utot)+"W/m2.degC")
print("Q total is "+str(Qtot)+"W")