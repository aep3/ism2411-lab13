# explore.py
# Author: Ashley Parker
# Module 13 Lab: First DataFrame — Retail Sales Explorer


# Reflection
# 1. A boolean filter allows me to select specific rows from a DataFrame based on a condition. For example, I can select only sales from the South region or sales with revenue greater than $1,000.
#
# 2. df["revenue"] returns a Series, which is a single column of data. df[["revenue"]] returns a DataFrame, even though it only contains one column. This matters when I need to keep the data in DataFrame format for additional operations.
#
# 3. I would choose pandas because it allows me to quickly filter, sort, calculate, and analyze thousands of rows of data without manually going through everything in Excel. It also makes it easier to repeat the same analysis on new datasets.


print("---Exercise 1---")

import pandas as pd

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


print("---Exercise 2---")

south = df[df["region"] == "South"]

print(len(south))
print(south.head())


print("---Exercise 3---")

top5 = df.sort_values('revenue', ascending=False).head(5)

print(top5)



print("---Exercise 4---")
big_south = df[(df['region']=='South') & (df['revenue']>1000)]

print(len(big_south))
print(big_south.head())



print("---Exercise 5---")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())



print("---Exercise 6---")
print(df['region'].unique())
print(df['region'].value_counts())




print("---Exercise 7---")
small_df = df[['region', 'product', 'revenue']]

print(small_df.shape)



print("---Exercise 8---")
df.to_csv('data/explored.csv', index=False)


print("File saved successfully!")