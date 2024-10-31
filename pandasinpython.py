import pandas as pd

# series

l1 = [1,2,3,4,5]

data = pd.Series(l1)

print(data) 


data2 = pd.Series(l1 , index = ["a","b","c","d","e"])

print(data2)

# 
print("series for dictionary")


s2 = pd.Series({"a":10,"b":2,"c":3})
print(s2)


s21 = pd.Series({"a":10,"b":2,"c":3}, index=["c","a","d","b"])
print(s21)

# dataframe


df = pd.DataFrame({"Name":["akash","behzad","ali","akram","bajwa","bilal"],"Marks":[20,30,40,50,60,70]})
print(df)

print("Read csv file")
readcsv = pd.read_csv("filetest.csv")
print(readcsv)
print("------------")
print(readcsv.head())
print(readcsv.tail())
print(readcsv.shape)
print(readcsv.describe())

# iloc [indexrow h-l , indexcol h-l]
print(readcsv.iloc[0:3,1:5])

# functions in pandas
# 
print("pandas functions")
print("mean")
# print(readcsv.mean())
print("meidan")
# print(readcsv.median())
print("max")
print(readcsv.max())
print("min")
print(readcsv.min())

