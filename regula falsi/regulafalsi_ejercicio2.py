import math
import numpy as np
import matplotlib as plt

def falsa_posicion(f, a, b, epsilon,N_max):
    #Inicialización
    fa= f(a)
    fb = f(b)
    
    if fa*fb > 0:
        raise ValueError("ERROR: La función no tiene raíz en este intervalo")

    iteracion = 0
    xr_old = a
    error = 100.0
    
    #Ciclo
    while iteracion < N_max:
        iteracion+=1
        
        #Cálculo del punto medio
        xr = b -((fb * (a-b)) / (fa-fb)) #Forzamos a python a que identifique que xr es un flotante
        fr = f(xr)  
        
        #Prueba de signo
        if fa * fr < 0:
            b = xr
            fb = fr
        elif fa * fr > 0:
            a = xr
            fa = fr
        else:
            #fa * fr = 0 significa que encontramos la ríz exacta
            return xr,iteracion,0.0
        
        #Cálculo del error aproximado
        error = (abs((xr - xr_old) / xr)) *100
        #Verificación de paro
        if error < epsilon:
            return xr, iteracion,error
        
        #Actualizamos el valor anterior paras la siguiente iteración
        xr_old = xr
        
    #Salida
    # Si el ciclo termina sin alcanzar la tolerancia (epsilon)
    #Retorna la mejor aproximación
    return xr, iteracion, error


#Definimos la función f(x) = cos(x) - x
funcion = lambda x:math.cos(x)-x

#Parámetros
a = 0.5
b = math.pi/4 #0.785398
tolerancia_error = 0.001 #Error relativo
iteraciones_maximas = 50

#Llamamos a la función
raiz,iteraciones,error_final = falsa_posicion(funcion,a,b,tolerancia_error,iteraciones_maximas)

if raiz is not None:
    print(f"Raiz aproximada: {raiz}")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Error aproximado final: {error_final:.4f}%") # para imprimir 4 decimales
else:
    print("No hay raíz, intenta con un intervalo [a,b] diferente.")    
    
