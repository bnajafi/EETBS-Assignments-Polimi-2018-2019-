import pandas as pd
import os
import scipy as sp

os.chdir(r"C:\Users\gelli\Desktop\POLIMI FIRST YEAR\ENERGY AND ENVIRONMENTAL SYSTEM FOR BUILDINGS\Files solved in Python")
Folder_whereIwas=os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\gelli\Desktop\POLIMI FIRST YEAR\ENERGY AND ENVIRONMENTAL SYSTEM FOR BUILDINGS\Files solved in Python\Assignment 7\Doing the assignment"

name_file="windows.csv"
path_file_window= os.path.join(Folder_whereThoseTablesAre, name_file)
window_DF= pd.read_csv(path_file_window, sep= ";", index_col= 0)
window_DF["Area"]= window_DF["width"]* window_DF["Height"]


name_file_modifiedWindows="windows_practicando.csv"
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre, name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep= ";")

# We are using this Data for the location of Piacenza, Italy
latitude= 45
location_deltaT_cooling= 7.9
location_deltaT_heating= 24.9
location_DR_cooling= 11.9

C_Value= location_deltaT_cooling -0.46*(location_DR_cooling)
window_DF["C_value"]= C_Value
window_DF.to_csv(path_file_modifiedWindows, sep= ";")


#Now we are going to calculate IAC_CL_ for every window


def IAC_CL_finder(row):
    
    windowID=row["Window_ID"]
    intShadingID= row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_cl=os.path.join(Folder_whereThoseTablesAre, name_file_IAC_Cl)
    IAC_cl_DF=pd.read_csv(path_file_IAC_cl, sep= ";", index_col= 1, header=0)
    IAC_cl_value=IAC_cl_DF.loc[windowID, intShadingID]
    return IAC_cl_value 


window_DF.apply( IAC_CL_finder, axis=1) 
window_DF["IAC_cl"]=window_DF.apply( IAC_CL_finder, axis=1) 
window_DF.to_csv(path_file_modifiedWindows, sep= ";")
window_DF["IAC"]=1.0 + (window_DF["IAC_cl"]-1.0)*window_DF["IntShading_closeness"]
window_DF.to_csv(path_file_modifiedWindows, sep= ";")

# Until here, We did this in class and now we are going to do the assignment #7

#Lets calculate Diffuse, Beam Irradiance from a table and we are ging to use the interpolation in case the latitude is not in the table.
#In this case the latitude is in the table that is 45, but with this formula we can use a latitude that is not in the table and interpolate the value for the beam and diffuse irradiance
#To calculate those values we are going to use functions and then appply to the document

def Ed(row):
    lat=45
    windowname=row["Direction"]
    name_file_Ed="DiffuseIrradiance.csv"
    path_file_Ed=os.path.join(Folder_whereThoseTablesAre,  name_file_Ed)
    Ed_DF=pd.read_csv(path_file_Ed, sep= ";",index_col=0,header=0)
    name_of_columns=Ed_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed_value=sp.interp(lat,name_of_columns_as_numbers,Ed_DF.loc[windowname])
    return Ed_value 
    

window_DF.apply(Ed, axis=1) 
window_DF["Ed"]=window_DF.apply( Ed, axis=1) 
window_DF.to_csv(path_file_modifiedWindows, sep= ";")

def ED(row):
    lat=45
    windowname=row["Direction"]
    name_file_ED="BeamIrradiance.csv"
    path_file_ED=os.path.join(Folder_whereThoseTablesAre,  name_file_ED)
    ED_DF=pd.read_csv(path_file_ED, sep= ";",index_col=0,header=0)
    name_of_columns=ED_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED_value=sp.interp(lat,name_of_columns_as_numbers,ED_DF.loc[windowname])
    return ED_value 

window_DF.apply(ED, axis=1) 
window_DF["ED"]=window_DF.apply(ED, axis=1) 
window_DF.to_csv(path_file_modifiedWindows, sep= ";")

def SLF(row):
    lat=45
    windowname=row["Direction"]
    name_file_SLF="SLF.csv"
    path_file_SLF=os.path.join(Folder_whereThoseTablesAre,  name_file_SLF)
    SLF_DF=pd.read_csv(path_file_SLF, sep= ";",index_col=0,header=0)
    name_of_columns=SLF_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    SLF_value=sp.interp(lat,name_of_columns_as_numbers,SLF_DF.loc[windowname])
    return SLF_value
    

window_DF.apply(SLF, axis=1) 
window_DF["SLF"]=window_DF.apply(SLF, axis=1) 
window_DF.to_csv(path_file_modifiedWindows, sep= ";") 


def FSHD(row):
    lengthofshade= ((row["SLF"]* row["Doh"]) - row["Xoh"])/ row["Height"]
    maximum=max(0,lengthofshade)
    minimum=min(1,maximum)
    return minimum 
    
        
window_DF.apply(FSHD, axis=1) 
window_DF["Fshd"]=window_DF.apply(FSHD, axis=1) 
window_DF.to_csv(path_file_modifiedWindows, sep= ";") 

window_DF["PXI"]= window_DF["Tx"] * (window_DF["Ed"] + (1- window_DF["Fshd"])* window_DF["ED"])
window_DF.to_csv(path_file_modifiedWindows, sep= ";")

 

