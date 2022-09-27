import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
from analisis import Analisis

fichero = Analisis.Transformacion()
fichero = Analisis.Limpiador()

data = pd.read_csv(fichero)
data = data.dropna()
data["Fecha"] = pd.to_datetime(data["Fecha"])
data["Cambios Precio Maiz"] = data["Precio Maiz"].diff()
data = data[data["Fecha"] >= pd.to_datetime("2013-01-06")]

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
plt.plot(data["Fecha"], data["Precio Maiz"])
plt.xlabel("Fecha")
plt.ylabel("Precio Maiz (usd)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(data["Fecha"], data["Cambios Precio Maiz"])
plt.xlabel("Fecha")
plt.ylabel("Cambios Precio Maiz (usd)")
plt.grid(True)
plt.savefig("graficos\datos")

X = data[["Cambios Precio Maiz"]].values
modelo = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
modelo.fit(X[1:])
Z = modelo.predict(X[1:])
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
    x = data["Fecha"].iloc[want]
    y = data["Precio Maiz"].iloc[want]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("Fecha", fontsize=16)
plt.ylabel("Precio Maiz (usd)", fontsize=16)
plt.subplot(2,1,2)
for i in estados:
    want = (Z == i)
    x = data["Fecha"[1:]].iloc[want]
    y = data["Cambios Precio Maiz"].iloc[want]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("Fecha", fontsize=16)
plt.ylabel("Cambio Precio Maiz (usd)", fontsize=16)
plt.savefig("graficos\predicciones")