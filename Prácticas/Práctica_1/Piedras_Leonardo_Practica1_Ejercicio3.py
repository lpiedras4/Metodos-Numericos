
import math
import numpy as np
import matplotlib as plt

#Ejercicio 3: Límites de convergencias
#En este ejercicio utilizaremos la Serie de Maclaurin para:
#Función f(x) = ln(1+x)

def mi_log_natural(x_val,tolerancia):
  base = 0
  iteraciones = 0
  error_aprox = 100
  while error_aprox > tolerancia: #Mientras el error aproximado sea mayor que la tolerancia, agregamos términos
    iteraciones+=1
    x = base
    maclaurin = ((-1)**(iteraciones+1)) * (x_val**iteraciones) / iteraciones
    base+=maclaurin
    
    #Cálculo del error aproximado
    if iteraciones > 1: #Condición para evitar que se divida entre 0.
      error_aprox = abs((base-x)/base) * 100
  return base,iteraciones

#Evaluación en ln(1.5)
resultado, iter = mi_log_natural(0.5,0.001)
real = np.log(1.5)
print(f"Aproximación:{resultado:.8f}")
print(f"Valor real: {real:.8f}")
print(f"Iteraciones: {iter}")

#Evaluación  en ln(3.0)
resultado, iter = mi_log_natural(2,0.001)
real = np.log(3)
print(f"Aproximación: {resultado:.8f}")
print(f"Valor real:   {real:.8f}")
print(f"Iteraciones: {iter}")