#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:14:39 2026

@author: remisw
"""

def newton_modificado(f, df, ddf, p0, epsilon, N_max):
    # Inicialización
    iteracion = 0
    xr_old = p0
    error = 100.0
    
    # --- ENCABEZADO DE LA TABLA ---
    print("\n--- MÉTODO DE NEWTON-RAPHSON MODIFICADO ---")
    print(f"{'Iter':<5} | {'xr_old':<12} | {'xr':<12} | {'Error (%)':<12}")
    print("-" * 50)

    # Ciclo
    while iteracion < N_max:
        iteracion += 1
        
        # Evaluación de la función y sus derivadas
        f_val = f(xr_old)
        df_val = df(xr_old)
        ddf_val = ddf(xr_old)
        
        # Denominador específico del método de Newton-Raphson Modificado
        denominador = (df_val**2) - (f_val * ddf_val)
        
        # Control de excepciones: Cancelación sustractiva o denominador cero
        if denominador == 0:
            print("ERROR: Denominador igual a cero. Falla del método.")
            return None, iteracion, error
            
        # Cálculo de la raíz por Newton-Raphson Modificado
        xr = xr_old - (f_val * df_val) / denominador
        
        # Cálculo del error relativo aproximado porcentual
        if xr != 0:
            error = abs((xr - xr_old) / xr) * 100.0
        else:
            error = 0.0
            
        # --- IMPRESIÓN DE FILA ---
        print(f"{iteracion:<5} | {xr_old:<12.6f} | {xr:<12.6f} | {error:<12.6f}")
        
        # Verificación de paro
        if error < epsilon:
            print("-" * 50)
            return xr, iteracion, error
            
        # Actualizamos el valor anterior para la siguiente iteración
        xr_old = xr
        
    # Retorna la mejor aproximación si se alcanza N_max
    print("-" * 50)
    return xr, iteracion, error

# --- CASO DE ESTUDIO (Ejemplo 1) ---
funcion = lambda x: x**4 - 6*x**3 + 12*x**2 - 10*x + 3
derivada = lambda x: 4*x**3 - 18*x**2 + 24*x - 10
segunda_derivada = lambda x: 12*x**2 - 36*x + 24

# Parámetros del problema
p_inicial = 0.5
tolerancia_error = 0.001 
iteraciones_maximas = 50

# Llamamos a la función
raiz, iteraciones, error_final = newton_modificado(funcion, derivada, segunda_derivada, 
                                                   p_inicial, 
                                                   tolerancia_error, 
                                                   iteraciones_maximas)

# Salida de resultados
if raiz is not None:
    print("\nRESULTADO FINAL:")
    print(f"Raíz aproximada: {raiz:.8f}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Error aproximado final: {error_final:.8f}%")
else:
    print("El método no pudo encontrar la raíz.")