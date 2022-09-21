import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
from analisis import Analisis

fichero = "https://storage.googleapis.com/kagglesdsdata/datasets/2807/4869/corn2013-2017.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220921T134656Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=6e75c8a1116e1406d1b21aac82fc7ece8a18947f42f52c1e16e58591191d506a16f0bf681f6c082e00197ff27581f9c95f0de04bebadc2c6afecdaa9dbb1e63812954d0aa2bf51e2eceb89ae32a9e12525dde9ace41d37b5d740001337c209f20707878b9cc95838c8ce84f344e70f6fd8b3f221162aca56d7fdec284ba8f4751f6ca65b0bd8a1bf235efa2756c085e2c4e9f9f78cde3108ec6618fbffda66badc4b450690b607ff488300d518a5e4d8e364055ea5b24e86c0be3911ec6bffb070e99ae8e04a5d58f374195ba166d21bbd106a0ef85f74768cdc93e2bbd4c67309b19e243dd02a4a08a70238ca32d9b757d4126360f99b7d7f99e1208b0a4224"

nombre_columnas = ["Fecha", "Precio Maiz"]

data = pd.read_csv(fichero, names=nombre_columnas)
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