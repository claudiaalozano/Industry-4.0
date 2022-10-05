import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_io as tfio
from IPython.display import Audio, display

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
  dato1 = tfio.audio.AudioIOTensor("C:\Users\Claudia\Desktop\Industry-4.0\audios_dtw" + str(i) + ".mp3")
  dato2= tfio.audio.AudioIOTensor("C:\Users\Claudia\Desktop\Industry-4.0\audios_dtw" + str(i) + ".mp3")

  aux1 = dato1.to_tensor()
  aux2 = dato2.to_tensor()

  aux1 = aux1 [:, 0]
  aux2 = aux2 [:, 0]
  
  
  a = tfio.audio.resample(aux1, dato1.rate.numpy(), 800)
  b = tfio.audio.resample(aux2, dato1.rate.numpy(), 800)

  print("mostramos los dos audios para comparar.")
  Audio(a.numpy(), rate=dato1.rate.numpy() )
  Audio(b.numpy(), rate=dato2.rate.numpy() )
  

  out = dtw(list(a), list(b))
  z = bestPath (out)
  print("Cuanto más recta sea la línea azul, presenta más relación y cercanía las dos notas de voz.")

  x =[]
  y =[]

  for i,j in z:
    x.append(i)
    y.append(j)

  plt.figure(figsize =(10,10))
  plt.plot(y, x, color ="blue")
  plt.imshow(out,cmap="hot", interpolation="nearset")
  plt.show()

  print("la distancia entre las dos series temporales es: " + str(out[-1][-1]))

  print("Mostramos las señales de cada nota de voz para ver la diferencia entre ambas.")
  plt.figure(figsize=(10,10))
  plt.plot(a)
  plt.plot(b)
  plt.legend(["Line a", "Line b"])
  plt.show()

  z.remove([0,0])
  plt.figure(figsize=(10,10))
  print("Unimos las dos series de tiempo.")

  for i, j in z:
    plt.plot([j-1, i-1] , [b[j-1], a [i-1]], color ="green")
    plt.plot(a)
    plt.plot(b)
    plt.show()


def prueba(i, j):
  comparacion(i, j)

def izquierda_con_derecha():
  izquierda =["1", "3", "5", "7" , "9"]
  for i in range (len(izquierda) -1):
    comparacion(izquierda[i], izquierda[i+1])

izquierda_con_derecha()

prueba("1", "5")

print(prueba)
print(izquierda_con_derecha)
