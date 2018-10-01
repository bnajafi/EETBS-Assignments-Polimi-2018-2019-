#resistences
R1=["R_gap","cond",0.01,0.026,1.2]
R2=["R_glass1","cond",0.004,0.78,1.2]
R2s=["R_glass2","cond",0.004,0.78,1.2]
R3=["R_conv1","conv",10,1.2]
R4=["R_conv2","conv",40,1.2]
#gap
L1=R1[2]
K1=R1[3]
A1=R1[-1]
#glass1
L2=R2[2]
K2=R2[3]
A2=R2[-1]
#glass2
L2s=R2s[2]
K2s=R2s[3]
A2s=R2s[-1]
#inside
h1=R3[2]
A3=R3[-1]
#outside
h2=R4[2]
A4=R3[-1]


#conductive and convective resistences with a cicle
ListOfResistence=[R1,R2,R2s,R3,R4] #list of resistences
R_tot_cond=0
for anyResistence in ListOfResistence:
    if anyResistence[1]=="cond":    #case of conductive resistence
        L=anyResistence[2]
        K=anyResistence[3]
        A=anyResistence[-1]
        print("name:"+anyResistence[0])
        print("tye:"+anyResistence[1])
        print("L:"+str(L))
        print("K:"+str(K))
        print("A:"+str(A))
        R_thisresistence=float(L)/(K*A)
        R_tot_cond=R_tot_cond+R_thisresistence
        anyResistence.append(R_thisresistence)
        print("total Rcond: " +str(R_tot_cond) + " degC/W")
    elif anyResistence[1]=="conv":   #case of convective resistence
        #convective resistence inside
        resistence_inside=1/(h1*A3)
        #convective resistence outside
        resistence_outside=1/(h2*A4)
        total_R_conv=resistence_inside+resistence_outside
        print("total Rconv: " +str(total_R_conv) + " degC/W")
    else :
            print("error")  #not cond or conv
            
        
  
print("*************")
totalR=R_tot_cond+total_R_conv
print("total R: " +str(R_tot_cond+total_R_conv) + " degC/W")
 
T_inf1=20 #inner temperature in C
T_inf2=-10 #outer temperature      
Q=(T_inf1-T_inf2)/totalR
T1=T_inf1-Q*resistence_inside
