import pandas as pd
import numpy as np

dataframes = pd.read_csv("covid_19_data.csv")

X = dataframes["Province/State"]
Y = dataframes["Deaths"]

for i in range(len(X)):
    print("{0}\t{1}".format(X[i], Y[i]))