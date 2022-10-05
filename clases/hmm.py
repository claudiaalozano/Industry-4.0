import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
from analisis import Analisis

Analisis.Transformacion()
Analisis.Remplazar()
Analisis.Limpiador()

df = pd.read_csv("corn2.csv")

df["0"]=pd.to_datetime(df["0"]) # Cambiamos la primera columna de string a un objeto datatime
df["2"] = df["1"].diff() # Creamos una columna nueva con la diferencia de los precios de maíz

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
plt.plot(df["0"], df["1"])
plt.xlabel("Fecha")
plt.ylabel("Precio del Maíz")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(df["0"], df["2"])
plt.xlabel("Fecha")
plt.ylabel("Diferencia del Precio del Maíz")
plt.grid(True)
plt.savefig("graficos/datos.png")

X = df[["2"]].iloc[1:].values # Vamos a observar los valores de la diferencia de precios del maíz
# Creamos un modelo HMM y metemos los datos observados
modelo = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
modelo.fit(X)

# Ahora predecimos con el siguiente código
Z = modelo.predict(X)
estados = pd.unique(Z)

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
for i in estados:
    want = (Z == i)
    x = df["0"].iloc[1:]
    y = df["1"].iloc[1:]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("Fecha", fontsize=16)
plt.ylabel("Precio del Maíz", fontsize=16)
plt.subplot(2,1,2)
for i in estados:
    want = (Z == i)
    x = df["0"].iloc[1:]
    y = df["2"].iloc[1:]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("Fecha", fontsize=16)
plt.ylabel("Diferencia del Precio del Maíz", fontsize=16)
plt.savefig("graficos/prediccion.png")