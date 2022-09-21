import pandas as pd

dataframe1 = pd.read_csv('corn_OHLC2013-2017.txt')
dataframe1.to_csv('corn1.csv', index= None)
df= pd.read_csv('corn1.csv')
print(df)
