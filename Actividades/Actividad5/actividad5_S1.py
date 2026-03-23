import math
import numpy as np
import matplotlib.pyplot as plt

def secante(f, x0, x1, epsilon, N_max):
    # Inicialización
    f0 = f(x0)
    f1 = f(x1)
    
    # [NUEVO] Lista para almacenar los datos geométricos de las secantes
    datos_grafica = []
    
    # Impresión de cabecera de la tabla
    print("Iteración | xn-1         | xn           | f(xn)        | error aprox (%)")
    print("-" * 75)
    
    # Control básico: evitar el caso trivial de misma evaluación
    if f0 == f1:
        raise ValueError("ERROR: f(x0) y f(x1) son iguales, no se puede aplicar la secante.")
    
    iteracion = 0
    xr_old = x1  # último valor de referencia, para calcular el error
    error = 100.0
    
    # Ciclo
    while iteracion < N_max:
        iteracion += 1
        
        # Verificación de denominador para evitar división por cero
        denominador = (f1 - f0)
        if denominador == 0:
            print("ERROR: Denominador igual a cero. Falla del método de la secante.")
            return None, iteracion, error, datos_grafica
        
        # Fórmula del método de la secante
        xr = x1 - f1 * (x1 - x0) / denominador
        fr = f(xr)
        
        # [NUEVO] Guardamos los puntos que forman la secante y el nuevo cruce xr
        datos_grafica.append(((x0, f0), (x1, f1), xr))
        
        # Cálculo del error relativo aproximado porcentual
        if xr != 0:
            error = abs((xr - xr_old) / xr) * 100.0
        else:
            error = 0.0

        # Impresión de la fila
        print(f"{iteracion:<9} | {x0:<12.6f} | {x1:<12.6f} | {f1:<12.6f} | {error:<12.6f}")
        
        # Verificación de paro
        if error < epsilon:
            return xr, iteracion, error, datos_grafica
        
        # Preparación para la siguiente iteración
        x0, f0 = x1, f1
        x1, f1 = xr, fr
        xr_old = xr
    
    # Si se alcanza el máximo de iteraciones, se retorna la mejor aproximación
    return xr, iteracion, error, datos_grafica


# ==========================================
# EJECUCIÓN DEL MÉTODO
# ==========================================

# Ejemplo: el primero que vimos en clase con bisección
funcion = lambda x: math.cos(x) - x

# Parámetros
x_inicial_0 = 0.0
x_inicial_1 = 1.0
tolerancia_error = 0.001  # Error relativo porcentual
iteraciones_maximas = 50

# Llamamos a la función
raiz, iteraciones, error_final, datos_grafica = secante(
    funcion, x_inicial_0, x_inicial_1, tolerancia_error, iteraciones_maximas
)

# Salida de resultados
print("-" * 75)
if raiz is not None:
    print(f"Raíz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Error aproximado final: {error_final:.8f}%")
else:
    print("El método de la secante no pudo encontrar la raíz.")


# ==========================================
# SECCIÓN DE GRAFICACIÓN
# ==========================================

if raiz is not None:
    # Rango de X para abarcar los puntos iniciales y la raíz
    x_min = min(x_inicial_0, x_inicial_1, raiz) - 0.2
    x_max = max(x_inicial_0, x_inicial_1, raiz) + 0.2
    x_vals = np.linspace(x_min, x_max, 400)
    
    # Vectorizamos la función
    f_vectorizada = np.vectorize(funcion)
    y_vals = f_vectorizada(x_vals)

    plt.figure(figsize=(10, 6))

    # Trazar la función original y el eje X
    plt.plot(x_vals, y_vals, label="f(x) = cos(x) - x", color='blue', linewidth=2)
    plt.axhline(0, color='black', linewidth=1.2, linestyle='--')

    colores = ['red', 'green', 'orange', 'purple', 'brown', 'cyan']

    # Limitamos a 4 iteraciones para no saturar la gráfica
    iteraciones_a_graficar = min(len(datos_grafica), 4)

    for i in range(iteraciones_a_graficar):
        (p_x0, p_f0), (p_x1, p_f1), p_xr = datos_grafica[i]
        color = colores[i % len(colores)]
        
        # 1. Líneas verticales de referencia hacia la curva
        plt.plot([p_x0, p_x0], [0, p_f0], color='gray', linestyle=':', alpha=0.5)
        plt.plot([p_x1, p_x1], [0, p_f1], color='gray', linestyle=':', alpha=0.5)
        
        # 2. Línea secante que cruza por (x0, f0), (x1, f1) y el eje X en xr
        plt.plot([p_x0, p_x1, p_xr], [p_f0, p_f1, 0], color=color, linestyle='-', marker='o', 
                 label=f'Iteración {i+1} (Secante)')
        
        # 3. Marcar la nueva aproximación xr
        plt.plot(p_xr, 0, marker='x', color=color, markersize=10)
        plt.text(p_xr, -0.15, f'xr{i+1}', color=color, fontsize=11, ha='center')

    plt.title("Comportamiento del Método de la Secante", fontsize=15)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()