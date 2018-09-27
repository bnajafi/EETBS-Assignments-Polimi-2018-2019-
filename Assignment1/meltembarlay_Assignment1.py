#Assignment-1. 
#According to Assignment0 values, insert the total resistance by using range of resistances, for and if commands.

R_1=["inner", "conv", 10, 1.2]   
R_2=["outer", "conv", 40, 1.2]
R_g_1=["glass", "cond", 0.78, 0.004, 1.2]
R_g_2=R_g_1
R_a=["air", "cond", 0.026, 0.01, 1.2]

ListOfResistances = [R_1, R_2, R_g_1, R_g_2, R_a]
R_total = 0

for anyResistance in ListOfResistances:
    if anyResistance[1]=="conv":
        h=anyResistance[2]
        A=anyResistance[-1]
        print("status: "+anyResistance[0])
        print("type: "+anyResistance[1])
        print("h: "+str(h))
        print("A: "+str(A))
        R_thisResistance=1/(float(h)*A)
        R_total=R_total+R_thisResistance
        print("R: "+str(R_thisResistance)+ " degC/W")
        print("*****************")
    elif anyResistance[1]=="cond":
        L=anyResistance[3]
        k=anyResistance[2]
        A=anyResistance[-1]
        print("status: "+anyResistance[0])
        print("type: "+anyResistance[1])
        print("L: "+str(L))
        print("k: "+str(k))
        print("A: "+str(A))
        R_thisResistance= float(L)/(k*A)
        R_total=R_total+R_thisResistance
        print("R: "+str(R_thisResistance)+ " degC/W")
        print("*****************")
    else:
        print("please check your values!")
        print("*****************")
print("total R: "+str(R_total))
        

