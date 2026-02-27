#Ejercicio 3: Límites de convergencias
#En este ejercicio utilizaremos la Serie de Maclaurin para:
#f(x) = ln(1+x)
import math
import numpy as np
import matplotlib as plt

def f(x): #Función f(x) = ln(1+x) como método en python
  return np.log(1+x)

def mi_log_natural(x_val,tolerancia):
  base = 0
  iteraciones = 0
  error_aprox = 100
  while error_aprox > tolerancia:
    x = base
    iteraciones+=1
    maclaurin = ((-1)**(iteraciones+1))*(x_val**iteraciones) / iteraciones
    base+=maclaurin
    
    #Cálculo del error aproximado
    if iteraciones > 1: #Condición para evitar que se divida entre 0.
      error_aprox = abs((base-x)/base) * 100
  return base,iteraciones

#Probamos en ln(0.5)
resultado, iter = mi_log_natural(0.5,0.001)
real = f(0.5)
print(f"Aproximación:{resultado:.8f}")
print(f"Valor real: {real:.8f}")
print(f"Iteraciones: {iter}")
