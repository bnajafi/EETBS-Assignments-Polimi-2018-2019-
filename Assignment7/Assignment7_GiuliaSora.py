import pandas as pd
import numpy as np
import scipy as sp

import os 
WhereIamAtTheStart=os.getcwd()
FolderInWhichTheTablesAre=r"C:\Users\Giulia\Documents\Pyton\Tables"
os.chdir(FolderInWhichTheTablesAre)

Window_DF=pd.read_csv("windows.csv",sep=";",index_col=0,header=0)
Latitude=42
def BeamIrradiance(row):#for latitude=42
    Latitude=42
    name_file="BeamIrradiance.csv"
    name_path=os.path.join(FolderInWhichTheTablesAre,name_file)
    BeamIrradianceTable=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0,header=0)
    name_of_columns=BeamIrradianceTable.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED=sp.interp(Latitude,name_of_columns_as_numbers,BeamIrradianceTable.loc[row["Direction"]])  
    return ED                                                                                   
Window_DF["ED"]=Window_DF.apply(BeamIrradiance,axis=1)

def DiffusiveIrradiance(row): #for latitude=42
    Latitude=42
    name_file="Diffuseirradiance.csv"
    path_file=os.path.join(FolderInWhichTheTablesAre,name_file)
    DiffuseIrradianceTable=pd.read_csv("Diffuseirradiance.csv",sep=";",index_col=0,header=0)
    name_of_columns=DiffuseIrradianceTable.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed=sp.interp(Latitude,name_of_columns_as_numbers,DiffuseIrradianceTable.loc[row["Direction"]])
    return Ed
Window_DF["Ed"]=Window_DF.apply(DiffusiveIrradiance,axis=1)

def ShadeLineFactors(row):
    Latitude=42
    name_file="SLF.csv"
    path_file=os.path.join(FolderInWhichTheTablesAre,name_file)
    ShadeLineFactorsTable=pd.read_csv("SLF.csv",sep=";",index_col=0,header=0)
    name_of_columns=ShadeLineFactorsTable.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    SLF=sp.interp(Latitude,name_of_columns_as_numbers,ShadeLineFactorsTable.loc[row["Direction"]])    
    return SLF
Window_DF["SLF"]=Window_DF.apply(ShadeLineFactors,axis=1)

def Fshd(row):
    SLF=row["SLF"]
    Doh=row["Doh"]
    Xoh=row["Xoh"]
    H=row["Height"]
    a=(SLF*Doh-Xoh)/H
    FshdMax=max(0,a)
    FshdMin=min(1,FshdMax)
    return FshdMin

Window_DF["Fshd"]=Window_DF.apply(Fshd,axis=1)

Window_DF["PXI"]=Window_DF["Tx"]*(Window_DF["Ed"]+(1-Window_DF["Fshd"])*Window_DF["ED"])

WindowModified="window_modified.csv"
WindowModified_path=os.path.join(FolderInWhichTheTablesAre,WindowModified) 
Window_DF.to_csv(WindowModified_path,sep=";")