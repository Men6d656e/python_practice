
# EDA Exploratary Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('filetest.csv')
x = data.head()

print(x)


data2 = pd.read_csv('automobileDataFromGrtLrgPractice.csv')
y = data2.head()


print(y)

shp = data2.info()
clms = data2.columns

print(shp)
print(clms)


# data pre processing

preposs = data2.isna().any()
preposs2 = data.isna().any()

print(preposs)
print(preposs2)

des = data2.describe()
print(des)

asd = data2['symboling'].count()
print(asd)




asd2 = data2['symboling'].unique()
print(asd2)



asd3 = data2['horsepower'].max()
print(asd3)

# error wala
asd4 = data2.iloc[data2['symboling'].idxmax()]
print(asd4)


