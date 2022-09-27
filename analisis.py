import pandas as pd

class Analisis():
  
  def Transformacion(): # Pasamos el dataset de txt a csv.

    dataframe1 = pd.read_csv('corn_OHLC2013-2017.txt')
    dataframe1.to_csv('corn1.csv', index= None)
    df= pd.read_csv('corn1.csv')
    df.columns = [["Fecha", "Precio Maíz"]]

    dataframe2= pd.read_csv('corn2013-2017.txt')
    dataframe2.to_csv('corn2.csv', index= None)
    df2= pd.read_csv('corn2.csv')
    df2.columns = [["Fecha", "Precio Maíz"]]

    dataframe3= pd.read_csv('corn2015-2017.txt')
    dataframe3.to_csv('corn3.csv', index= None)
    df3= pd.read_csv('corn3.csv')
    df3.columns = [["Fecha", "Precio Maíz"]]

    return(df, df2, df3)
  
  def Limpiador(): # Limpiamos el dataset para asegurarnos de no tener elementos nulos.

    dato1= pd.read_csv('corn1.csv')
    c1=dato1.dropna()

    dato2= pd.read_csv('corn2.csv')
    c2=dato2.dropna()
    
    dato3=pd.read_csv('corn3.csv')
    c3=dato3.dropna()
    
    return(c1,c2,c3)