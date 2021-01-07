import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())
#print(london_data.iloc[100:200])

print(len(london_data))

temp=london_data['TemperatureC']
average_temp=temp.mean()
print(average_temp)

temperature_var=np.var(temp)
print(temperature_var)

temperature_standard_deviation=np.std(temp)
print(temperature_standard_deviation)

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]

print(june.head())

july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

junemean= np.mean(june)
print(junemean)

julymean= np.mean(july)
print(julymean)

print(np.std(june))
print(np.std(july))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

