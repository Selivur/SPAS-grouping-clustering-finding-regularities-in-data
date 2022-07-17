# -*- coding: cp1251 -*-
import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = pn.DataFrame({
     'age':[5,4,1,9, 1, 5],
     'race' : [45000,15000,17500,36000, 17500, 36000],
     'cost' : [1500,2200,1500,900, 700, 1200]
                 })
X = df['cost'].values[:, np.newaxis]  
Y = df['race'].values
model = LinearRegression()
model.fit(X, Y)
plt.title(f"y = {model.intercept_} + {model.coef_[0]}*x")
plt.scatter(X, Y)
plt.plot(X, model.predict(X), color='r', label='Linear Regression')
plt.legend()
plt.show()

