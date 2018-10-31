# -*- coding: utf-8 -*-
import numpy as np

MaterialNames=np.array(["OutsideSurfaceWinter","Wood_bevel_lapped_siding","fiberboard","Glass_fiber_ıns","Wood_studs","Gypsum","inside_surface"])
ResistanceTypes=np.array(["Conv","Cond","Cond","Cond","Cond","Cond","Conv"])
ResistanceLengthReal=np.array([None,0.013,0.013,0.09,0.09,0.013,None])
ResistanceRValue=np.array([0.03,0.14,0.23,0.7,0.63,0.079,0.12])
ResistanceLengthDict=np.array([None,0.013,0.013,0.025,0.09,0.013,None])

Resistances_RValues=np.array(np.zeros(7))

Resistances_RValues[ResistanceTypes=="Cond"]=ResistanceLengthReal[ResistanceTypes=="Cond"]/ResistanceLengthDict[ResistanceTypes=="Cond"]*ResistanceRValue[ResistanceTypes=="Cond"]
Resistances_RValues[ResistanceTypes=="Conv"]=ResistanceRValue[ResistanceTypes=="Conv"]
WithWood=MaterialNames!="Glass_fiber_ıns"
WithInsulation=MaterialNames!="Wood_studs"
Rtot_withWood=Resistances_RValues[WithWood].sum()
Rtot_withInsulation=Resistances_RValues[WithInsulation].sum()

print("R total with wood is "+ str(Rtot_withWood)+" m2.degC/W")
print("R total with insulation is "+ str(Rtot_withInsulation)+" m2.degC/W")
        
Atot=100
Awood=25
Ains=75
DeltaT=24
Uwood=1/float(Rtot_withWood)
Uins=1/float(Rtot_withInsulation)
Utot=(Uwood*(float(Awood)/Atot))+(Uins*(float(Ains)/Atot))
Rtot=1/float(Utot)
Qtot=Utot*Atot*DeltaT
print("R total is "+str(Rtot)+" m2.degC/W")
print("U overall is "+str(Utot)+" W/m2.degC")
print("Q total is "+str(Qtot)+" W")