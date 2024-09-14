import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv('data/data.csv')

X = data.iloc[:, 1:-1].values
Y = data.iloc[:, -1].values
X_log = np.log(X)

PF = PolynomialFeatures(degree=2)
X_train = PF.fit_transform(X_log)
model = LinearRegression()
model.fit(X_train, Y)

Y_pred = model.predict(X_train)
#Visualizing the Status

print(Y_pred)
print(model.predict(PF.fit_transform(np.log([[8]])))) # for c (3. letter)
print(model.predict(PF.fit_transform(np.log([[48]])))) #for g (7. letter)