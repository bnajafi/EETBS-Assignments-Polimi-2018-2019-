import pandas as pd
import scipy as sp
import numpy as np
import os
folder_wherethetablesare= r"C:\Users\Gilberto\Desktop\poli\Energy building systems\Python4ScientificComputing_Fundamentals\A 2018-2019\Tables"
name_file_windows = "windows.csv"
path_file_windows = os.path.join(folder_wherethetablesare,name_file_windows)
window_DF= pd.read_csv(path_file_windows, sep=";", index_col=0) 
name_file_mod= "Windows_modified.csv"
path_file_windowsmod = os.path.join(folder_wherethetablesare,name_file_mod)

window_DF.index
window_DF.columns

latitude = 42

def IAC_CL_finder_correct(row):

    WindowID=row["Window_ID"]
    IntshadingID=row["IntShading_ID"]
    name_file_IAC_Cl = "IAC_cl.csv"
    path_file_IAC_Cl = os.path.join(folder_wherethetablesare,name_file_IAC_Cl)
    IAC_cl_DF= pd.read_csv(path_file_IAC_Cl, sep=";", index_col=1, header=0) 
    IAC_cl_DF_value=IAC_cl_DF.loc[WindowID,IntshadingID]

    return(IAC_cl_DF_value)

WindowsRow=window_DF.loc["east",:]

window_DF["IAC_cl"]=window_DF.apply(IAC_CL_finder_correct, axis=1)
window_DF["IAC"]=1.0+(window_DF["IAC_cl"]-1.0)*window_DF["IntShading_closeness"]

window_DF.to_csv(path_file_windowsmod, sep=";")

#Definition of the function for SLF
def SLF_finder_correct(row):

    direction=row["Direction"]
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(folder_wherethetablesare,name_file_SLF)
    SLF_DF= pd.read_csv(path_file_SLF, sep=";", index_col=0, header=0)  
    name_of_columns_SLF=SLF_DF.columns.get_values()
    name_of_columns_as_numbers_SLF = name_of_columns_SLF.astype(np.int32, copy=False)
    SLF=sp.interp(latitude,name_of_columns_as_numbers_SLF,SLF_DF.loc[direction])

    return(SLF)
    

window_DF["SLF"]=window_DF.apply(SLF_finder_correct, axis=1)
window_DF.to_csv(path_file_windowsmod, sep=";")


#F_shd

fshd=(window_DF["SLF"]*window_DF["Doh"]-window_DF["Xoh"])/window_DF["Height"]
fshd.loc["south-Fixed"]=1.0
fshd.loc["south-Operable"]=1.0
window_DF["Fshd"]=fshd
window_DF.to_csv(path_file_windowsmod, sep=";")

#Beam irradiance:

def Beam_finder_correct(row_Beam):

    direction=row_Beam["Direction"]
    name_file_Beam = "BeamIrradiance.csv"
    path_file_Beam = os.path.join(folder_wherethetablesare,name_file_Beam)
    Beam_DF= pd.read_csv(path_file_Beam, sep=";", index_col=0, header=0)  
    name_of_columns_Beam=Beam_DF.columns.get_values()
    name_of_columns_as_numbers_Beam = name_of_columns_Beam.astype(np.int32, copy=False)
    Beam=sp.interp(latitude,name_of_columns_as_numbers_Beam,Beam_DF.loc[direction]) 

    return(Beam)
    
window_DF["ED"]=window_DF.apply(Beam_finder_correct, axis=1)
window_DF.to_csv(path_file_windowsmod, sep=";")


#Diffuse irradiance:

def Diffuse_finder_correct(row_Diffuse):

    direction=row_Diffuse["Direction"]
    name_file_Diffuse = "DiffuseIrradiance.csv"
    path_file_Diffuse = os.path.join(folder_wherethetablesare,name_file_Diffuse)
    Diffuse_DF= pd.read_csv(path_file_Diffuse, sep=";", index_col=0, header=0)  
    name_of_columns_Diffuse=Diffuse_DF.columns.get_values()
    name_of_columns_as_numbers_Diffuse = name_of_columns_Diffuse.astype(np.int32, copy=False)
    Diffuse=sp.interp(latitude,name_of_columns_as_numbers_Diffuse,Diffuse_DF.loc[direction])

    return(Diffuse)
    
window_DF["Ed"]=window_DF.apply(Diffuse_finder_correct, axis=1)
window_DF.to_csv(path_file_windowsmod, sep=";")

#PXI Calculation


window_DF["PXI"]=window_DF["Tx"]*(window_DF["Ed"]+(1-window_DF["Fshd"])*window_DF["ED"])
window_DF.to_csv(path_file_windowsmod, sep=";")