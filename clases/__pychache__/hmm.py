import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm

base_dir = "corn2.csv"
data = pd.read_csv(base_dir)
data[0] = pd.to_datetime(data[0])
data[2] = data[1].diff()
data = data[data[0] >= pd.to_datetime("2013-01-06")]

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
plt.plot(data[0], data[1])
plt.xlabel("datetime")
plt.ylabel("gold price (usd)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(data[0], data[2])
plt.xlabel("datetime")
plt.ylabel("gold price change (usd)")
plt.grid(True)
plt.savefig("graficas\datos")

X = data[[2]].values
modelo = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
modelo.fit(X)
Z = modelo.predict(X)
estados = pd.unique(Z)

print("Unique states:")
print(estados)
print("\nStart probabilities:")
print(modelo.startprob_)
print("\nTransition matrix:")
print(modelo.transmat_)
print("\nGaussian distribution means:")
print(modelo.means_)
print("\nGaussian distribution covariances:")
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
plt.xlabel("datetime", fontsize=16)
plt.ylabel("gold price (usd)", fontsize=16)
plt.subplot(2,1,2)
for i in estados:
    want = (Z == i)
    x = data[0].iloc[want]
    y = data[2].iloc[want]
    plt.plot(x, y, '.')
plt.legend(estados, fontsize=16)
plt.grid(True)
plt.xlabel("datetime", fontsize=16)
plt.ylabel("gold price change (usd)", fontsize=16)
plt.savefig("graficas\predicciones")