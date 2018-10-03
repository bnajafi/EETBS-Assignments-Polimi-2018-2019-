# -*- coding: utf-8 -*-
b=0.8 #Highness of the double-pane window[m]
w=1.5 #Width of the double-pane window [m]
A=b*w #Total area [m2]
L_g=0.004 #thickness of the glass [m]
k_g=0.78 #Conductive resistance of the glass [W/(m°C)]
h_1=10 #Convective resistance of the inner surface [W/m2]
h_2=40 #Convective resistance of the outer surface [W/m2]
T_in=20 #Temperature of the inner space
T_out=-10 #temperature of the outer space
k_a=0.026 #Conductive resistance of the stagnant air [W/m2]
L_a=0.01 #Thickness of the stagnant air space [m]

R1=['Inner Surface','conv',h_1,A]
R3=['glass','cond',L_g,k_g,A]
R4=['air','cond',L_a,k_a,A]
R5=['glass','cond',L_g,k_g,A]
R2=['Outer surface','conv',h_2,A]

R_tot=0
Resistances=[R1,R3,R4,R5,R2]
for resistance in Resistances:
    if resistance[1]=='cond':
        
        Rc=float(resistance[2])/(resistance[3]*resistance[4])
        resistance.append(Rc)
        
        print("Material: "+resistance[0])
        print("Type: "+resistance[1])
        print("L: "+str(resistance[2]))
        print("k: "+str(resistance[3]))
        print("A: "+str(resistance[4]))
        print("R: "+str(resistance[-1]))
        print("*************************")
        
    elif resistance[1]=='conv':
        
        Rc=1/(float(resistance[2])*resistance[3])
        resistance.append(Rc)        
        print("Material: "+resistance[0])
        print("Type: "+resistance[1])
        print("h: "+str(resistance[2]))
        print("A: "+str(resistance[3]))
        print("R: "+str(resistance[-1]))
        print("*************************")        
    else:
        print ("Error!")

    R_tot=R_tot+Rc
print('The total resistance is: '+str(R_tot)+' [°C/W]')
U=1/float(R_tot)
Q=U*(T_in-T_out)

T1=T_in-Q*Resistances[0][-1]
print('The steady rate of heat is: '+str(Q)+' [W]')
print('The temperature of the inner surface is: '+str(T1)+' [°C]')



    


