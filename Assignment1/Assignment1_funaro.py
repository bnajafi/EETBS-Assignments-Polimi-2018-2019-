# -*- coding: utf-8 -*-
#assignment 1
#funaro_eleonora
#EXAMPLE B

T_in=20              
T_out=-10 

R_in=["inner air","conv",10,0.8,1.5]
R_out=["outer air","conv",40,0.8,1.5]
R_wall1=["wall1","cond",0.78,0.8,1.5,0.004]
R_wall2=["wall2","cond",0.78,0.8,1.5,0.004]
R_gap=["gap","cond",0.026,0.8,1.5,0.010]

ListOfResistances=[R_in,R_out,R_wall1,R_wall2,R_gap]

R_tot=0
for anyResistance in ListOfResistances:       
    if anyResistance[1]=="cond":             
        k=anyResistance[2]
        height=anyResistance[3]
        wide=anyResistance[4]
        L=anyResistance[5]
        print("name: " +anyResistance[0])
        print("type: " +anyResistance[1])
        print("k: " +str(k))
        print("height: " +str(height))
        print("wide: " +str(wide))
        print("L: " +str(L))
        R_thisResistance=float((L)/(k*height*wide))
        print("R: "+str(R_thisResistance) +"°C/W")
        anyResistance.append(R_thisResistance)
    if anyResistance[1]=="conv":
        h=anyResistance[2]
        height=anyResistance[3]
        wide=anyResistance[4]
        print("name: " +anyResistance[0])
        print("type: " +anyResistance[1])
        print("h: " +str(h))
        print("height: " +str(height))
        print("wide: " +str(wide))
        R_thisResistance=(1/(h*height*wide))
        print("R: "+str(R_thisResistance) +"°C/W")
        anyResistance.append(R_thisResistance)
    R_tot=R_tot+R_thisResistance
    print("*********************")
print("Rtot: " +str(R_tot))

Q=(T_in-T_out)/R_tot
print("The value of the heat transferred is: "+str(Q)+"W")              

T1=T_in-(Q*R_in[-1]) 
print("the inner temperature is: " +str(T1)+"°C")  