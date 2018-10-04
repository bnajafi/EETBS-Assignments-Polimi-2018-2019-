#EXAMPLE B USING LISTS AND CONDITIONS

#WE ARE GOING TO USE FOR TO SELECT THE LIST AND IF TO IDENTIFY THE TYPE OF HEAT TRANSFER AND SOLVED THE RESISTANCES


R1= ["R_Air","conv", 10, 1.2]
R2= ["R_wood","cond", 0.78, 1.2, 0.008]
R3= ["R_Air","conv", 40, 1.2]

Resist=[R1,R2,R3]
R_total=0
for Resistances in Resist:
       typ=Resistances[1]
       if typ == "conv":
            h=Resistances[2]
            A=Resistances[-1]
            print("name: " + Resistances[0])
            print("type: " + str(typ))
            print("h: " + str(h) )       
            print("A: " + str(A) )
            R_thisResistance=float(1)/(h*A)
            print("The resistance " + str(R_thisResistance))
            print("*********************************") 
       elif typ == "cond":
            L=Resistances[-1]
            k=Resistances[2]
            A=Resistances[3]
            print("name: " + Resistances[0])
            print("type: " + Resistances[1])
            print("L: " +str(L) )
            print("k: " + str(k) )       
            print("A: " + str(A) )
            R_thisResistance=float(L)/(k*A)
            print("The resistance " + str(R_thisResistance))
            print("*********************************")
       R_total=R_total+ R_thisResistance
       print("The total resistance " + str(R_total))
       print("*********************************")
       
Solved=[R1,R2,R3,R_total,20,-10]
Q_total=(Solved[4]-Solved[-1])/Solved[3]
print("The value of the net heat transfer "+ str(Q_total))
R_conv1=0.08333333
R_conv2=0.02083333
T_1= (Solved[4]-(R_conv1*Q_total))
T_2= (Solved[-1]+(R_conv2*Q_total))
print("The first inner temperature is "+ str(T_1))
print("The second inner temperature is "+ str(T_2))

       
       


    