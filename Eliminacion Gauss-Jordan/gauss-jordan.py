import numpy as np

def gauss_jordan_pivoteo_pasos(A,b):
  #Inicialización
  #Evitar truncamienots convirtiendo la matriz a flotantes de 64 bits
  A = np.array(A, dtype=np.float64)
  b = np.array(b, dtype=np.float64)
  n = len(b)

  #Construir la matriz aumentada
  M = np.hstack((A, b.reshape(n,1)))

  print("\n" + "="*55)
  print(" INICIO: Matriz Aumentada [A | b]")
  print("="*55)
  print(np.round(M, 4))
  print("-"*55)

  # --- FASE 1: Reducción de Gauss-Jordan con Pivoteo Parcial ---
  for k in range(n):
    print(f"\n--- PASO {k+1}: Eliminaci[on y Normalizaci[on en la columna {k} ---]]")

    #Encontrar el índice de la fila con el máxim valor absoluto en la columna k 
    max_index = np.argmax(np.abs(M[k:n, k])) + k

    #Intercambiar la fila k con la fila max_index
    if max_index !=k:
      print(f"[*] Pivoteo: Intercambiando fila {k} con fila {max_index}")
      M[[k, max_index]] = M[[max_index, k]]
      print(np.round(M,4))
    else:
      print("[*] Pivoteo: No es necesario el intercambio (el pivote es máximo).")
    
    #Control de excepciones: matriz singular o mal condicionado
    if np.abs(M[k,k]) < 1e-12:
      print("ERROR: El sistema es singular o mal condicionado.")
      return None
    
    #Normalización del renglón pivote (hacer que el pivote sea 1)
    pivot_val = M[k,k]
    print(f"[*] Normalizando la fila pivote {k} (dividiendo entre {pivot_val:.4f})")
    M[k,:] = M[k, :] / pivot_val

    #Reducción copleta: Eliminación de los elementos arriba y abajo del pivoe
    print(f"[*] Haciendo ceros en la columna {k} (excepto el pivote)")
    for i in range(n):
      if i != k:
        factor = M[i,k]
        #Actualización vectorizada del renglón
        M[i,:] = M[i,:] - factor * M[k,:]

      print("Matriz resultante tras el Paso", k+1, ":")
      print(np.round(M,4))
      print("-"*55)

    # --- FASE 2: Extracción de la solución ---
    # En Gauss-Jordan, la matriz queda en forma escalonada reducida,
    # por lo que la última columna ya contiene la solución directa.
    print("\n" + "="*55)
    print(" FASE 2: Extracción del vector solución")
    print("="*55)

    x = M[:,n]

    #Imprimir valores indicviduales
    for i in range(n):
      print(f"x_{i} = {x[i]:.6f}")
    
    print("\n" + "="*55)
    return x

matriz_A = np.array([
  [5, 2 , 0],
  [2, 1, -1],
  [2, 3, -1]
])

vector_b = np.array([2, 0, 3])

#Llamamos a la función
solucion =  gauss_jordan_pivoteo_pasos(matriz_A,vector_b)

#Salida de resultados finales
print("\n--- RESULTADO FINAL ---")
if solucion is not None:
  print(f"Vector solución: {np.round(solucion,6)}")
else:
  print("No se pudo calcular una solución válida.")
print("-"*55)