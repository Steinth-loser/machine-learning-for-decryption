import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

data = pd.read_csv('data/data.csv')
X = data.iloc[:, 1: -1].values
Y = data.iloc[:, -1].values
Y = Y.reshape(len(Y), 1)
sc_X = StandardScaler()
sc_Y = StandardScaler()
X_train = sc_X.fit_transform(X)
Y_train = sc_Y.fit_transform(Y)

model = SVR(kernel='rbf')
model.fit(X_train, Y_train)
Y_pred = model.predict(X_train)

plt.scatter(X_train, Y_train)
plt.plot(X_train, Y_pred, color='red')
plt.show()

value = input()
print(sc_Y.inverse_transform(model.predict(sc_X.transform([[value]])).reshape(-1,1)))