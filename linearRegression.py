import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from pyodide.http import pyfetch

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

async def get_data(url, filename):
    response = await pyfetch(url)
    if response.status != 200:
        raise Exception("HTTP error: " + str(response.status))
    else:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
            
get_data(path, "FuelConsumption.csv")
path = "FuelConsumption.csv"

df = pd.read_csv(FuelConsumption.csv)

df.head()