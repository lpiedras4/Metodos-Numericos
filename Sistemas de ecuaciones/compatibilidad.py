import numpy as np

def evaluar_sistema_lineal(A,b):
  #Asegurarnos de que b es un vector columna para concatenar correctamente
  if b.ndim == 1:
    b = b.reshape(-1,1)
  
  #Inicializacion: formar la matriz aumentada [A|b]

  matriz_aumentada= np.hstack((A,b))

  #Calculo de rangos
  rango_A = np.linalg.matrix_rank(A)
  rango_aumentada = np.linalg.matrix_rank(matriz_aumentada)
  n_incognitas = A.shape[1]

  #Logica de evaluacion (Teorema de Rouche-Frobenius)
  if rango_A != rango_aumentada:
    diagnostico = "[!] SISTEMA ICNOSISTENTE. No existe solucion."
  else:
    if rango_A == n_incognitas:
      diagnostico = "[+] SISTEMA CONSISTENTE DETERMINADO. Posee una solucion unica"
    elif rango_A < n_incognitas:
      diagnostico = "[?] SISTEMA CONSISTENTE INDETERMINADO. Existen infinitas soluciones."
  

  #Salidas de la funcion
  return rango_A, rango_aumentada, n_incognitas, diagnostico


#CASO DE ESTUDIO 1: Asignación de recursode en Centro de Datos ...
print("\n--- EJEMPLO 1: Asignación de Tareas ---")
#Sistema de ecuaciones:
# 5x_1 + 2x_2 = 11
# 3x_1 + 6x_2 = 21

#Parámetros
A_centro_datos = np.array([[5,2],
                          [3,6]])

b_centro_datos = np.array([[11],[21]])

#Llamamos a la funcion
r_A, r_aug, n_inc, diag = evaluar_sistema_lineal(A_centro_datos, b_centro_datos)

#Salida de resultados
print("-" * 65)
print("Evaluando el sistema:")
print("5x_1 + 2x_2 = 11")
print("3x_1 + 6x_2 = 21")
print("-" * 65)
print(f"Rango de A: {r_A}")
print(f"Rango de Matrix Aumentada [A|b]: {r_aug}")
print(f"Numero de incognitas (n): {n_inc}")
print(f"Diagnostico: {diag}")
print("-" * 65)