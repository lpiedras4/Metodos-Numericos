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

  #Crear gráfica
  x_vals = np.linspace(x0 - 0.2, x + 0.2, 300) #linspace crea un vector

  #Función real
  y_real = np.exp(-x_vals)

  #Funciones de Taylor alrededor de x0
  y_ord0 = f0 * np.ones_like(x_vals)
  y_ord1 = f0 + f1 * (x_vals - x0)
  y_ord2 = f0 + f1 * (x_vals - x0) + (f2 / 2) * (x_vals - x0)**2
  y_ord3 = f0 + f1 * (x_vals - x0) + (f2 / 2) * (x_vals - x0)**2 + (f3 / 6) * (x_vals - x0)**3

pit.figure(figsize=(10,6))
pit.plot(x_vals,y_real, 'k-', linewidth = 2.5, label = 'f(x) = e^(-x)')
pit.plot(x_vals,y_ord0, '--',linewidth = 1.5, label = 'Orden 0')
pit.plot(x_vals,y_ord1, '--',linewidth = 1.5, label = 'Orden 1')
pit.plot(x_vals,y_ord2, '--',linewidth = 1.5, label = 'Orden 2')
pit.plot(x_vals,y_ord3, '--',linewidth = 1.5, label = 'Orden 3')
pit.legend()
pit.show()