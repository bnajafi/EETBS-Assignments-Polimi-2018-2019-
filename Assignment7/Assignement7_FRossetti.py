# -*- coding: utf-8 -*-
import pandas as pd
import scipy as sp
import numpy as np
#first method
import os
os.chdir("/Users/federicarossetti/Documents/Python4ScientificComputing_Fundamentals/A 2018-2019/Tables")

Folder_whereThoseTablesAre="/Users/federicarossetti/Documents/Python4ScientificComputing_Fundamentals/A 2018-2019/Tables"

window_DF = pd.read_csv("windows.csv",sep=";", index_col=0, header=0)

name_file_windows="windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows)
window_DF=pd.read_csv(path_file_windows,sep=";",index_col=0)
 
name_file_modified_windows="Window_modified.csv"
path_file_modified_windows = os.path.join(Folder_whereThoseTablesAre,name_file_modified_windows)
window_DF.to_csv(path_file_modified_windows,sep=";") 

latitude =42

name_file_IAC_Cl="IAC_cl.csv" 
path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl)
IAC_Cl_DF=pd.read_csv(path_file_IAC_Cl, sep=";", index_col=1, header=0)

def IAC_CL_finder(row):
    windowID=row["Window_ID"]
    IntShading_ID=row["IntShading_ID"]
    name_file_IAC_Cl="IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl)
    IAC_Cl_DF=pd.read_csv(path_file_IAC_Cl, sep=";", index_col=1, header=0)
    IAC_Cl_DF_value=IAC_Cl_DF.loc[windowID,IntShading_ID]
    return IAC_Cl_DF_value
    
window_DF["IAC_cl"]=window_DF.apply(IAC_CL_finder, axis=1)
window_DF["IAC"]=  1.0+(window_DF["IAC_cl"]-1.0)*window_DF["IntShading_closeness"]

name_file_Ed="DiffuseIrradiance.csv" 
path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed) 
Ed_DF=pd.read_csv(path_file_Ed, sep=";", index_col=0, header=0) 

def Ed_finder(row):
    Directions=row["Direction"]
    name_file_Ed="DiffuseIrradiance.csv" 
    path_file_Ed = os.path.join(Folder_whereThoseTablesAre,name_file_Ed) 
    Ed_DF=pd.read_csv(path_file_Ed, sep=";", index_col=0, header=0) 
    name_of_columns=Ed_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed=sp.interp(latitude,name_of_columns_as_numbers,Ed_DF.loc[Directions])
    return Ed

window_DF["Ed"]=window_DF.apply(Ed_finder, axis=1)

name_file_ED="BeamIrradiance.csv" 
path_file_ED = os.path.join(Folder_whereThoseTablesAre,name_file_ED) 
ED_DF=pd.read_csv(path_file_ED, sep=";", index_col=0, header=0) 

def ED_finder(row):
    Directions=row["Direction"]
    name_file_ED="BeamIrradiance.csv" 
    path_file_ED = os.path.join(Folder_whereThoseTablesAre,name_file_ED) 
    ED_DF=pd.read_csv(path_file_ED, sep=";", index_col=0, header=0) 
    name_of_columns=ED_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED=sp.interp(latitude,name_of_columns_as_numbers,ED_DF.loc[Directions])
    return ED

window_DF["ED"]=window_DF.apply(ED_finder, axis=1)

name_file_SLF="SLF.csv" 
path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
SLF_DF=pd.read_csv(path_file_SLF, sep=";", index_col=0, header=0) 

def SLF_finder(row):
    Directions=row["Direction"]
    name_file_SLF="SLF.csv" 
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
    SLF_DF=pd.read_csv(path_file_SLF, sep=";", index_col=0, header=0) 
    name_of_columns=SLF_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    SLF=sp.interp(latitude,name_of_columns_as_numbers,SLF_DF.loc[Directions])
    return SLF

window_DF["SLF"]=window_DF.apply(SLF_finder, axis=1)

window_DF["Fshd"] = (window_DF["SLF"]*window_DF["Doh"]-window_DF["Xoh"])/window_DF["Height"]
window_DF["Fshd"][window_DF["Fshd"]<0] =0
window_DF["Fshd"][window_DF["Fshd"]>1]=1


window_DF["PXI"]= window_DF["Tx"]*(window_DF["Ed"]+(1.0-window_DF["Fshd"])*window_DF["ED"])

window_DF.to_csv(path_file_modified_windows,sep=";") 

