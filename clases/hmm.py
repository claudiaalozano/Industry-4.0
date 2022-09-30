import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
from analisis import Analisis
import numpy as np

Analisis.Transformacion()
Analisis.Limpiador()

data = pd.read_csv("corn2.csv")
data = pd.DataFrame(np.vstack([data.columns, data]))

print(data)

data[0] = pd.to_datetime(data[0])
data[2] = data[1].diff()
data = data[data[0] >= pd.to_datetime("2013-01-06")]

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
plt.plot(data[0], data[1])
plt.xlabel("Fecha")
plt.ylabel("Precio Maiz (usd)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(data[0], data[2])
plt.xlabel("Fecha")
plt.ylabel("Cambios Precio Maiz (usd)")
plt.grid(True)
plt.savefig("graficos\datos")

X = data[[2]].values
modelo = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
modelo.fit(X)
Z = modelo.predict(X)
estados = pd.unique(Z)

print("Estados únicos:")
print(estados)
print("\nComenzar probabilidades:")
print(modelo.startprob_)
print("\nMatriz de transición:")
print(modelo.transmat_)
print("\nMedias de distribución Gaussiana:")
print(modelo.means_)
print("\nCovarianzas de distribución Gaussiana:")
print(modelo.covars_)

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
for i in estados:
    want = (Z == i)
    x = data[0].iloc[want]
    y = data[1].iloc[want]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("Fecha", fontsize=16)
plt.ylabel("Precio Maiz (usd)", fontsize=16)
plt.subplot(2,1,2)
for i in estados:
    want = (Z == i)
    x = data[0].iloc[want]
    y = data[2].iloc[want]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("Fecha", fontsize=16)
plt.ylabel("Cambio Precio Maiz (usd)", fontsize=16)
plt.savefig("graficos\predicciones")