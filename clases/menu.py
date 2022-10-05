from dtw import *
from hmm import *
def iniciar():
  print("=====================")
  print("=BIENVENIDOS AL MENU=")
  print("=====================")
  print("==[1] EJECUTAR HMM ==")
  print("==[2] EJECUTAR DTW ==")
  print("=====================")
  opcion= input('>')
  if opcion == 1:
    print("CARGANDO EL EJERCICIO...")
    markov = CadenasMarkov()
    markov1= markov.grafica_datos()
    markov2 =markov.analisis_markov()
    markov3=markov.grafica_predicciones()
    print(markov1)
    print(markov2)
    print(markov3)
    
