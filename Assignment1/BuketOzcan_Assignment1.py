# -*- coding: utf-8 -*-
R1=["Rcond_1","cond",0.004,0.78,1.2]
R2=["Rcond_2","cond",0.01,0.026,1.2]
R3=["Rcond_3","cond",0.004,0.78,1.2]
R4=["Rconv_1","conv",10,1.2]
R5=["Rconv_2","conv",40,1.2]

ListOfResistances=[R1, R2, R3, R4, R5]
R_total= 0

for anyResistance in ListOfResistances:
    if anyResistance[1]== "cond":
        L=anyResistance[2]
        k=anyResistance[3]
        A=anyResistance[-1]
        print("name: "+anyResistance[0])
        print("type: "+anyResistance[1])
        print("L: "+str(L))
        print("k: "+str(k))
        print("A: "+str(A))
        R_thisResistance=float(L)/(k*A)
        R_total=R_total+R_thisResistance
        print("R: "+str(R_thisResistance)+"  degC/W")
        anyResistance.append(R_thisResistance)   #her listeye R eklemek için
        print("**********************")   
    elif anyResistance[1]== "conv":
        h=anyResistance[2]
        A=anyResistance[3]
        print("name: "+anyResistance[0])
        print("type: "+anyResistance[1])
        print("h: "+str(h))
        print("A: "+str(A))
        R_thisResistance=1/float(h*A)
        R_total=R_total+R_thisResistance
        print("R: "+str(R_thisResistance)+"  degC/W")
        anyResistance.append(R_thisResistance) 
        print("**********************")  

print("Total R: "+str(R_total)+ "  degC/W")