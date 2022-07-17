# -*- coding: cp1251 -*-
import math
import pandas as pn
import numpy as np
my_mas=np.zeros((3, 4))
num=np.array([0., 0., 0.])

my_data = [5., 30.2, 4.7, 1.4]

df = pn.read_csv('iris.csv', sep=',')

data = 0
counter=0
for i in range(1, len(df)):
    if(df.iloc[i][4]=="Setosa"):
        for j in range(0, 4):
            my_mas[0][j]+=df.iloc[i][j]
        counter=counter+1
for x in range(0, 4):
    my_mas[0][x]=my_mas[0][x]/counter
#
counter=0
for i in range(1, len(df)):
    if(df.iloc[i][4]=="Versicolor"):
        for j in range(0, 4):
            my_mas[1][j]+=df.iloc[i][j]
        counter=counter+1
for x in range(0, 4):
    my_mas[1][x]=my_mas[1][x]/counter
#
counter=0
for i in range(1, len(df)):
    if(df.iloc[i][4]=="Virginica"):
        for j in range(0, 4):
            my_mas[2][j]+=df.iloc[i][j]
        counter=counter+1
for x in range(0, 4):
    my_mas[2][x]=my_mas[2][x]/counter

    #cos
for i in range(0, len(my_mas)):
    a=0.
    b=0.
    for j in range(0, 4):
        num[i] += my_data[j] * my_mas[i][j]
        a+=math.pow(my_data[j], 2)
        b+=math.pow(my_mas[i][j], 2)
    num[i]=num[i]/ math.sqrt( a*b )
    print(str(num[i]))

print(str(num.argmin()))
if(num.argmin()==0):
    print("This is Setosa")
if(num.argmin()==1):
    print("This is Versicolor")
if(num.argmin()==2):
    print("This is Virginica")

