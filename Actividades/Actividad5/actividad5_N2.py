import math
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(f, df, p0, epsilon, N_max):
    # Inicialización
    iteracion = 0
    xr_old = p0
    error = 100.0  # error alto para ver como va disminuyendo
    
    # [NUEVO] Lista para almacenar los datos geométricos de las tangentes
    datos_grafica = []
  
    # Impresión de cabecera de la tabla
    print("Iteración | xn           | f(xn)          | error aproximado (%)")
    print("-" * 75)

    # Ciclo
    while iteracion < N_max:
        iteracion += 1
        
        # Evaluación de la función y su derivada
        f_val = f(xr_old)
        df_val = df(xr_old)

        # Control de excepciones: División por cero (derivada nula)
        if df_val == 0:
            print("ERROR: La derivada es cero, Falla del método")
            return None, iteracion, error, datos_grafica

        # Cálculo de la raíz por Newton-Raphson
        xr = xr_old - (f_val / df_val)

        # [NUEVO] Guardamos el punto actual y el nuevo punto proyectado por la tangente
        datos_grafica.append((xr_old, f_val, xr))

        # Cálculo del error relativo aproximado
        if xr != 0:
            error = abs((xr - xr_old) / xr) * 100
        else:
            error = 0.0
      
        # Impresión de la fila
        print(f"{iteracion:<9} | {xr:<12.6f} | {f_val:<12.6f} | {error:<12.6f}")  
    
        # Verificacion de paro
        if error < epsilon:
            return xr, iteracion, error, datos_grafica
    
        # Actualizamos el valor anterior para la siguiente iteracion
        xr_old = xr

    # Retorna la mejor aproximación si se alcanza N_max
    return xr, iteracion, error, datos_grafica


# ==========================================
# EJECUCIÓN DEL MÉTODO
# ==========================================

# Definimos la función f(x) = cos(x) - x y su derivada
funcion = lambda x: math.log(x) - 1
derivada = lambda x: 1 / x

# Parámetros
p_inicial = 2.5
tolerancia_error = 0.001
iteraciones_maximas = 50

# Llamado a la funcion
raiz, iteraciones, error_final, datos_grafica = newton_raphson(
    funcion, derivada, p_inicial, tolerancia_error, iteraciones_maximas
)

# Salida de resultados
print("-" * 75)
if raiz is not None: 
    print(f"Raíz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Error aproximado final: {error_final:.8f}%")
else:
    print("El método no pudo encontrar la raíz debido a una derivada nula")


# ==========================================
# SECCIÓN DE GRAFICACIÓN
# ==========================================

if raiz is not None:
    # Creamos un rango de valores X alrededor de nuestra raíz y punto inicial
    x_vals = np.linspace(p_inicial - 0.5, raiz + 1.0, 400)
    
    # Vectorizamos la función para que matplotlib la pueda evaluar con arreglos de numpy
    f_vectorizada = np.vectorize(funcion)
    y_vals = f_vectorizada(x_vals)

    plt.figure(figsize=(10, 6))

    # Trazar la función original y el eje X
    plt.plot(x_vals, y_vals, label="f(x) = ln(x) - 1", color='blue', linewidth=2)
    plt.axhline(0, color='black', linewidth=1.2, linestyle='--')

    colores = ['red', 'green', 'orange', 'purple', 'brown', 'cyan']

    # Graficamos las iteraciones (limitamos a 4 para no amontonar las líneas)
    iteraciones_a_graficar = min(len(datos_grafica), 4)

    for i in range(iteraciones_a_graficar):
        xn, f_xn, x_next = datos_grafica[i]
        color = colores[i % len(colores)]
        
        # 1. Línea vertical desde el eje X hasta tocar la curva en f(xn)
        plt.plot([xn, xn], [0, f_xn], color=color, linestyle=':', alpha=0.7)
        
        # 2. Línea tangente desde la curva hasta el nuevo punto en el eje X
        plt.plot([xn, x_next], [f_xn, 0], color=color, linestyle='-', marker='o', 
                 label=f'Iteración {i+1} ')
        
        # 3. Marcamos la nueva aproximación en el eje X
        plt.plot(x_next, 0, marker='x', color=color, markersize=10)
        plt.text(x_next, -0.15, f'x{i+1}', color=color, fontsize=11, ha='center')

    plt.title("Comportamiento del Método de Newton-Raphson", fontsize=15)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()