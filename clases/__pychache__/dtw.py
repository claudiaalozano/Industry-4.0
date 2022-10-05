import numpy as np 
import matplotlib.pyplot as plt
import torch
import torchaudio
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
      cost = abs(first[i-1] - second[j-1])
      last_min = np.min([dtwmatriz[i-1, j], dtwmatriz[i, j-1], dtwmatriz[i-1, j-1]])
      dtwmatriz[i, j]= cost + last_min
      return dtwmatriz


def bestPath(out):
  i= out.shape[0] - 1
  j = out.shape[1] - 1
  point = out[i, j]
  path = [[i, j]]
  while [i, j] != [0, 0]:
    
    min= np.min([out[i-1, j], out[i, j-1],  out [i-1, j-1]])
    
    if out[i-1, j-1] == min:
      path.append([i-1, j-1])
      [i, j]=[i-1, j-1]
      
    elif out[i, j-1]== min:
      path.append([i, j-1])
      [i,j] = [i, j-1]
      
    else:
      path.append([i-1, j])
      [i,j] = [i-1, j]

  return path


def comparacion(i, j):
  print("Subimos los audios y bajamos el número de datos a cada audio.")
  dato1, _ = tourchaudio.load("")
