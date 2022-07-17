# -*- coding: cp1251 -*-
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
     'age':[5,4,1,9],
     'race' : [45000,15000,17500,36000],
     'cost' : [1500,2200,1500,900]
                 })
print(df)
print("\n")
df.to_csv('data.csv')
df = pd.read_csv('data.csv', sep=',')
print("\n")
print(df)
print("\n")
df=df.groupby('cost')['race'].mean()
print(df)
df.to_csv('data.csv')
df.plot(xlabel='race', ylabel="cost",x="race", y="cost")
plt.show()
