#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:13:44 2026

@author: remisw
"""

import numpy as np

def metodo_potencias_pasos(A, x0, tol=1e-5, max_iter=50):
    # Inicialización
    # Evitar truncamientos convirtiendo a flotantes de 64 bits
    A = np.array(A, dtype=np.float64)
    x0 = np.array(x0, dtype=np.float64)
    n = len(A)
    
    print("\n" + "="*55)
    print(" INICIO: Método de las Potencias")
    print("="*55)
    print("Matriz A:")
    print(np.round(A, 4))
    print("\nVector inicial x0:")
    print(np.round(x0, 4))
    print("-" * 55)
    
    # --- FASE 1: Normalización inicial ---
    print("\n--- FASE 1: Normalización inicial ---")
    idx_max = np.argmax(np.abs(x0))
    x = x0 / x0[idx_max]
    print(f"[*] Vector x normalizado inicialmente:\n{np.round(x, 6)}")
    print("-" * 55)
    
    # Encabezado de la tabla de iteraciones
    print(f"\n{'Paso':<6} | {'Val. Propio (μ)':<16} | {'Error ∞':<15}")
    print("-" * 55)
    
    # --- FASE 2: Bucle iterativo ---
    for k in range(1, max_iter + 1):
        # Multiplicación matriz-vector
        y = np.dot(A, x)
        
        # Estimar valor propio dominante
        mu = y[idx_max]
        
        # Encontrar nuevo índice del máximo absoluto
        idx_max = np.argmax(np.abs(y))
        
        # Control de excepciones: vector nulo o mal condicionado
        if np.abs(y[idx_max]) < 1e-12:
            print("\n[!] ERROR: El vector colapsó a cero. El valor propio es 0.")
            return None, None
            
        # Calcular el error (Norma infinito de la diferencia de aproximaciones)
        x_new = y / y[idx_max]
        err = np.max(np.abs(x - x_new))
        
        print(f"{k:<6} | {mu:<16.6f} | {err:<15.6e}")
        
        # Actualizar vector
        x = x_new
        
        # Criterio de convergencia
        if err < tol:
            print("\n" + "="*55)
            print(f" [+] CONVERGENCIA ALCANZADA en {k} iteraciones.")
            print("="*55)
            return mu, x
            
    print("\n" + "="*55)
    print(" [-] Límite de iteraciones excedido.")
    print("="*55)
    return mu, x


# --- CASO DE ESTUDIO ---
# Parámetros (Ejemplo del marco teórico)
matriz_A = np.array([
    [2.0, 0.0, 0.0],
    [1.0, 1.0, 2.0],
    [1.0, -1.0, 4.0]
])

vector_x0 = np.array([1.0, 1.0, 1.0])

# Llamamos a la función
val_propio, vec_propio = metodo_potencias_pasos(matriz_A, vector_x0)

# Salida de resultados finales
print("\n--- RESULTADO FINAL ---")
if val_propio is not None:
    print(f"Valor propio dominante (μ): {val_propio:.6f}")
    print(f"Vector propio: {np.round(vec_propio, 6)}")
else:
    print("No se pudo calcular una solución válida.")
print("-" * 55)


# Práctica de Industria de Software: LAPACK / NumPy
print("\n--- Verificación Industrial (NumPy) ---")
# np.linalg.eig usa implementaciones asintóticamente robustas como el Algoritmo QR subyacente.
vals_numpy, vecs_numpy = np.linalg.eig(matriz_A)
print(f"Valores propios exactos:\n{np.round(vals_numpy, 6)}")
print("-" * 55)