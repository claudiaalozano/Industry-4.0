import numpy as np 
import matplotlib.pyplot as plt
import torch
impot torchaudio
import searbon as sns
import IPython.display import Audio, display

def dtw(first, second):
  n = len(first)
  m = len(second)

dtwmatriz= np.zeros((n+1, m+1))
for i in range(n+1):
  for j in range(m+1):
    dtwmatriz[i,j]= np.inf

dtwmatriz[0, 0] = 0

for i in range (1, n+1):
  for j in range (1, m+1):
  
