from dataset import 
import pandas as pd

dataframe2= pd.read_csv('dataset.corn2013-2017')
dataframe2.to_csv('corn2.csv', index= None)
dd= pd.read_csv('corn1.csv')
print(dd)
