# -*- coding: cp1251 -*-
import pandas as pn
import numpy as np

my_mas=np.zeros((3, 4))
Evk=np.zeros((3, 3))
df = pn.read_csv('iris.csv', sep=',')

flower={
    0:"Setosa",
    1:"Versicolor",
    2:"Virginica"
    }
for k in range(0, 3):
    counter=0
    for i in range(1, len(df)):
        if(df.iloc[i][4]==flower[k]):
            for j in range(0, 4):
                my_mas[k][j]+=df.iloc[i][j]
            counter=counter+1
    for x in range(0, 4):
        my_mas[0][x]=my_mas[0][x]/counter

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 4):
            Evk[i][j]+=(my_mas[i][k]-my_mas[j][k])*(my_mas[i][k]-my_mas[j][k])
print(Evk)

