import sys
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ExternalFilesFolder = os.path.dirname(sys.argv[0])
os.chdir(ExternalFilesFolder)
ConsumptionFileName = "consumption_5545.csv"
TemperatureFileName = "Austin_weather_2014.csv"
IraddianceFileName = "irradiance_2014_gen.csv"

path_consumptionFile = os.path.join(ExternalFilesFolder,ConsumptionFileName)
path_temperatureFile = os.path.join(ExternalFilesFolder,TemperatureFileName)
path_irradianceFile = os.path.join(ExternalFilesFolder,IraddianceFileName)

DF_Consumption = pd.read_csv(path_consumptionFile, sep = ',', index_col =0 )
PreviousIndex_Consumption = DF_Consumption.index
NewParsedIndex_Consumption = pd.to_datetime(PreviousIndex_Consumption)
DF_Consumption.index = NewParsedIndex_Consumption
DF_Consumption_SomeDaysInMay = DF_Consumption["2014-05-15 00:00:00" : "2014-05-30 23:00:00"]

DF_Weather = pd.read_csv(path_temperatureFile,sep=";",index_col=0)
PreviousIndex_Weather = DF_Weather.index
NewParsedIndex_Weather = pd.to_datetime(PreviousIndex_Weather)
DF_Weather.index = NewParsedIndex_Weather
DF_Temperature = DF_Weather[["temperature"]]           
DF_Temperature_SomeDaysInMay = DF_Temperature["2014-05-15 00:00:00" : "2014-05-30 23:00:00"]

DF_IrradianceSource = pd.read_csv(path_irradianceFile, sep = ";", index_col = 1)
DF_Irradiance = DF_IrradianceSource[["gen"]]
DF_Irradiance[DF_Irradiance["gen"]<0] = 0
DF_Irradiance_SomeDaysInMay = DF_Irradiance["2014-05-15 00:00:00" : "2014-05-30 23:00:00"]

DF_joined_SomeDaysInMay = DF_Consumption_SomeDaysInMay.join([DF_Temperature_SomeDaysInMay,DF_Irradiance_SomeDaysInMay])
DF_joined_SomeDaysInMay_Cleaned = DF_joined_SomeDaysInMay.dropna()

T_min = DF_joined_SomeDaysInMay_Cleaned["temperature"].min()
T_MAX = DF_joined_SomeDaysInMay_Cleaned["temperature"].max()

Consumption_min = DF_joined_SomeDaysInMay_Cleaned["air conditioner_5545"].min()
Consumption_MAX = DF_joined_SomeDaysInMay_Cleaned["air conditioner_5545"].max()

Gen_min = DF_joined_SomeDaysInMay_Cleaned["gen"].min()
Gen_MAX = DF_joined_SomeDaysInMay_Cleaned["gen"].max()

DF_joined_SomeDaysInMay_Cleaned["temperature_Normalized"] = (DF_joined_SomeDaysInMay_Cleaned["temperature"]-T_min)/(T_MAX-T_min)
DF_joined_SomeDaysInMay_Cleaned["air conditioner_5545_Normalized"] = (DF_joined_SomeDaysInMay_Cleaned["air conditioner_5545"]-Consumption_min)/(Consumption_MAX-Consumption_min)
DF_joined_SomeDaysInMay_Cleaned["gen_Normalized"] = (DF_joined_SomeDaysInMay_Cleaned["gen"]-Gen_min)/(Gen_MAX-Gen_min)

plt.figure()
plt.subplot(3,1,1)
plt.plot(DF_joined_SomeDaysInMay_Cleaned["air conditioner_5545"],'-', color = "r")
plt.xlabel("Time")
plt.ylabel("Power Consumption (W)")
plt.subplot(3,1,2)
plt.plot(DF_joined_SomeDaysInMay_Cleaned["temperature"],':', color = "g")
plt.xlabel("Time")
plt.ylabel("Temperature (F)")
plt.subplot(3,1,3)
plt.plot(DF_joined_SomeDaysInMay_Cleaned["gen"],'--',color = "y")
plt.xlabel("Time")
plt.ylabel("Irradiance (W)")
plt.show()

plt.figure()
plt.plot(DF_joined_SomeDaysInMay_Cleaned["air conditioner_5545_Normalized"],'-', color = "r")
plt.plot(DF_joined_SomeDaysInMay_Cleaned["temperature_Normalized"],':', color = "g")
plt.plot(DF_joined_SomeDaysInMay_Cleaned["gen_Normalized"],'--',color = "y")
plt.legend()
































