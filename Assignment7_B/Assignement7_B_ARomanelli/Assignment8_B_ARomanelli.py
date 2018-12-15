import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ExternalFilesFolder=r"C:\Users\Alessia\Documents\Primo_anno_en\Building\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles"
TemperatureFileName="Austin_weather_2014.csv"
IrraditionFileName= "irradiance_2014_gen.csv"
ConsumptionFileName="consumption_5545.csv"

path_consumptionFile=os.path.join(ExternalFilesFolder,ConsumptionFileName)
path_temperatureFile=os.path.join(ExternalFilesFolder,TemperatureFileName)
path_irradiationFile=os.path.join(ExternalFilesFolder,IrraditionFileName)

DF_consumption=pd.read_csv(path_consumptionFile,sep=",",index_col=0)


PreviousIndex=DF_consumption.index
NewParsedIndex=pd.to_datetime(PreviousIndex)  #change dtype in datetime from object
DF_consumption.index=NewParsedIndex

DF_consumption_someDaysInMay=DF_consumption["2014-05-15 00:00:00":"2014-05-30 23:00:00"]



#Let's import weather data

DF_weather=pd.read_csv(path_temperatureFile,sep=";",index_col=0)  #pay attention ;
DF_weather.head(24)

PreviousIndex_weather=DF_weather.index
NewParsedIndex_weather=pd.to_datetime(PreviousIndex_weather)  
DF_weather.index=NewParsedIndex_weather

DF_weather_someDaysInMay=DF_weather["2014-05-15 00:00:00":"2014-05-30 23:00:00"]

DF_weather.columns
Series_Temperature=DF_weather_someDaysInMay["temperature"]

DF_Temperature=DF_weather_someDaysInMay[["temperature"]]



#Irradiance data
DF_irradiancesSource=pd.read_csv(path_irradiationFile,sep=";",index_col=1)  #time is second column

DF_irradiances=DF_irradiancesSource[["gen"]]


DF_irradiances["gen"]<0   #true is the night
DF_irradiances[DF_irradiances["gen"]<0]=0   #remove negative


PreviousIndexx=DF_irradiances.index
NewParsedIndexx=pd.to_datetime(PreviousIndexx)  #change dtype in datetime from object
DF_irradiances.index=NewParsedIndexx

DF_irradiances_someDaysInMay=DF_irradiances["2014-05-15 00:00:00":"2014-05-30 23:00:00"]


plt.figure()
plt.subplot(3,1,1) 
plt.plot(DF_irradiances_someDaysInMay)
plt.xlabel("Time")
plt.ylabel("Gen")

plt.subplot(3,1,2) 
plt.plot(DF_consumption_someDaysInMay)
plt.xlabel("Time")
plt.ylabel("AC Power(W)")

plt.subplot(3,1,3)  #number of row,columns,items
plt.plot(DF_Temperature)
plt.xlabel("Time")
plt.ylabel("Temperature")


#togheter

DF_joined=DF_consumption_someDaysInMay.join([DF_Temperature,DF_irradiances_someDaysInMay])

DF_joined.cleaned=DF_joined.dropna()   #remove eveything is not a number


#plot togheter, but first normalize temperatures,gen and power because the ranges are too different

temp_min=DF_joined.cleaned["temperature"].min() #show me the min temperature
temp_max=DF_joined.cleaned["temperature"].max() #show me the max temperature
DF_joined.cleaned["temperature_normalized"]=(DF_joined.cleaned["temperature"]-temp_min)/(temp_max-temp_min) #new column with normalized

gen_min=DF_joined.cleaned["gen"].min() #show me the min gen
gen_max=DF_joined.cleaned["gen"].max() #show me the max gen
DF_joined.cleaned["gen_normalized"]=(DF_joined.cleaned["gen"]-gen_min)/(gen_max-gen_min) #new column with normalized

cons_min=DF_joined.cleaned["air conditioner_5545"].min() #show me the min cons
cons_max=DF_joined.cleaned["air conditioner_5545"].max() #show me the max cons
DF_joined.cleaned["cons_normalized"]=(DF_joined.cleaned["air conditioner_5545"]-cons_min)/(cons_max-cons_min) #new column with normalized

plt.figure()
DF_joined.cleaned["temperature_normalized"].plot()
DF_joined.cleaned["gen_normalized"].plot()
DF_joined.cleaned["cons_normalized"].plot()
plt.xlabel("Time")
plt.ylabel("Values Normalized")
plt.legend()
plt.show()