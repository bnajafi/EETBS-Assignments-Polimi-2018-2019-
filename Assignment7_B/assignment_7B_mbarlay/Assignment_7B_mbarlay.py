#Assignment 7A&7B

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

externalFiesFolder= r"C:\Users\My\Desktop\Laurea Magistrale\1st sem\ENERGY AND ENVIRONMENTAL TECHNOLOGIES FOR BUILDING SYSTEMS\files cloned\22.11.18-cloning\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles"
ConsumptinFileName="consumption_5545.csv"
IrradianceFileName="irradiance_2014_gen.csv"
TemperatureFileName="Austin_weather_2014.csv"

path_consumptionFile=os.path.join(externalFiesFolder,ConsumptinFileName)
path_irradianceFile=os.path.join(externalFiesFolder,IrradianceFileName)
path_temperatureFile=os.path.join(externalFiesFolder,TemperatureFileName)


DF_Consumption=pd.read_csv(path_consumptionFile, sep=",",index_col=0)
DF_Consumption.head()
PreviousIndex = DF_Consumption.index
NewParsedIndex= pd.to_datetime(PreviousIndex)
DF_Consumption.index= NewParsedIndex
DF_Consumption_InJuly=DF_Consumption["2014-05-15 00:00:00":"2014-05-30 23:00:00"]
plt.figure()
plt.plot(DF_Consumption_InJuly)
plt.ylabel("W")
plt.show()

DF_weather = pd.read_csv(path_temperatureFile, sep=";",index_col=0)
DF_weather.head(24)
PreviousIndex_weather=DF_weather.index
newIndex_weather=pd.to_datetime(PreviousIndex_weather)
DF_weather.index=newIndex_weather
Series_Temperature=DF_weather["temperature"]
DF_Temperature=DF_weather[["temperature"]]


DF_Temperature_InMay=DF_Temperature["2014-05-15 00:00:00":"2014-05-30 23:00:00"]
plt.figure()
plt.plot(DF_Temperature_InMay)
plt.xlabel("time")
plt.ylabel("temperature")
plt.show()

DF_irradianceSource=pd.read_csv(path_irradianceFile, sep=";",index_col=1)
DF_irradiance=DF_irradianceSource[["gen"]]
DF_irradiance["gen"]<0
DF_irradiance[DF_irradiance["gen"]<0]=0

DF_irradiance_InMay=DF_irradiance["2014-05-15 00:00:00":"2014-05-30 00:00:00"]
plt.figure()
DF_irradiance_InMay.plot()
plt.xlabel("time")
plt.ylabel("W")
plt.show()


#for two graphs in one graph: insert their normalizations

temp_min=DF_Temperature_InMay["temperature"].min()
temp_max=DF_Temperature_InMay["temperature"].max()

DF_Temperature_InMay["temperature"]=(DF_Temperature_InMay["temperature"]-temp_min)/(temp_max-temp_min)
DF_Temperature_InMay.columns=pd.Series("Temperature_Normalized")

irr_min=DF_irradiance_InMay["gen"].min()
irr_max=DF_irradiance_InMay["gen"].max()

DF_irradiance_InMay["gen"]=(DF_irradiance_InMay["gen"]-irr_min)/(irr_max-irr_min)
DF_irradiance_InMay.columns=pd.Series("Irradiance_Normalized")

#for the joined graph:
DF_joined = DF_Consumption.join([DF_Temperature,DF_irradiance])
DF_joined["temperature_normalized"]=(DF_joined["temperature"]-temp_min)/(temp_max-temp_min)
DF_joined.head(24)

#plot.figure()
DF_joined.plot()
plt.xlabel("time")
plt.ylabel("Normalized")
plt.show()

