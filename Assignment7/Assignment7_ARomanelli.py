import os
import numpy as np
import pandas as pd
import scipy as sp # You need to import Scipy in order to interpolate


Folder_whereThoseTablesAre=r"C:\Users\Alessia\Documents\Primo_anno_en\Building\Python4ScientificComputing_Fundamentals\A 2018-2019\Tables"
os.chdir(Folder_whereThoseTablesAre)  
name_file_modifiedWindows="windows_modified.csv"
path_file_modifiedWindows=os.path.join(Folder_whereThoseTablesAre,name_file_modifiedWindows)
window_DF=pd.read_csv(path_file_modifiedWindows,sep=";",index_col=0)


Latitude=42
window_DF["Area"]= window_DF['width']*window_DF['Height'] 


#I find ED and I put it in window_DF table

def ED_finder_correct(row):
    direction=row["Direction"]
    Latitude=42

    name_file_beamirr="BeamIrradiance.csv"
    path_file_beamirr=os.path.join(Folder_whereThoseTablesAre,name_file_beamirr)
    Beamirr_DF=pd.read_csv(path_file_beamirr,sep=";",index_col=0,header=0)
    name_of_columns_b=Beamirr_DF.columns.get_values()
    name_of_columns_as_numbers_b = name_of_columns_b.astype(np.int32, copy=False)
    ED_value=sp.interp(Latitude,name_of_columns_as_numbers_b,Beamirr_DF.loc[direction])
    
    return ED_value
    

window_DF["ED"]=window_DF.apply(ED_finder_correct,axis=1)


#I find Ed and I put it in window_DF table

def Ed_finder_correct(row):
    direction=row["Direction"]
    Latitude=42

    name_file_diffirr="DiffuseIrradiance.csv"
    path_file_diffirr=os.path.join(Folder_whereThoseTablesAre,name_file_diffirr)
    Diffirrr_DF=pd.read_csv(path_file_diffirr,sep=";",index_col=0,header=0)
    name_of_columns=Diffirrr_DF.columns.get_values()
    name_of_columns_as_numbers = name_of_columns.astype(np.int32, copy=False)
    Ed_value=sp.interp(Latitude,name_of_columns_as_numbers,Diffirrr_DF.loc[direction])
    
    return Ed_value
    

window_DF["Ed"]=window_DF.apply(Ed_finder_correct,axis=1)



#I find SLF and I put it in window_DF table

def SLF_finder_correct(row):
    direction=row["Direction"]
    Latitude=42

    name_file_SLF="SLF.csv"
    path_file_SLF=os.path.join(Folder_whereThoseTablesAre,name_file_SLF)
    SLF_DF=pd.read_csv(path_file_SLF,sep=";",index_col=0,header=0)
    name_of_columns_slf=SLF_DF.columns.get_values()
    name_of_columns_as_numbers_slf = name_of_columns_slf.astype(np.int32, copy=False)
    SLF_value=sp.interp(Latitude,name_of_columns_as_numbers_slf,SLF_DF.loc[direction])
    
    return SLF_value

window_DF["SLF"]=window_DF.apply(SLF_finder_correct,axis=1)

window_DF.to_csv(path_file_modifiedWindows,sep=";")

#I find IAC and IAC_cl and I put it in window_DF table

def IAC_CL_finder_correct(row):
    windowID=row["Window_ID"]
    intShadingID=row["IntShading_ID"]
    name_file_IAC_Cl="IAC_Cl.csv"
    path_file_IAC_Cl=os.path.join(Folder_whereThoseTablesAre,name_file_IAC_Cl)
    IAC_Cl_DF=pd.read_csv(path_file_IAC_Cl,sep=";",index_col=1,header=0)
    IAC_Cl_value=IAC_Cl_DF.loc[windowID,intShadingID]   
    return IAC_Cl_value

window_DF["IAC_cl"]=window_DF.apply(IAC_CL_finder_correct,axis=1)

window_DF["IAC"]=  1.0+(window_DF["IAC_cl"]-1.0)*window_DF["IntShading_closeness"]


#I find Fshd and I put it in window_DF table


Fshd_value= ((window_DF["SLF"] *window_DF["Doh"])-window_DF["Xoh"])/window_DF["Height"]

window_DF["Fshd"]=Fshd_value
window_DF["Fshd"][window_DF["Fshd"]<0]=0
window_DF["Fshd"][window_DF["Fshd"]>1]=1

#I find PXI and I put it in window_DF table

window_DF["PXI"]=window_DF["Tx"]*((window_DF["Ed"]+(1-window_DF["Fshd"])*window_DF["ED"]))

#Save the found values in excel table
window_DF.to_csv(path_file_modifiedWindows,sep=";")



    