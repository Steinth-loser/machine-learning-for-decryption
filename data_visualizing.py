import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv')

x = data.iloc[:, 1: -1].values
y = data.iloc[:, -1].values

x_log = np.log(x)

plt.scatter(x, y)
plt.title("Which letter / Encrypet Value")
plt.xlabel("Encrypted value")
plt.ylabel("Which Letter in Alphabet")
plt.show()

plt.scatter(x_log, y)
plt.show()