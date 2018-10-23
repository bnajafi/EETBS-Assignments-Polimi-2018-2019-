import os
import sys   
ThisFileDirectory=os.path.dirname(sys.argv[0])   #it says where we are running the file 
os.chdir(ThisFileDirectory)    
print os.getcwd() 

#Definig the folder where is my file
Folderofmywallcalculation=r"C:\\Users\\gelli\\Desktop\\POLIMI FIRST YEAR\\ENERGY AND ENVIRONMENTAL SYSTEM FOR BUILDINGS\\Files solved in Python"
import os
os.chdir(Folderofmywallcalculation)

#First way to import

import WallFunction_HCordoba as WFHC  #importing the file where is assignment #3
Dictionaryofthermalresistances=WFHC.ThermalResDict   
Dictionaryofairgap=WFHC.AirGapResDict
DictionaryR1=WFHC.R_1
DictionaryR2=WFHC.R_2
DictionaryR3=WFHC.R_3
DictionaryR4=WFHC.R_4
DictionaryR5=WFHC.R_5
DictionaryR6=WFHC.R_6
DictionaryR7=WFHC.R_7
DictionaryRGAP=WFHC.R_gap


resistancesListWithWood=[R_1,R_2,R_3,R_5,R_6,R_4, R_gap]
resistancesListWithInsulation=[R_1,R_2,R_7,R_5,R_6,R_4, R_gap]

#Calculating The Value of my epsilon Effective
myEpsilonEffective=WFHC.epsilonEffective(R_gap["epsilon1"],R_gap["epsilon2"])

#Calculation the Value of the resistances for wood and insulation and list all values of resistances on a dictionary

resistancesforwood=WFHC.ResistanceOfLayerInSeries(resistancesListWithWood)
resistancesforinsulation=WFHC.ResistanceOfLayerInSeries(resistancesListWithInsulation)

#Giving the value for Rtotal for insulation for wood and insulation
print("RESISTANCE FOR WOOD IS " + str(WFHC.Rwood)  ) 
print("RESISTANCE FOR INSULATION IS " + str(WFHC.Rinsulation))

#Calculation U, R total for the problem. Also, calculating the rate of heat loss through the walls
print("UTOTAL FOR THIS PROBLEM IS " + str(WFHC.U_total) )  
print("RTOTAL FOR THIS PROBLEM IS " + str(WFHC.R_total))
print("THE RATE OF HEAT LOSS THROUGH THE WALLS " + str(WFHC.Q_total))


print("THE RESULTS CALLING THE FUNCTION IN ANOTHER WAY")

#Second way to import

from WallFunction_HCordoba import *

#Calculating The Value of my epsilon Effective
myEpsilonEffective=epsilonEffective(R_gap["epsilon1"],R_gap["epsilon2"])

#Calculation the Value of the resistances for wood and insulation and list all values of resistances on a dictionary

resistancesforwood=ResistanceOfLayerInSeries(resistancesListWithWood)
resistancesforinsulation=ResistanceOfLayerInSeries(resistancesListWithInsulation)

#Giving the value for Rtotal for insulation for wood and insulation
print("RESISTANCE FOR WOOD IS " + str(Rwood)  ) 
print("RESISTANCE FOR INSULATION IS " + str(Rinsulation))

#Calculation U, R total for the problem. Also, calculating the rate of heat loss through the walls
print("UTOTAL FOR THIS PROBLEM IS " + str(U_total) )  
print("RTOTAL FOR THIS PROBLEM IS " + str(R_total))
print("THE RATE OF HEAT LOSS THROUGH THE WALLS " + str(Q_total))


