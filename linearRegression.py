import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from sklearn import linear_model
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
destination = "FuelConsumption.csv"
response = requests.get(url)
with open(destination, "wb") as file:
    file.write(response.content)

df = pd.read_csv(destination)

print(df.head())
df.describe()

cdf = df[['CYLINDERS','ENGINESIZE','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

# scatter graph for the cylinders against emissions
plt.scatter(cdf.CYLINDERS,cdf.CO2EMISSIONS,color='red')
plt.xlabel("Cylinders")
plt.ylabel("Emissions")
plt.show()

#scatter graph for the engine size against emissions
plt.scatter(cdf.ENGINESIZE,cdf.CO2EMISSIONS,color='red')
plt.xlabel("Engine Size")
plt.ylabel("Emissions")
plt.show()

#scatter graph for the fuel consumption comb against emissions
plt.scatter(cdf.FUELCONSUMPTION_COMB,cdf.CO2EMISSIONS,color='red')
plt.xlabel("Fuel Consumption Comb")
plt.ylabel("Emissions")
plt.show()