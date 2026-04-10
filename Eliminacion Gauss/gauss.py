import numpy as np

def eliminacion_gauss_pivoteo_pasos(A,b):
  #Inicializacion
  #Evitar truncamiento convirtiendo la matriz a flotantes de 64 bits
  A = np.array(A, dtype=np.float64)
  b = np.array(b, dtype=np.float64)
  n = len(b)


  #Construir la matriz aumentada
  M = np.hstack((A, b.reshape(n,1)))

  print("\n" + "="*55)
  print(" INICIO: Matriz Aumentada [A | b]")
  print("="*55)
  print(np.round(M,4))
  print("-" * 55)

  # --- FASE 1: Eliminaci[on hacia adelante con Pivoteo Parcial ---
  for k in range(n - 1):
    print(f"\n--- PASO {k+1}: Eliminacion en la columna {k} ---")

    #Encontrar el indice de la fila con el maximo valor absoluto en la columna j
    max_index = np.argmax(np.abs(M[k:n, k])) + k

      #Intercambiar la fila k con la fila max_index
    if max_index != k:
        print(f"[*] Pivoteo: Intercambiando fila {k} con fila {max_index}")
        M[[k,max_index]] = M[[max_index,k]]
        print(np.round(M,4))
    else:
        print("[*] Pivoteo: No es necesario el intercambio (el pivoteo es maximo). ")
      
      #Control de excepciones: matriz singular o mal condicionada
    if np.abs(M[k,k]) < 1e-12:
        print("ERROR: El sistema es singular o mal condicionado.")
        return None
      
      #Eliminacion de los elementos bajo el pivote
    print(f"[*] Eliminando elementos bajo el pivote M[{k},{k}] = {M[k,k]:.4f}")
    for i in range(k + 1, n):
        factor = M[i,k] / M[k,k]
        #Actualizacion vectorizada del renglon
        M[i,k:] = M[i,k:] - factor * M[k,k:]

    print("Matriz resultante tras la eliminacion:")
    print(np.round(M,4))
    print("-" * 55)

  #--- FASE 2: Sustitucion hacia atras ---
  print("\n" + "="*55)
  print(" FASE 2: Sustitucion hacia atras")
  print("="*55)

  x = np.zeros(n)

  #Despejar de abajo hacia arriba
  x[n-1] = M[n-1,n] / M[n-1, n-1]
  print(f"x_{n-1} = {x[n-1]:.6f}")

  #Ciclo 
  for i in range(n-2, -1, -1):
    #Uso de producto punto de numpy para sumar eficientemente
    suma = np.dot(M[i,i+1:n], x[i+1:n])
    x[i] = (M[i,n] - suma) / M[i,i]
    print(f"x_{i} = {x[i]:.6f}")
  
  #Salida
  print("\n" + "="*55)
  return x


# # --- CASO DE ESTUDIO
# # Parametros
# matriz_A = np.array

matriz_A = np.array([
  [5, 2 , 0],
  [2, 1, -1],
  [2, 3, -1]

])    

vector_b = np.array([2, 0, 3])

solucion = eliminacion_gauss_pivoteo_pasos(matriz_A, vector_b)

#Salida de resultados finales
print("\n--- RESULTADO FINAL ---")
if solucion is not None:
  print(f"Vector solución: {np.round(solucion,6)}")
else:
  print("No se pudo calcular una solucion válida")
print("-" * 75)

