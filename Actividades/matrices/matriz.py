import numpy as np
import time as t
def multiplicacion_matricial (A, b):
  c = [[0]*len(b[0]) for _ in range(len(A))]

  for i in range(len(A)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        c[i][j] += A[i][k] * b[k][j]
  
  return c

matriz_A= np.array([
  [2, 3, 5],
  [6, 7, 8]
])

matriz_B= np.array([
  [1, 4],
  [2, 5],
  [3,6]
])

inicio = multiplicacion_matricial(matriz_A, matriz_B)

fin = t.perf_counter()
print("Matriz C:")
for r in inicio:
  print(r)
print(f"Tiempo de ejecución: {fin - inicio:.8f} segundos")





