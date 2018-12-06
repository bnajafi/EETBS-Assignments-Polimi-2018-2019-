# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import scipy as sp
import os 

Start=os.getcwd()
Tables=r"C:\Users\LoruPortatile\Desktop\clima 2\Python4ScientificComputing_Fundamentals\A 2018-2019\Tables"
os.chdir(Tables)

DF_Windows=pd.read_csv("windows.csv",sep=";",index_col=0,header=0)

Latitude_piacenza=42

def BeamIrradiance(row):
    name_file="BeamIrradiance.csv"
    name_path=os.path.join(Tables,name_file)
    BeamIrradianceTable=pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0,header=0)
    name_of_columns=BeamIrradianceTable.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED=sp.interp(Latitude_piacenza,name_of_columns_as_numbers,BeamIrradianceTable.loc[row["Direction"]])
    return ED                                                                                   
DF_Windows["ED"]=DF_Windows.apply(BeamIrradiance,axis=1)

def DiffusiveIrradiance(row):
    name_file="Diffuseirradiance.csv"
    path_file=os.path.join(Tables,name_file)
    DiffuseIrradianceTable=pd.read_csv("Diffuseirradiance.csv",sep=";",index_col=0,header=0)
    name_of_columns=DiffuseIrradianceTable.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed=sp.interp(Latitude_piacenza,name_of_columns_as_numbers,DiffuseIrradianceTable.loc[row["Direction"]])
    return Ed
    
DF_Windows["Ed"]=DF_Windows.apply(DiffusiveIrradiance,axis=1)

def ShadeLineFactors(row):
    name_file="SLF.csv"
    path_file=os.path.join(Tables,name_file)
    ShadeLineFactorsTable=pd.read_csv("SLF.csv",sep=";",index_col=0,header=0)
    name_of_columns=ShadeLineFactorsTable.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    SLF=sp.interp(Latitude_piacenza,name_of_columns_as_numbers,ShadeLineFactorsTable.loc[row["Direction"]])    
    return SLF
DF_Windows["SLF"]=DF_Windows.apply(ShadeLineFactors,axis=1)

def Fshd(row):
    SLF=row["SLF"]
    Doh=row["Doh"]
    Xoh=row["Xoh"]
    H=row["Height"]
    a=(SLF*Doh-Xoh)/H
    FshdMax=max(0,a)
    FshdMin=min(1,FshdMax)
    return FshdMin

DF_Windows["Fshd"]=DF_Windows.apply(Fshd,axis=1)
DF_Windows["PXI"]= DF_Windows["Tx"]*(DF_Windows["Ed"]+(1-DF_Windows["Fshd"])*DF_Windows["ED"])

WindowModified="window_modified.csv"
WindowModified_path=os.path.join(Tables,WindowModified) 

# Using a lambda function I convert all the float numbers to string and replace the dot with a comma
DF_Windows.applymap(lambda x: str(x).replace(".", ",") if isinstance(x, float) else x).to_csv(WindowModified_path,sep=";")