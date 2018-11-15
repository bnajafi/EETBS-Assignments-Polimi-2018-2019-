# Guidelines for Assignment 8
import os
import numpy as np
import pandas as pd

import scipy as sp # You need to import Scipy in order to interpolate


        
# You should use the demosntrated prcedure to find and update the PXI of all windows!

# How to interpolate !

# if df_BeamIrradiance is your DataFrame:
#pay attention that you should add a code to create df_BeamIrradiance using read_csv

Latitude=42
name_of_columns=df_BeamIrradiance.columns.get_values()
name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)

# for thedirection of South
ED=sp.interp(Latitude,name_of_columns_as_numbers,df_BeamIrradiance.loc["S"]) # pay attention that you should have scipy imported as sp in the beggining 

# you use the same procedure for the diffuse one 






    