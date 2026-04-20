import numpy as np
import time as t
def multiplicacion_matricial (A, b):
  c = [[0]*len(b[0]) for _ in range(len(A))]

  for i in range(len(A)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        c[i][j] += A[i][k] * b[k][j]
  
  return c

matriz_A=[
  [2, 3, 5],
  [6, 7, 8]
]

matriz_B=[
  [1, 4],
  [2, 5],
  [3,6]
]


#Configuracion del experimento
iteraciones = 100
tiempos = []

for _ in range (iteraciones):
  inicio = t.perf_counter()
  C = multiplicacion_matricial(matriz_A, matriz_B)
  fin = t.perf_counter()
  tiempos.append(fin-inicio)

#Calculos de resultados
promedio = sum(tiempos) / iteraciones
mejor_tiempo = min(tiempos)
peor_tiempo = max(tiempos)

print(f" --- Resultados sobre {iteraciones} ejecuciones --- ")
print(f" Matriz resultante C: {C}")
print(f"Tiempo promedio: {promedio:.8f} segundos")
print(f"Mejor tiempo:    {mejor_tiempo:.8f} segundos")
print(f"Peor tiempo:     {peor_tiempo:.8f} segundos ")

A1=[
  [1, 2],
  [0, 3]
]

B1=[
  [4, -1],
  [2, 1]
]

#Calcular AB y luego transponer (AB)^T
C1 = multiplicacion_matricial(A1,B1)
C1 = np.transpose(C1)
print(C1)
#Calcular B^T y A^T por separado y multiplicar  B^T * A^T
Bt = np.transpose(B1)
At = np.transpose(A1)
C2 = multiplicacion_matricial( Bt,At )
print(C2)





