# -*- coding: cp1251 -*-
import math
import pandas as pn

my_data = [5, 3.2, 4.7, 1.4]
df = pn.read_csv('iris.csv', sep=',')
w=1.01
data = 0

for i in range(4):
    data += w*math.sqrt(math.pow(my_data[i]-df.iloc[0][i], 2))

index = 0

for i in range(1, len(df)):
    num = 0
    for j in range(4):
        num += w*math.sqrt(math.pow(my_data[j]-df.iloc[i][j], 2))
    if num < data:
        data = num
        index = i
        


print(f"Результат: {data}\nПозиція: {index}\n\nНайблищий сусід:\n{df.iloc[index]}\n\n"
      f"Невизначена категорія відноситься до {df.iloc[index][4]}.")


