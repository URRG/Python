import pandas as pd

df=pd.read_csv("vehicle.csv")

print(df)

a=df["fuel"].dtype
b=df["selling_price"].dtype
print(a)
print(b)
tempdf=df.append(df)
print(tempdf.shape)
tempdf=tempdf.drop_duplicates()
print(tempdf.shape)

print(df.columns)
print(df.isnull())
print(df.isnull().sum())
count=df["name"].value_counts()
print(count)
r=df[(df["selling_price"]<=200000)]
print(r)
