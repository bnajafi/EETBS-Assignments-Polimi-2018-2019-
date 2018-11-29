import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Getting the files
ExternalFilesFolder=r"C:\Users\Giulia\Desktop\Gitex\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles"
TemperatureFileName="Austin_weather_2014.csv"
IrradianceFileName="irradiance_2014_gen.csv"
ConsumptionFileName="consumption_5545.csv"
path_ConsumptionFileName=os.path.join(ExternalFilesFolder,ConsumptionFileName)
path_TemperatureFile=os.path.join(ExternalFilesFolder,TemperatureFileName)
path_IrradianceFile=os.path.join(ExternalFilesFolder,IrradianceFileName)

#Opening DataFrame of consumption and changing the index format
DF_consumption=pd.read_csv(path_ConsumptionFileName,sep=",",index_col=0)
PreviousIndex=DF_consumption.index
NewParseIndex=pd.to_datetime(PreviousIndex)
DF_consumption.index=NewParseIndex
DF_consumption.index.dayofweek

#Finding data for a specific period of time
DF_consumption_somedaysinMay=DF_consumption["2014-05-15 00:00:00":"2014-05-30 23:00:00"]

#Finding weather data of the referred period
DF_weather=pd.read_csv(path_TemperatureFile,sep=";",index_col=0)
previousIndex_weather=DF_weather.index
NewIndex_weather=pd.to_datetime(previousIndex_weather)
DF_weather.index=NewIndex_weather

#a new data frame with a list as colomn
DF_Temperature_somedaysinMay=DF_weather[["temperature"]]["2014-05-15 00:00:00":"2014-05-30 23:00:00"]

#temperature in Celsius
def celsius(row):
    FtoCelsius=(row-32)*5/9
    return FtoCelsius
DF_Temperature_celsius=DF_Temperature_somedaysinMay.apply(celsius)

#Reading the Irradiance file
DF_IrradianceSource=pd.read_csv(path_IrradianceFile,sep=";",index_col=1)
PreviousIndex=DF_IrradianceSource.index
NewIndexIrradiance=pd.to_datetime(PreviousIndex)
DF_IrradianceSource.index=NewIndexIrradiance
DF_Irradiance_insomedaysinMay=DF_IrradianceSource[["gen"]]["2014-05-15 00:00:00":"2014-05-30 23:00:00"]

DF_Irradiance_insomedaysinMay["gen"]<0
DF_Irradiance_insomedaysinMay["gen"][DF_Irradiance_insomedaysinMay["gen"]<0]=0
                                             
                                               

DF_joined=DF_consumption.join([DF_Temperature_celsius,DF_Irradiance_insomedaysinMay])
DF_joined.head()
DF_joined_cleaned=DF_joined.dropna()
DF_joined_cleaned_insomedaysinMay=DF_joined_cleaned["2014-05-15 00:00:00":"2014-05-30 23:00:00"]

plt.subplot(3,1,1)
plt.plot(DF_consumption_somedaysinMay)
plt.xlabel("Time")
plt.ylabel("AC Power(W)")

plt.subplot(3,1,2)
plt.plot(DF_Temperature_celsius)
plt.xlabel("Time")
plt.ylabel("Temperature")

plt.subplot(3,1,3)
plt.plot(DF_Irradiance_insomedaysinMay)
plt.xlabel("data")
plt.ylabel("Generation-->Irradiance")

#changing the scale
temp_max=DF_joined_cleaned["temperature"].min()
temp_min=DF_joined_cleaned["temperature"].max()
DF_joined_cleaned["Temperature Normalized"]=(DF_joined_cleaned["temperature"]-temp_min)/(temp_max-temp_min)

DF_joined_cleaned.head(4)

air_conditioner_5545_min=DF_joined_cleaned["air conditioner_5545"].min()
air_conditioner_5545_max=DF_joined_cleaned["air conditioner_5545"].max()
DF_joined_cleaned["air conditioner_5545 Normalized"]=(DF_joined_cleaned["air conditioner_5545"]-air_conditioner_5545_min)/(air_conditioner_5545_max-air_conditioner_5545_min)

gen_min=DF_joined_cleaned["gen"].min()
gen_max=DF_joined_cleaned["gen"].max()
DF_joined_cleaned["gen Normalized"]=(DF_joined_cleaned["gen"]-gen_min)/(gen_max-gen_min)


plt.figure()
plt.plot(DF_joined_cleaned["Temperature Normalized"])
plt.plot(DF_joined_cleaned["air conditioner_5545 Normalized"])
plt.plot(DF_joined_cleaned["gen Normalized"])
plt.xlabel("Time")
plt.ylabel("Normalized Data")