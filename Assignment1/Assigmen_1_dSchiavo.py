# -*- coding: utf-8 -*-
t_inf1=20.0   #inlet temperature
t_inf2=-10.0  #outlet temperature
D_T=(t_inf1-t_inf2)
H=0.8  # height of he window
W=1.5  # wide of the window
A= H*W  #Area of the window
R1=["R_air_in","conv", 10.0, A] #defining the sting for the resistance of the in air
R2=["R_glass","cond", 0.004,0.78,A] #defining the sting for the resistance of the glass
R3=["R_air","cond", 0.01,0.026,A] #defining the sting for the resistance of the air between the glasses
R4=["R_glass","cond", 0.004,0.78,A] #defining the sting for the resistance of the glasse
R5=["R_air_out","conv", 40,A] #defining the sting for the resistance of the out air

R_tot=0

ListOfResistance=[R1,R2,R3,R4,R5] # list containing all the resistance
for i in ListOfResistance: # for cycle which analizes all the resistance
    if i[1]=="cond":  # if it's a conduction coefficient then:
         l=i[2]   # extract by the list l, k and the area
         k=i[3]
         a=i[4]
         R=l/(a*k) # computing the resistance
         print("Name " + i[0])
         print("type " + i[1])
         print("L " + str(l))
         print("k " + str(k))
         print("A " + str(a))
         print("Resistance " + str(R)+ "   °C/W")
         print("******************")
         i.append(R) #adding the computed resistance to its list
         R_tot=R_tot+R  #computing the total resistance
    elif i[1]=="conv":   # if it's a convection coefficient then:
         h=i[2]  #extract h and a
         a=i[3]
         R=1/(h*a)    #compute the resistance  
         print("Name " + i[0])
         print("type " + i[1])        
         print("h " + str(h))
         print("A " + str(a))
         print("Resistance " + str(R)+ "   °C/W")
         print("******************")
         i.append(R) #adding the computed resistance to its list
         R_tot=R_tot+R  # computing the totla resistance
    else:
        print("error, something goes wrong")

print("the total resistances is " + str(R_tot)+ "   °C/W")
Q=D_T/R_tot  # the total heat  transfer 
print( "the heat transfer is equal to " + str(Q)+ "  W")
T_inner=t_inf1-Q*R1[-1] # the inner temperature
print("the inner temperature is " + str(T_inner)+  "  °C")
