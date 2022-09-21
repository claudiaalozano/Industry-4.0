
import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm

base_dir = "corn2013-2017.txt"

data = pd.read_csv(base_dir)

# Convert the datetime from str to datetime object.
data["fecha"] = pd.to_datetime(data["fecha"])

# Determine the daily change in gold price.
data["precio_maiz"] = data["precio_maiz_usd"].diff()

# Restrict the data to later than 2008 Jan 01.
data = data[data["datetime"] >= pd.to_datetime("2013-01-06")]

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
plt.plot(data["fecha"], data["precio_maiz_usd"])
plt.xlabel("fecha")
plt.ylabel("precio maíz (usd)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(data["fecha"], data["precio_maiz"])
plt.xlabel("fecha")
plt.ylabel("precio maíz (usd)")
plt.grid(True)
plt.savefig("img\predicciones")

# Use the daily change in gold price as the observed measurements X.
X = data[["precio_maiz"]].values
# Build the HMM model and fit to the gold price change data.
model = hmm.GaussianHMM(n_components = 3, covariance_type = "diag", n_iter = 50, random_state = 42)
model.fit(X)
# Predict the hidden states corresponding to observed X.
Z = model.predict(X)
states = pd.unique(Z)

print("Unique states:")
print(states)

print("\nStart probabilities:")
print(model.startprob_)

print("\nTransition matrix:")
print(model.transmat_)

print("\nGaussian distribution means:")
print(model.means_)

plt.figure(figsize = (15, 10))
plt.subplot(2,1,1)
for i in states:
    want = (Z == i)
    x = data["fecha"].iloc[want]
    y = data["precio_maiz_usd"].iloc[want]
    plt.plot(x, y, '.')
plt.legend(states, fontsize=16)
plt.grid(True)
plt.xlabel("fecha", fontsize=16)
plt.ylabel("precio maiz (usd)", fontsize=16)
plt.subplot(2,1,2)
for i in states:
    want = (Z == i)
    x = data["fecha"].iloc[want]
    y = data["precio_maiz"].iloc[want]
    plt.plot(x, y, '.')
plt.legend(states, fontsize=16)
plt.grid(True)
plt.xlabel("fecha", fontsize=16)
plt.ylabel("precio maíz (usd)", fontsize=16)
plt.savefig("img\predicciones")
