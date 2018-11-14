import numpy as np
import pandas as pd


#what we call an 1D array in numpy in pandas it s called serie
S1 = pd.Series([1,2,3,4])   #Every item has an index and it is written. That's usefull because so we can give index
S2 = pd.Series([4,5,6,0.1])    #If just one element is of float type, pandas converts all the other too
S3 = S1+S2
S4 = S1-S2
S5 = S1 > S2
S2[S2>5]                    #Boolean series and then application oof this to the series
S6 = pd.Series([1,3,6,9],["a","b","c","d"])
S7 = pd.Series([4,5,7,9],["d","b","c","a"])
S8 = S6+S7              #It does the same on the names, we don t need to remember the order
Q_heating= pd.Series([1150,1240,124],index=["Wall","Ceiling","Door"])
Q_heating["Door"]

#One useful function
Q_heating.argmax()#arg gives the mane of the maximum

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

Q_heating = pd.Series(Opaque_Q_array,index=Opaque_item_list)
Q_heating["wall"] 
#using Apply and functions
def toKw(inputValue):
    outputValue = inputValue/1000
    return outputValue
    
Q_heating_kW = Q_heating.apply(toKw)    #We can apply a function to a column. We can avoid the for


#Let's see how define 2D matrix:
resistance_names=["R1","R2","R3","R4","R5"]
resistance_types=["conv","cond","cond","cond","conv"]
resistance_h=[10,None,None,None,25]
resistance_k=[None,0.8,1.5,0.05,None]
resistance_L=[None,0.5,0.3,0.6,None]
resistance_RValues=[0,0,0,0,0]
resistance_ListOfResistance = [resistance_types,resistance_h,resistance_k,resistance_L,resistance_RValues]
resistance_DataFrame=pd.DataFrame(resistance_ListOfResistance,index=["Types","h","k","L","R"],columns=resistance_names)    #list of a list I want the columns to be the resistance and the rows the items

#How to extract data froma DataFrame
resistance_DataFrame.iloc[0,1]     #i=number loc=ocation    [row,column]
resistance_DataFrame.iloc[:,1] 
resistance_DataFrame.iloc[0] 
resistance_DataFrame.iloc[-1,:] 

#Second way of extraction using names
#Either you shouldn't use anything(columns) or 
resistance_DataFrame["R3"]
resistance_DataFrame.loc["Types","R1"]            #Gli indici non sono conteggiati nel numero di colonne/righe
resistance_DataFrame.loc["k","R4"]
resistance_DataFrame.loc["R"]=1                   #I can assign or update in this way, the same with which i extract
resistance_DataFrame.loc["R"][resistance_DataFrame.loc["Types"]=="conv"]=1.0/resistance_DataFrame.loc["h"][resistance_DataFrame.loc["Types"]=="conv"]
#do the same with the other

