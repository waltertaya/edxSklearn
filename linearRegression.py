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