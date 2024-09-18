import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('data/data.csv')

X = dataset.iloc[:, 1: -1].values
Y = dataset.iloc[:, -1].values

model = RandomForestRegressor(n_estimators=20, random_state=0)
model.fit(X, Y)

Y_pred = model.predict(X)
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()

value = input()
print(model.predict([[value]]))
