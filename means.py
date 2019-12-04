import time
import os
import pandas

if os.path.exists("c1_temperature_data.csv"):
    data = pandas.read_csv("c1_temperature_data.csv")
    print("The data set 1 mean is") 
    print(data.mean())
else:
    print("File does not exist.")

if os.path.exists("c2_temperature_data.csv"):
    data = pandas.read_csv("c2_temperature_data.csv")
    print("The data set 2 mean is") 
    print(data.mean())
else:
    print("File does not exist.")