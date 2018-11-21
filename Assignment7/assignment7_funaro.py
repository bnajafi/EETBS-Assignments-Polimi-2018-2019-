#assignment 7
#funaro_eleonora

import os
import pandas as pd
import numpy as np  
import scipy as sp

Folder_WhereIwas=os.getcwd()
Folder_whereThoseTablesAre=r"C:\Users\Nora\Documents\Piacenza\Building systems\Python"
os.chdir(Folder_whereThoseTablesAre) 
name_file_windows="windows.csv"
path_file_windows=os.path.join(Folder_whereThoseTablesAre,name_file_windows)
window_DF=pd.read_csv("windows.csv", sep=";",index_col=0, header=0)

name_file_modifiedWindows="window_modified.csv"
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep=";") 

latitude=42

#diffuse irradiance
def Ed_finder(row): 
    NameWindow=row["Direction"]
    name_file_Ed="DiffuseIrradiance.csv"
    path_file_Ed=os.path.join(Folder_whereThoseTablesAre,name_file_Ed)
    Ed_DF=pd.read_csv(path_file_Ed, sep=";",index_col=0)
    name_of_columns=Ed_DF.columns.get_values() 
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)   
    Ed_value=sp.interp(latitude,name_of_columns_as_numbers,Ed_DF.loc[NameWindow])                                
    return Ed_value

window_DF["Ed"]=window_DF.apply(Ed_finder,axis=1)
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep=";")  

#beam irradiance
def ED_finder(row): 
    NameWindow=row["Direction"]
    name_file_ED="BeamIrradiance.csv"
    path_file_ED=os.path.join(Folder_whereThoseTablesAre,name_file_ED)
    ED_DF=pd.read_csv(path_file_ED, sep=";",index_col=0)               
    name_of_columns=ED_DF.columns.get_values() 
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)   
    ED_value=sp.interp(latitude,name_of_columns_as_numbers,ED_DF.loc[NameWindow])                   
    return ED_value

window_DF["ED"]=window_DF.apply(ED_finder,axis=1)
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep=";") 

#SLF
def SLF_finder(row): 
    NameWindow=row["Direction"]
    name_file_SLF="SLF.csv"
    path_file_SLF=os.path.join(Folder_whereThoseTablesAre,name_file_SLF)
    SLF_DF=pd.read_csv(path_file_SLF, sep=";",index_col=0)               
    name_of_columns=SLF_DF.columns.get_values() 
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)   
    SLF_value=sp.interp(latitude,name_of_columns_as_numbers,SLF_DF.loc[NameWindow])                  
    return SLF_value

window_DF["SLF"]=window_DF.apply(SLF_finder,axis=1)
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep=";") 

def fshd_finder(row):
    fraction=((row["SLF"]*row["Doh"])-row["Xoh"])/row["Height"]
    maximum=max(0,fraction)
    minimum=min(1,maximum)
    return minimum
    
window_DF["Fshd"]=window_DF.apply(fshd_finder,axis=1)

path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep=";")  

window_DF.loc[:,"PXI"]=window_DF.loc[:,"Tx"]*(window_DF.loc[:,"Ed"]+((1-window_DF.loc[:,"Fshd"])*window_DF.loc[:,"ED"]))
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF.to_csv(path_file_modifiedWindows, sep=";")  