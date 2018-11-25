#Assignment 7

import pandas as pd
import scipy as sp
import numpy as np
import os

Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\My\Desktop\data"
os.chdir(Folder_whereThoseTablesAre)
window_DF = pd.read_csv("windows.csv", sep=";", index_col = 0, header=0) 
os.chdir(Folder_WhereIwas)

name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows) 
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0) 
name_file_modifiedWindows="window_modified.csv"
path_file_modifiedwindows = os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows) 
window_DF.to_csv(path_file_modifiedwindows,sep=";") 

#piacenza
latitude=45

location_deltaT_cooling = 7.9 
location_deltaT_heating = 24.9 
location_DR_cooling= 11.9

C_Value = location_deltaT_cooling - 0.46*location_DR_cooling
window_DF["C_value"]= C_Value

name_file_IAC_Cl="IAC_cl.csv"
path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
IAC_cl_DF.head(3)
IAC_cl_DF.loc["1c","BlindsDark"]



def IAC_CL_finder(windowID,intShadingID):  
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    IAC_cl_value = IAC_cl_DF.loc[windowID,intShadingID]
    return IAC_cl_value

IAC_CL_finder("1c","BlindsDark")  

def IAC_CL_finder_correct(row):
    windowID = row["Window_ID"]
    intShadingID = row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl) 
    IAC_cl_DF = pd.read_csv(path_file_IAC_Cl, sep=";", index_col = 1, header=0) 
    IAC_cl_value = IAC_cl_DF.loc[windowID,intShadingID]
    return IAC_cl_value

thisWindowRow= window_DF.loc["east",:]

IAC_CL_finder_correct(thisWindowRow)

window_DF["IAC_cl"]=window_DF.apply(IAC_CL_finder_correct,axis=1)
window_DF["IAC"]=  1.0+(window_DF["IAC_cl"]-1.0)*window_DF["IntShading_closeness"]
window_DF.to_csv(path_file_modifiedwindows,sep=";") 

def SLF_finder(row):
    direction = row["Direction"]
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF)
    SLF_DF = pd.read_csv(path_file_SLF, sep = ";", index_col = 0, header = 0)
    nameOfCloumns = SLF_DF.columns.get_values()
    nameOfColumnsNumbers = nameOfCloumns.astype(np.int32, copy=False)
    SLF_Value = sp.interp(latitude,nameOfColumnsNumbers,SLF_DF.loc[direction])
    return SLF_Value
    
window_DF["SLF"] = window_DF.apply(SLF_finder,axis=1)


def Ed_finder(row):
    direction = row["Direction"]
    name_file_Ed = "DiffuseIrradiance.csv"
    path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed)
    Ed_DF = pd.read_csv(path_file_Ed, sep = ";", index_col = 0, header = 0)
    nameOfCloumns = Ed_DF.columns.get_values()
    nameOfColumnsNumbers = nameOfCloumns.astype(np.int32, copy=False)
    Ed_Value = sp.interp(latitude,nameOfColumnsNumbers,Ed_DF.loc[direction])
    return Ed_Value                

window_DF["Ed"] = window_DF.apply(Ed_finder,axis=1)

def ED_finder(row):
    direction = row["Direction"]
    name_file_ED = "BeamIrradiance.csv"
    path_file_ED = os.path.join(Folder_whereThoseTablesAre,name_file_ED)
    ED_DF = pd.read_csv(path_file_ED, sep = ";", index_col = 0, header = 0)
    nameOfCloumns = ED_DF.columns.get_values()
    nameOfColumnsNumbers = nameOfCloumns.astype(np.int32, copy=False)
    ED_Value = sp.interp(latitude,nameOfColumnsNumbers,ED_DF.loc[direction])    
    return ED_Value         

window_DF["ED"] = window_DF.apply(ED_finder,axis=1)
window_DF["Fshd"] = (window_DF["SLF"]*window_DF["Doh"] - window_DF["Xoh"])/window_DF["Height"]               
window_DF["Fshd"][(window_DF["Fshd"] < 0.0 )]  = 0.0
window_DF["Fshd"][(window_DF["Fshd"] > 1.0 )]  = 1.0
window_DF["PXI"] = window_DF["Tx"]*(window_DF["Ed"] + (1-window_DF["Fshd"])*window_DF["ED"])                                                      
window_DF.to_csv(path_file_modifiedwindows, sep = ";")
print (window_DF["PXI"]) 






