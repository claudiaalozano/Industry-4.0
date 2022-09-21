import pandas as pd

dataframe1 = pd.read_csv('corn_OHLC2013-2017.txt')
dataframe1.to_csv('corn1.csv', index= None)
df= pd.read_csv('corn1.csv')
print(df)


dataframe2= pd.read_csv('corn2013-2017.txt')
dataframe2.to_csv('corn2.csv', index= None)
df2= pd.read_csv('corn2.csv')
print(df2)


dataframe3= pd.read_csv('corn2015-2017.txt')
dataframe2.to_csv('corn3.csv', index= None)
df2= pd.read_csv('corn3.csv')
print(df2)

