import numpy as np

def lu_doulittle_pasos (A, b):
    #Inicialización
    #Evitar truncamientos convirtiendo a flotantes de 64 bits
    A = np.array(A, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    n = len(b)

    print("\n" + "=" * 55)
    print(" INICIO: Matriz A (Original)")
    print("="*55)
    print(np.round(A, 4))
    print("-" * 55)

    # --- FASE 1: Descomposición ---
    print("\n" + "=" * 55)
    print("FASE 1: Descomposición LU")
    print(" (L debajo de la diagonal, U en la diagonal y arriba)")

    for k in range(n):
        print(f"\n--- Paso {k+1}: Iteración k={k} ---")

        # Calcular los elementos de U para la fila k
        for j in range(k, n):
            # Uso de produco punto para numpy para sumar eficientemente
            suma = np.dot(A[k, :k], A[:k,j])
            A[k, j] = A[k, j] - suma

        # Control de excepciones: matriz singular o mal condicionada
        if np.abs(A[k, k]) < 1e-12:
            print(f"ERROR: Elemento diagonal U[{k},{k}] es nulo. El sistema requiere pivoteo.")
            return None
        
        # Calcular los elementos de L para la columna k
        for i in range(k+1, n):
            suma = np.dot(A[i, :k], A[:k,k])
            A[i, k] = (A[i, k] - suma) / A[k, k]

        print(f"[*] Matriz A sobrescrita tras el paso {k+1}:")
        print(np.round(A, 4))
        print("=" * 55)

        # --- FASE 2: Sustitución hacia adelante (Ld = b) ---
        print("\n" + "=" * 55)
        print("FASE 2: Sustitución hacia adelante (Ld = b)")
        print("=" * 55)

        d = np.zeros(n)
        for i in range(n):
            # Producto punto de la fila i de L (estrictamente debajo de diagonal)
            suma = np.dot(A[i, :i], d[:i])
            d[i] = b[i] - suma
            print(f"d_{i}:.6f")

        # --- FASE 3: Sustitución hacia atrás (Ux = d) ---
        print("\n" + "=" * 55)
        print(" FASE 3: Sustitución hacia atrás (Ux = d)")
        print("="*55)

        x = np.zeros(n)

        # Despejar de abajo hacia arriba
        for i in range(n - 1, -1, -1):
            # Producto punto de la fia i de U (estrictamente a la derecha de la diagonal) con el vector x
            suma = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (d[i] - suma) / A[i, i]
            print(f"x_{i} = {x[i]:.6f}")
        
    print("\n" + "="*55)
    return x
    
# --- CASO DE ESTUDIO ---
# Parámetros
matriz_A = [
    [4, -9, 2],
    [2, -4, 6],
    [1, -1, 3]
]

vector_b = [5, 3, 4]

# Llamamos a la función
solucion = lu_doulittle_pasos(matriz_A, vector_b)

# Salida de resultados finales
print("\n --- RESULTADO FINAL ---")
if solucion is not None:
    print(f"Vector solución: {np.round(solucion, 6)}")
else:
    print("No se pudo calcular una solución válida.")
print("-" * 55)