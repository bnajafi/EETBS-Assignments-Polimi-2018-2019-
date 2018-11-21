#ASSIGNMENT 7: Calculate and update the PXI of all the windows
import os
import numpy as np
import pandas as pd
import scipy as sp

Folder_WhereThoseTablesAre = r"C:\Users\media\Documents\1 Master POLIMI\Building Systems\forkedRepoAssignment\Python4ScientificComputing_Fundamentals\A 2018-2019\Tables"
os.chdir(Folder_WhereThoseTablesAre)

name_file_windows="windows.csv"
path_file_windows=os.path.join(Folder_WhereThoseTablesAre,name_file_windows)
windows=pd.read_csv(path_file_windows,sep=";",index_col=0,header=0)

Latitude=44.92

#First step: we interpolate and obtain the SLF factor of each window

def SLF_finder(row):
    Direction=row["Direction"]
    name_file_SLF="SLF.csv"
    path_file_SLF=os.path.join(Folder_WhereThoseTablesAre,name_file_SLF)
    SLF_DF=pd.read_csv(path_file_SLF,sep=";",index_col=0,header=0)  
    name_of_columns_SLF=SLF_DF.columns.get_values()
    name_of_columns_as_numbers_SLF=name_of_columns_SLF.astype(np.int32, copy=False)
    SLF=sp.interp(Latitude,name_of_columns_as_numbers_SLF,SLF_DF.loc[Direction])
    return(SLF)
    
windows["SLF"]=windows.apply(SLF_finder,axis=1)
windows.to_csv(path_file_windows, sep=";")



#Second step: we calculate Fshd factor of each window

name_file_windows="windows.csv"
path_file_windows=os.path.join(Folder_WhereThoseTablesAre,name_file_windows)
windows=pd.read_csv(path_file_windows,sep=";",index_col=0,header=0)

    #For South (fixed and operable)
Fshd_S=min(1,max(0,((windows.loc["south-Fixed","SLF"]*windows.loc["south-Fixed","Doh"]-windows.loc["south-Fixed","Xoh"])/windows.loc["south-Fixed","Height"])))
    #For East
Fshd_E=min(1,max(0,((windows.loc["east","SLF"]*windows.loc["east","Doh"]-windows.loc["east","Xoh"])/windows.loc["east","Height"])))
    #For West
Fshd_W=min(1,max(0,((windows.loc["west","SLF"]*windows.loc["west","Doh"]-windows.loc["west","Xoh"])/windows.loc["west","Height"])))

windows["Fshd"]=[Fshd_E,Fshd_W,Fshd_S,Fshd_S]
windows.to_csv(path_file_windows,sep=";")



#Third step: we interpolate and obtain the Ed factor of each window

def Ed_finder(row):
    Direction=row["Direction"]
    name_file_DiffuseIrradiance="DiffuseIrradiance.csv"
    path_file_DiffuseIrradiance=os.path.join(Folder_WhereThoseTablesAre,name_file_DiffuseIrradiance)
    DiffuseIrradiance=pd.read_csv(path_file_DiffuseIrradiance,sep=";",index_col=0,header=0)
    name_of_columns=DiffuseIrradiance.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed=sp.interp(Latitude,name_of_columns_as_numbers,DiffuseIrradiance.loc[Direction])
    return(Ed)
    
windows["Ed"]=windows.apply(Ed_finder,axis=1)
windows.to_csv(path_file_windows, sep=";")



#Forth step: we interpolate and obtain the ED factor of each window

def ED_finder(row):
    Direction=row["Direction"]
    name_file_BeamIrradiance="BeamIrradiance.csv"
    path_file_BeamIrradiance=os.path.join(Folder_WhereThoseTablesAre,name_file_BeamIrradiance)
    BeamIrradiance=pd.read_csv(path_file_BeamIrradiance,sep=";",index_col=0,header=0)
    name_of_columns=BeamIrradiance.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED=sp.interp(Latitude,name_of_columns_as_numbers,BeamIrradiance.loc[Direction])
    return(ED)
    
windows["ED"]=windows.apply(ED_finder,axis=1)
windows.to_csv(path_file_windows, sep=";")



#Final step: we calculate PXI factor of each window

name_file_windows="windows.csv"
path_file_windows=os.path.join(Folder_WhereThoseTablesAre,name_file_windows)
windows=pd.read_csv(path_file_windows,sep=";",index_col=0,header=0)

    #For South (fixed)
PXI_S_fix=windows.loc["south-Fixed","Tx"]*(windows.loc["south-Fixed","Ed"]+(1-Fshd_S)*windows.loc["south-Fixed","ED"])
    #For South (operable)
PXI_S_oper=windows.loc["south-Operable","Tx"]*(windows.loc["south-Operable","Ed"]+(1-Fshd_S)*windows.loc["south-Operable","ED"])
    #For East
PXI_E=windows.loc["east","Tx"]*(windows.loc["east","Ed"]+(1-Fshd_E)*windows.loc["east","ED"])
    #For West
PXI_W=windows.loc["west","Tx"]*(windows.loc["west","Ed"]+(1-Fshd_W)*windows.loc["west","ED"])

windows["PXI"]=[PXI_E,PXI_W,PXI_S_fix,PXI_S_oper]
windows.to_csv(path_file_windows,sep=";")