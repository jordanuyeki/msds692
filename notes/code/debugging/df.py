import pandas as pd

df = pd.read_csv("../../data/SampleSuperstoreSales.csv")
print(df)
N = len(df)
sales = df['Sales']
print(sales)
