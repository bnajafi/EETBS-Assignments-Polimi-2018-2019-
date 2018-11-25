#Assignment 7
import os
import numpy as np
import pandas as pd

import scipy as sp # You need to import Scipy in order to interpolate

Folder_WhereIwas= os.getcwd()
Folder_whereThoseTablesAre = r"C:\Users\Famiglia\Documents\Manuel\Polimi\MAGISTRALE\PRIMO ANNO\Primo semestre\Bezhad\Python4ScientificComputing_Fundamentals\A 2018-2019\Tables"

name_file_windows = "windows.csv"
path_file_windows = os.path.join(Folder_whereThoseTablesAre,name_file_windows)
window_DF = pd.read_csv(path_file_windows, sep=";", index_col = 0, header=0) 
window_DF.to_csv(path_file_windows,sep=";")
        
name_file_modifiedWindows="window_modified.csv"
path_file_modifiedwindows = os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows) 
window_DF.to_csv(path_file_modifiedwindows,sep=";")


Latitude=42

def Ediffuse_finder(row):
    DirectionofWindow=row["Direction"]
    name_file_DiffuseIrradiance="DiffuseIrradiance.csv"
    path_file_DiffuseIrradiance = os.path.join(Folder_whereThoseTablesAre,name_file_DiffuseIrradiance) 
    DiffuseIrradiance_DF = pd.read_csv(path_file_DiffuseIrradiance, sep=";", index_col = 0, header=0) 
    name_of_columns=DiffuseIrradiance_DF.columns.get_values() 
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)   
    DiffuseIrradiance_DF_value=sp.interp(Latitude,name_of_columns_as_numbers,DiffuseIrradiance_DF.loc[DirectionofWindow]) 
    return DiffuseIrradiance_DF_value
    
def EBeam_finder(row):
    DirectionofWindow=row["Direction"]
    name_file_BeamIrradiance="BeamIrradiance.csv"
    path_file_BeamIrradiance = os.path.join(Folder_whereThoseTablesAre,name_file_BeamIrradiance) 
    BeamIrradiance_DF = pd.read_csv(path_file_BeamIrradiance, sep=";", index_col = 0, header=0) 
    name_of_columns=BeamIrradiance_DF.columns.get_values() 
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)   
    BeamIrradiance_DF_value=sp.interp(Latitude,name_of_columns_as_numbers,BeamIrradiance_DF.loc[DirectionofWindow]) 
    return BeamIrradiance_DF_value
    
def SLF_finder(row):
    DirectionofWindow=row["Direction"]
    name_file_SLF="SLF.csv"
    path_file_SLF = os.path.join(Folder_whereThoseTablesAre,name_file_SLF) 
    SLF_DF = pd.read_csv(path_file_SLF, sep=";", index_col = 0, header=0) 
    name_of_columns=SLF_DF.columns.get_values() 
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)   
    SLF_DF_value=sp.interp(Latitude,name_of_columns_as_numbers,SLF_DF.loc[DirectionofWindow]) 
    return SLF_DF_value

window_DF["Ed"]=window_DF.apply(Ediffuse_finder,axis=1)
window_DF["ED"]=window_DF.apply(EBeam_finder,axis=1)
window_DF["SLF"]=window_DF.apply(SLF_finder,axis=1)
window_DF.to_csv(path_file_modifiedwindows,sep=";")


def Fshd_finder(row):
    frac_to_maximize=((row["SLF"]*row["Doh"])-row["Xoh"])/row["Height"]
    maximum=max(0,frac_to_maximize)
    minimum=min(1,maximum)
    return minimum
    
window_DF["Fshd"]=window_DF.apply(Fshd_finder,axis=1)


window_DF["PXI"]= window_DF["Tx"]*(window_DF["Ed"]+window_DF["ED"]*(1-window_DF["Fshd"]))
window_DF.to_csv(path_file_modifiedwindows,sep=";")