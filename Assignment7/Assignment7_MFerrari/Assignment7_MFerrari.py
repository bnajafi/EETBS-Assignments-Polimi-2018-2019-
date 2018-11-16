#In this assignment I'm going to evaluate the PXI for all the windows reported in the Excel file "windows_mod".
import numpy as np
import pandas as pd
import os
import sys
import scipy as sp
#In this way you should be able to see where also the Excel files I'm using are. Use RUN for this time.
thisFileDirectory = os.path.dirname(sys.argv[0])
os.chdir(thisFileDirectory)
print os.getcwd()

window_DF = pd.read_csv("windows_mod.csv", sep = ";", index_col = 0, header = 0) 
name_file_windows_mod = "windows_mod.csv"
path_file_windows_mod =os.path.join(thisFileDirectory,name_file_windows_mod)
#For Piacenza I use latitude equal to 45, but since I'll use interpolation instruments, you can use any value for the latitude.
latitude = 45

def Ed_finder(row):
    """This function reads ( or evaluates, for latitude values different from tabulated ones ) and returns 
    the value of the diffuse irradiance for a certain input window."""
    direction = row["Direction"]
    name_file_Ed = "DiffuseIrradiance.csv"
    path_file_Ed = os.path.join(thisFileDirectory,name_file_Ed)
    Ed_DF = pd.read_csv(path_file_Ed, sep = ";", index_col = 0, header = 0)
    name_of_columns = Ed_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed_Value = sp.interp(latitude,name_of_columns_as_numbers,Ed_DF.loc[direction])
    return Ed_Value                
#I'm applying the function to all the row of the data frame.
window_DF["Ed"] = window_DF.apply(Ed_finder,axis=1)

def ED_finder(row):
    """This function reads ( or evaluates, for latitude values different from tabulated ones ) and returns 
    the value of the beam irradiance for a certain input window."""
    direction = row["Direction"]
    name_file_ED = "BeamIrradiance.csv"
    path_file_ED = os.path.join(thisFileDirectory,name_file_ED)
    ED_DF = pd.read_csv(path_file_ED, sep = ";", index_col = 0, header = 0)
    name_of_columns = ED_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    ED_Value = sp.interp(latitude,name_of_columns_as_numbers,ED_DF.loc[direction])    
    return ED_Value         
#I'm applying the function to all the row of the data frame.
window_DF["ED"] = window_DF.apply(ED_finder,axis=1)

def SLF_finder(row):
    """This function reads ( or evaluates, for latitude values different from tabulated ones ) and returns 
    the value of SLF for a certain input window."""
    direction = row["Direction"]
    name_file_SLF = "SLF.csv"
    path_file_SLF = os.path.join(thisFileDirectory,name_file_SLF)
    SLF_DF = pd.read_csv(path_file_SLF, sep = ";", index_col = 0, header = 0)
    name_of_columns = SLF_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    SLF_Value = sp.interp(latitude,name_of_columns_as_numbers,SLF_DF.loc[direction])
    return SLF_Value                

#I'm applying the function to all the row of the data frame.
window_DF["SLF"] = window_DF.apply(SLF_finder,axis=1)
#I'm calculating the shadow factors for all the windows.
window_DF["Fshd"] = (window_DF["SLF"]*window_DF["Doh"] - window_DF["Xoh"])/window_DF["Height"]               
#I've to impose that Fshd value is beetween 0 and 1, both included.
window_DF["Fshd"][(window_DF["Fshd"] < 0.0 )]  = 0.0
window_DF["Fshd"][(window_DF["Fshd"] > 1.0 )]  = 1.0
#I'm calculating the PXI for all the windows.
window_DF["PXI"] = window_DF["Tx"]*(window_DF["Ed"] + (1-window_DF["Fshd"])*window_DF["ED"])                                                      
#I'm updating the Excel file "windows_mod" with the calculations I've done since now.
window_DF.to_csv(path_file_windows_mod, sep = ";")
#I'm printing the results.
print (window_DF["PXI"])