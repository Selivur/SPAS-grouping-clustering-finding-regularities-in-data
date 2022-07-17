# -*- coding: cp1251 -*-
import math
import numpy as np
import pandas as pn

df = pn.read_csv('iris.csv', sep=',')
my_mas=np.zeros((3,50))
Evk=np.zeros((3))
k1=0
k2=0
k3=0

for i in range(1, len(df)):
    if(df.iloc[i][4]=="Setosa"):
        for j in range(0, 3):
            print(str(j))
            my_mas[j][k1]=df.iloc[i][j]
        k1=k1+1
    if(df.iloc[i][4]=="Versicolor"):
        for j in range(0, 3):
            my_mas[j][k2]=df.iloc[i][j]
        k2=k2+1
    if(df.iloc[i][4]=="Virginica"):
        for j in range(0, 3):
            my_mas[j][k3]=df.iloc[i][j]
        k3=k3+1
for j in range(0, 3):
    my_mas[j].sort

for i in range (0, 3):
    for i in my_mas[i]:
        Evk[j]=
