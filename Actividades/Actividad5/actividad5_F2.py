import math
import numpy as np
import matplotlib.pyplot as plt

def falsa_posicion(f, a, b, epsilon, N_max):
    # Inicialización
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError("ERROR: La función no tiene raíz en este intervalo")

    iteracion = 0
    xr_old = a
    error = 100.0
    
    # [NUEVO] Lista para almacenar los datos geométricos de cada iteración
    datos_grafica = []
    
    # Imprimir encabezado de la tabla
    print("Iteración | a            | b            | xr         | fr         | Error (%)")
    print("-" * 75)  
    
    # Ciclo
    while iteracion < N_max:
        iteracion += 1
        
        # Cálculo del punto medio
        xr = b - ((fb * (a-b)) / (fa-fb)) # Forzamos a python a que identifique que xr es un flotante
        fr = f(xr)  
        
        # [NUEVO] Guardamos las coordenadas de la secante actual ANTES de actualizar a o b
        datos_grafica.append(((a, fa), (b, fb), xr))
        
        # Cálculo del error aproximado
        if xr != 0:
            error = (abs((xr - xr_old) / xr)) * 100
            
        # Impresión de fila (usamos las a y b que generaron este xr)
        print(f"{iteracion:<9} | {a:<12.6f} | {b:<12.6f} | {xr:<10.6f} | {fr:<10.6f} | {error:<10.6f}")
        
        # Prueba de signo
        if fa * fr < 0:
            b = xr
            fb = fr
        elif fa * fr > 0:
            a = xr
            fa = fr
        else:
            # fa * fr = 0 significa que encontramos la raíz exacta
            return xr, iteracion, 0.0, datos_grafica
        
        # Verificación de paro
        if error < epsilon:
            return xr, iteracion, error, datos_grafica
        
        # Actualizamos el valor anterior paras la siguiente iteración
        xr_old = xr
        
    # Salida si el ciclo termina sin alcanzar la tolerancia (epsilon)
    return xr, iteracion, error, datos_grafica

# ==========================================
# EJECUCIÓN DEL MÉTODO
# ==========================================

# Definimos la función f(x) = cos(x) - x
funcion = lambda x: math.log(x) - 1

# Parámetros
a_inicial = 2.0
b_inicial = 3.0
tolerancia_error = 0.001 # Error relativo en porcentaje
iteraciones_maximas = 50

# Llamamos a la función (ahora también nos devuelve los datos para graficar)
raiz, iteraciones, error_final, datos_grafica = falsa_posicion(
    funcion, a_inicial, b_inicial, tolerancia_error, iteraciones_maximas
)

if raiz is not None:
    print("-" * 75)
    print(f"Raíz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Error aproximado final: {error_final:.4f}%\n") 
else:
    print("No hay raíz, intenta con un intervalo [a,b] diferente.")    

# ==========================================
# SECCIÓN DE GRAFICACIÓN
# ==========================================

# Para graficar la curva suave, evaluamos la función en muchos puntos

x_vals = np.linspace(a_inicial - 0.2, b_inicial + 0.2, 400)
f_vectorizada = np.vectorize(funcion)
y_vals = f_vectorizada(x_vals)

plt.figure(figsize=(10, 6))

# Trazar la función y el eje X
plt.plot(x_vals, y_vals, label="f(x) = ln(x) - 1", color='blue', linewidth=2)
plt.axhline(0, color='black', linewidth=1.2, linestyle='--')

colores = ['red', 'green', 'orange', 'purple', 'brown', 'cyan', 'magenta']

# Limitamos a graficar solo las primeras 4 iteraciones para no saturar la imagen
iteraciones_a_graficar = min(len(datos_grafica), 4)

for i in range(iteraciones_a_graficar):
    (a, fa), (b, fb), xr = datos_grafica[i]
    color = colores[i % len(colores)]
    
    # Línea Secante
    plt.plot([a, b], [fa, fb], color=color, linestyle='-', marker='o', label=f'Iteración {i+1}')
    
    # Línea vertical hacia la nueva raíz aproximada xr
    plt.plot([xr, xr], [0, funcion(xr)], color=color, linestyle=':')
    plt.plot(xr, 0, marker='x', color=color, markersize=10)
    plt.text(xr, -0.15, f'xr{i+1}', color=color, fontsize=11, ha='center')

plt.title("Comportamiento del Método de Falsa Posición", fontsize=15)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()