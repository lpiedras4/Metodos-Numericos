import math

def secante(f, x0, x1, epsilon, N_max):
    # Inicialización
    f0 = f(x0)
    f1 = f(x1)
    #Impresión de cabecera de la tabla
    print("Iteración | xn-1          | xn           | f(xn)          | error aproximado          ")
    print("-" * 70)
    
    
    # Control básico: evitar el caso trivial de misma evaluación
    if f0 == f1:
        raise ValueError("ERROR: f(x0) y f(x1) son iguales, no se puede aplicar la secante.")
    
    iteracion = 0
    xr_old = x1         # último valor de referencia, para calcular el error
                        # puede carcularse a partir de la iteración 2.
                        # o asignar un valor alto ej: 100
    error = 100.0
    
    # Ciclo
    while iteracion < N_max:
        iteracion += 1
        
        # Verificación de denominador para evitar división por cero
        denominador = (f1 - f0)
        if denominador == 0:
            print("ERROR: Denominador igual a cero. Falla del método de la secante.")
            return None, iteracion, error
        
        # Fórmula del método de la secante
        xr = x1 - f1 * (x1 - x0) / denominador
        fr = f(xr)
        
        # Cálculo del error relativo aproximado porcentual
        if xr != 0:
            error = abs((xr - xr_old) / xr) * 100.0
        else:
            error = 0.0

        #Impresión de fila
        print
        
        #Impresión de la fila
        print(f"{iteracion:<9} | {x0:<12.6f} | {x1:<12.6f} | {f1:<12.6f} | {error:<12.6f} ")
        # Verificación de paro
        if error < epsilon:
            return xr, iteracion, error
        
        # Preparación para la siguiente iteración
        x0, f0 = x1, f1
        x1, f1 = xr, fr
        xr_old = xr
    
    # Si se alcanza el máximo de iteraciones, se retorna la mejor aproximación
    return xr, iteracion, error

# --- CASO DE ESTUDIO ---
# Ejemplo: el primero que vimos en clase con bisección
funcion = lambda x: math.log(x)-1

# Parámetros
x_inicial_0 = 2.0
x_inicial_1 = 3.0
tolerancia_error = 0.001  # Error relativo porcentual
iteraciones_maximas = 50

# Llamamos a la función
raiz, iteraciones, error_final = secante(funcion,
                                         x_inicial_0,
                                         x_inicial_1,
                                         tolerancia_error,
                                         iteraciones_maximas)

# Salida de resultados
if raiz is not None:
    print(f"Raíz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Error aproximado final: {error_final:.8f}%")
else:
    print("El método de la secante no pudo encontrar la raíz.")