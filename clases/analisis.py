import pandas as pd

class Analisis():
  
  def Transformacion(): # Pasamos el dataset de txt a csv.

    dataframe1 = pd.read_csv('corn_OHLC2013-2017.txt')
    dataframe1.to_csv('corn1.csv', index= None)
    df1 = pd.read_csv('corn1.csv')

    dataframe2 = pd.read_csv('corn2013-2017.txt')
    dataframe2.to_csv('corn2.csv', index= None)
    df2 = pd.read_csv('corn2.csv')

    dataframe3 = pd.read_csv('corn2015-2017.txt')
    dataframe3.to_csv('corn3.csv', index= None)
    df3 = pd.read_csv('corn3.csv')

    return(df1, df2, df3)

  def Remplazar(): #Remplazamos las comas por puntos y comas
    x1= pd.read_csv('corn1.csv', sep=';')
    x2= pd.read_csv('corn2.csv', sep=';')
    x3= pd.read_csv('corn3.csv', sep=';')

    return(x1, x2, x3)
  
  def Limpiador(): # Limpiamos el dataset para asegurarnos de no tener elementos nulos.

    dato1 = pd.read_csv('corn1.csv')
    c1 = dato1.dropna()

    dato2 = pd.read_csv('corn2.csv')
    c2 = dato2.dropna()
    
    dato3 = pd.read_csv('corn3.csv')
    c3 = dato3.dropna()
    
    return(c1,c2,c3)