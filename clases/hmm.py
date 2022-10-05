import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
from analisis import Analisis

class CadenasMarkov():

    def __init__(self):
        Analisis.Transformacion()
        Analisis.Remplazar()
        Analisis.Limpiador()
        self.df = pd.read_csv("corn2.csv")
        self.df["0"] = pd.to_datetime(self.df["0"]) # Cambiamos la primera columna de string a un objeto datatime
        self.df["2"] = self.df["1"].diff() # Creamos una columna nueva con la diferencia de los precios de maíz
        self.Z = 0
        self.estados = 0

    def grafica_datos(self):
        plt.figure(figsize = (15, 10))
        plt.subplot(2,1,1)
        plt.plot(self.df["0"], self.df["1"])
        plt.xlabel("Fecha")
        plt.ylabel("Precio del Maíz")
        plt.grid(True)
        plt.subplot(2,1,2)
        plt.plot(self.df["0"], self.df["2"])
        plt.xlabel("Fecha")
        plt.ylabel("Diferencia del Precio del Maíz")
        plt.grid(True)
        plt.savefig("graficos/datos.png")

    def analisis_markov(self):
        X = self.df[["2"]].iloc[1:].values # Vamos a observar los valores de la diferencia de precios del maíz
        # Creamos un modelo HMM y metemos los datos observados
        modelo = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
        modelo.fit(X)

        # Ahora predecimos con el siguiente código
        self.Z = modelo.predict(X)
        self.estados = pd.unique(self.Z)

    def grafica_predicciones(self):
        plt.figure(figsize = (15, 10))
        plt.subplot(2,1,1)
        for i in self.estados:
            want = (self.Z == i)
            x = self.df["0"].iloc[1:].iloc[want]
            y = self.df["1"].iloc[1:].iloc[want]
            plt.plot(x, y, '.')
        plt.legend(self.estados, fontsize=16)
        plt.grid(True)
        plt.xlabel("Fecha", fontsize=16)
        plt.ylabel("Precio del Maíz", fontsize=16)
        plt.subplot(2,1,2)
        for i in self.estados:
            want = (self.Z == i)
            x = self.df["0"].iloc[1:].iloc[want]
            y = self.df["2"].iloc[1:].iloc[want]
            plt.plot(x, y, '.')
        plt.legend(self.estados, fontsize=16)
        plt.grid(True)
        plt.xlabel("Fecha", fontsize=16)
        plt.ylabel("Diferencia del Precio del Maíz", fontsize=16)
        plt.savefig("graficos/prediccion.png")

markov = CadenasMarkov()
markov.grafica_datos()
markov.analisis_markov()
markov.