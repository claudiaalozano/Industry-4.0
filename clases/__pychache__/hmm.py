import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm

class HiddenMarkovModels():

  def __innit__(self, fichero):
    self.data = pd.read_csv(str(fichero))
    self.data[0] = pd.to_datetime(self.data[0]) 
    self.data[2] = self.data[1].diff()
    self.data = self.data[self.data[0] >= pd.to_datetime("2013-01-06")]
    self.Z = 0
    self.estados = 0

  def grafica_datos(self):
    plt.figure(figsize = (15, 10))
    plt.subplot(2,1,1)
    plt.plot(self.data[0], self.data[1])
    plt.xlabel("fecha")
    plt.ylabel("precio maíz (usd)")
    plt.grid(True)
    plt.subplot(2,1,2)
    plt.plot(self.data[0], self.data[2])
    plt.xlabel("fecha")
    plt.ylabel("precio maíz (usd)")
    plt.grid(True)
    plt.savefig("img\datos")

  def modelo_markov(self):
    # Use the daily change in gold price as the observed measurements X.
    X = self.data[[2]].values
    # Build the HMM model and fit to the gold price change data.
    modelo = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
    modelo.fit(self.X)
    # Predict the hidden states corresponding to observed X.
    self.Z = modelo.predict(X)
    self.estados = pd.unique(self.Z)
    
    print("Estados únicos:")
    print(self.estados)
    print("\nComenzamos probabilidades:")
    print(modelo.startprob_)
    print("\nMatriz de transición:")
    print(modelo.transmat_)
    print("\nMedias de distribución gaussiana:")
    print(modelo.means_)

  def grafica_prediccion(self):
    plt.figure(figsize = (15, 10))
    plt.subplot(2,1,1)
    for i in self.estados:
        want = (self.Z == i)
        x = self.data[0].iloc[want]
        y = self.data[1].iloc[want]
        plt.plot(x, y, '.')
    plt.legend(self.estados, fontsize=16)
    plt.grid(True)
    plt.xlabel("fecha", fontsize=16)
    plt.ylabel("precio maiz (usd)", fontsize=16)
    plt.subplot(2,1,2)
    for i in self.states:
        want = (self.Z == i)
        x = self.data[0].iloc[want]
        y = self.data[2].iloc[want]
        plt.plot(x, y, '.')
    plt.legend(self.states, fontsize=16)
    plt.grid(True)
    plt.xlabel("fecha", fontsize=16)
    plt.ylabel("precio maíz (usd)", fontsize=16)
    plt.savefig("img\predicciones")


fichero = "corn2.csv"
HiddenMarkovModels(fichero).grafica_datos()
HiddenMarkovModels(fichero).modelo_markov()
HiddenMarkovModels(fichero).grafica_prediccion()
