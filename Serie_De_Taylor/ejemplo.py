import math
import numpy as np
import matplotlib.pyplot as pit

#Datos
x0 = 0.25 #este puede ser a
x = 1.0
h = x - x0 # este es el paso

#Funcion a evaluar
print("Taylor de f(x) = e^(-x), x0=0.25, x= 1.0")

#Derivadas en x0
exp_val = math.exp(-x0)
f0 = exp_val
f1 = -exp_val
f2 =  exp_val
f3 = -exp_val

# Términos de la serie de taylor
taylor_0 = f0
taylor_1 = f1 * h
taylor_2 = f2 * (h**2) / math.factorial(2)
taylor_3 = f3 * (h**3) / math.factorial(3)

#Aproximacion de Taylor
P0 = taylor_0
P1 = P0 + taylor_1
P2 = P1 + taylor_2
P3 = P2 + taylor_3

aproximaciones =[P0,P1,P2,P3]
real = math.exp(-x)

#Imprimir resultados
print("\n Orden | Aproximación | Error %")
for i, aprox in enumerate(aproximaciones):
  error = abs((real-aprox) / real) * 100
  print(f"{i} | {aprox:8f} | {error:8f}%" )