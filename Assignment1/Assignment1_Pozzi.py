# -*- coding: utf-8 -*-

#Gilberto Pozzi
#Assignement1: Determinate the steady rate of heat transfer through a window and the temperature of its inner surface:

t_in=20.0
t_out=-10.0 
DT=(t_in-t_out)
H=0.8  
W=1.5  
A= H*W  

#Definition of the resistances:
#
Rin=["R_air_in","conv", 10.0, A] 
Rglass=["R_glass","cond", 0.004,0.78,A] 
Rair=["R_stagnant_air","cond", 0.01,0.026,A] #stagnant air between glasses
Rout=["R_air_out","conv", 40,A] 

R_tot=0

ListOfResistance=[Rin,Rglass,Rair,Rglass,Rout] # list containing all the resistances

#Computation of all resistances and calculation of the overall one:
for i in ListOfResistance: 
    if i[1]=="cond":  
         l=i[2]   
         k=i[3]
         a=i[4]
         R=l/(a*k) 
         print("Name: " + i[0])
         print("type: " + i[1])
         print("R value: " + str(R)+ " °C/W")
         print("____________________________________")
         i.append(R) #adds the Ri-value to the "Ri description list"
         R_tot=R_tot+R  
    elif i[1]=="conv":   
         h=i[2]  
         a=i[3]
         R=1/(h*a)      
         print("Name: " + i[0])
         print("type: " + i[1])
         print("R value: " + str(R)+ " °C/W")
         print("____________________________________")
         i.append(R) 
         R_tot=R_tot+R  
    else:
        print("ERROR: Unvalid resistance type")


#steady rate of heat transfer:
Q=DT/R_tot

# Inner surface temperature:
T_in_surface=t_in-Q*Rin[-1]

#printing results:

print("the total thermal resistances is: " + str(R_tot)+ "   °C/W")

print( "the heat transfer rate is: " + str(Q)+ "  W")

print("the inner temperature is: " + str(T_in_surface)+  "  °C")

