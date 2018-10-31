import numpy as np
#the main use of numpy is create array
A1=np.array([1,4,5,11]) #array of integer
A2=np.array([1.2,5.0,9.3,5])
A1.dtype
A2.dtype
#All the elements of an array should have integer numbers
#if they don't numpy will convert them
A3=np.array(["marco","mirco","sara"])
#the type of all the elements is string with 5 characters
A4=np.array([True,False,False,True])
A5=np.array([1,"Manuel",4.5])
#It converts everything in strings

#This is definitely a disadvantage because it will convert it in strings every thing, it will be a mess!
#We can't use different type, the advantage is that we can do vectorial operations
L6=[1.4,5.3,7.6]
#A6=np.array()
A6=np.array(L6)
L7=[2.2,3-0,9.5]
A7=np.array(L7)
A8=A6+A7 #
#this does vectorial operation
L8=L7+L6

A10=A6*A8
A11=2*A6
L11=2*L6 #we don't want this

#Let's use it to solve our problem
Opaque_item_list=["wall","ceiling","door"]
Opaque_item_array=np.array(Opaque_item_list)
Opaque_U_list=[0.438,0.25,1.78]
Opaque_U_array=np.array(Opaque_U_list)
Opaque_area_array=([105.8,200,2.2])

T_inside_heating=20
T_outside_heating=-4.8
DeltaT_Heating=T_inside_heating-T_outside_heating
opaque_HF_array=DeltaT_Heating*Opaque_U_array
Opaque_Q_array=opaque_HF_array*Opaque_area_array
Opaque_Q_array[0]
Opaque_Q_array[0:2]
Opaque_Q_array[-1]
Opaque_Q_array[-1]=0 #You can assign values
 

#Logical arrays to avoid using "for"
TheOneMoreThan1000=Opaque_Q_array>1000 #Checking conditions on al off them at the same time
A12=np.array([3,5,7,11])
A13=A12>5
A14=A12<=5
Opaque_item_array=="wall"
A12[A14] #Python discomprehension, show the true one but not the false one
Opaque_Q_array[Opaque_item_array=="wall"]
#Opaque_Q_array[Opaque_item_array=="wall" | Opaque_item_array=="ceiling"] #it doesn t work
index_wall=Opaque_item_array=="wall"

index_ceiling=Opaque_item_array=="ceiling"
index_wallorceing=index_wall | index_ceiling #OR 
Opaque_Q_array[index_wallorceing]
Opaque_wallOrCeiling_value=Opaque_Q_array[index_wallorceing].sum() #Making a summation
AverageOfAll_opaqueHeating=Opaque_Q_array.mean()

#Let's use this approach to solve the resistance problem
Ri=["R_internal","conv",8.9,15]
R1=["R_foam","cond",0.06,0.05,15]
R2=["R_wood","cond",0.1,0.4,15]
R3=["R_plaster","cond",0.01,1,15]
Ro=["R_external","conv",20,15]
resistance_name=np.array(["R_internal","R_foam","R_wood","R_plaster","R_external"])
resistance_types=np.array(["conv","cond","cond","cond","conv"])
resistance_k=np.array([None,0.05,0.4,1,None])
resistance_L=np.array([None,0.06,0.1,0.01,None])
resistance_A=np.array([15,15,15,15,15])
resistance_h=np.array([8.9,None,None,None,20])

resistance_RValues=np.array(np.zeros(5))
resistance_RValues[resistance_types=="cond"]=resistance_L[resistance_types=="cond"]/resistance_k[resistance_types=="cond"]/resistance_A[resistance_types=="cond"]
resistance_RValues[resistance_types=="conv"]=1.0/resistance_h[resistance_types=="conv"]/resistance_A[resistance_types=="conv"]
Rtot=resistance_RValues.sum()    #WE CAN T DO IF AND FOR in the next assignment without the air gap 
#far git pull per aggiornare ed avere la consegna dell esercizio