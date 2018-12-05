# -*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt
import os 

ExternalFileFolder = r"C:\Users\elbar\Dropbox\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles"
ConsumptionFileName="consumption_5545.csv"
TemperatureFileName="Austin_weather_2014.csv"
IrradiationFileName="irradiance_2014_gen.csv"

path_consumptionFile= os.path.join(ExternalFileFolder,ConsumptionFileName)
path_TemperatureFile=os.path.join(ExternalFileFolder,TemperatureFileName)
path_IrradiationFile=os.path.join(ExternalFileFolder,IrradiationFileName)

#CONSUMPTION

DF_consumption= pd.read_csv(path_consumptionFile, sep=",", index_col=0)
DF_consumption.head()
DF_consumption.tail(10)

Previous_index=DF_consumption.index
NewParsedIndex = pd.to_datetime(Previous_index)
DF_consumption.index=NewParsedIndex

DF_consumption_may=DF_consumption["2014-05-15 00:00:00":"2014-05-30 00:00:00"]

plt.figure()
DF_consumption_may.plot()
plt.xlabel("time")
plt.ylabel("Ac Power (W)")
plt.show()

#TEMPERATURE

DF_weather= pd.read_csv(path_TemperatureFile, sep=";", index_col=0)
DF_weather.head(24)

PreviousIndex_weather=DF_weather.index
newIndex_weather=pd.to_datetime(PreviousIndex_weather)
DF_weather.index=newIndex_weather

Series_Temperature=DF_weather["temperature"]

DF_Temperature=DF_weather[["temperature"]]

DF_Temperature_may=DF_Temperature["2014-05-15 00:00:00":"2014-05-30 00:00:00"]

plt.figure()
DF_Temperature_may.plot()
plt.xlabel("time")
plt.ylabel("temperature Farhenite")
plt.show()

#IRRADIATION (PHOTOVOLTAIC GENERATION)

DF_irradianceSource= pd.read_csv(path_IrradiationFile, sep=";", index_col=1)

DF_irradiance=DF_irradianceSource[["gen"]]

DF_irradiance["gen"]<0
DF_irradiance[DF_irradiance["gen"]<0]=0

DF_irradiance_may=DF_irradiance["2014-05-15 00:00:00":"2014-05-30 00:00:00"]

plt.figure()
DF_irradiance_may.plot()
plt.xlabel("time")
plt.ylabel("Generation W")
plt.show()

fig,ax=plt.subplots(3) #figure s the all frame, ax is a list with the name of which is associated the axes
ax[0].DF_irradiance_may.plot()
ax[1].DF_Temperature_may.plot()
ax[3].DF_consumption.plot()




#TEMPERATURE NORMALIZATION
temp_min=DF_Temperature_may["temperature"].min()
temp_max=DF_Temperature_may["temperature"].max()

DF_Temperature_may["temperature"]=(DF_Temperature_may["temperature"]-temp_min)/(temp_max-temp_min)
DF_Temperature_may.columns=pd.Series("Temperature_Normalized")

#CONSUMPTION NORMALIZATION
cons_min=DF_consumption_may["air conditioner_5545"].min()
cons_max=DF_consumption_may["air conditioner_5545"].max()

DF_consumption_may["air conditioner_5545"]=(DF_consumption_may["air conditioner_5545"]-cons_min)/(cons_max-cons_min)
DF_consumption_may.columns=pd.Series("Consumption_Normalized")

#IRRADIANCE (THROUGH THE PHOTOVOLTAIC GENERATION) NORMALIZATION
gen_min=DF_irradiance_may["gen"].min()
gen_max=DF_irradiance_may["gen"].max()

DF_irradiance_may["gen"]=(DF_irradiance_may["gen"]-gen_min)/(gen_max-gen_min)
DF_irradiance_may.columns=pd.Series("Generation_Normalized")

DF_joined_may=DF_consumption_may.join([DF_Temperature_may,DF_irradiance_may])
DF_joined_may.head(24)

#for the plot

plt.figure()
DF_joined_may.plot()
plt.xlabel("time")
plt.ylabel("Values_Normalized")
plt.show()

