import hmm 

def iniciar():
  print("========================")
  print("  Bienvenido al menú ") 
  print("========================")
  print("[1] Ejecutar el hmm ")
  print('[2] Ejecutar el dtw')

  opcion = input('>')

  if opcion == 1:
    print('Ejecutando el hmm....')
    markov = CadenasMarkov()
    markov.grafica_datos()
    markov.analisis_markov()
    markov.grafica_predicciones()
  elif opcion == 2:
    print('Ejecutando el dtw...')
    
