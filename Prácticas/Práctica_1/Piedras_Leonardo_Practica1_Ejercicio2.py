#Ejercicio 2: Series de Taylor en tiempo real
# Función f(t) = e^(-t) * cos(2t) 
# Predecir f(0.5), sabiendo que estamos actualmente en t=0
#Implementar en código la Serie de Taylor usando aproximaciones hasta 2do orden

import math
import numpy as np
import matplotlib.pyplot as pit

#Datos
t = 0.5
t0 = 0 
# Paso h = t - ti
h = t - t0

#Función a evaluar
print("Taylor de f(t) = e^(-t) * cos(2t), t = 0.5, t0 = 0")

def f(t): #Función a evaluar mediante series de Taylor
  return np.exp(-t) * np.cos(2*t)


# f(0.5) = e^-0.5 * cos(2*0.5) 
#Derivadas en t0
exp_val = np.exp(-t0) 
f0 = exp_val * (np.cos(2*t0)) #Orden 0: f(0) = e^(-0) · cos(2·(0)) = 1 
f1 = -f0 - 2*np.sin(2*t0) #Orden 1
f2 = (4*exp_val*np.sin(2*t0)) - (3*exp_val*np.cos(2*t0)) #Orden 2

#Términos en la Serie de Taylor
taylor_0 = f0
taylor_1 = f1 * h
taylor_2 = f2 * (h**2) / math.factorial(2)

#Aproximación de Taylor
P0=taylor_0 
P1=P0+taylor_1
P2 = P1 + taylor_2

aproximaciones = [P0,P1,P2]
real = f(t)

#Imprimir resultados
print("\n Orden | Aproximación | Error %")
for i, aprox in enumerate(aproximaciones):
  error = abs((real-aprox) / real) * 100
  print(f"{i} | {aprox:6f} | {error:6f}%" )

#Crear gráfica
t_vals = np.linspace(t0 - 0.2, t + 0.2, 300) #linspace crea un vector

#Función real
y_real = f(t_vals)

#Funciones de Taylor alrededor de x0
y_ord0 = f0 * np.ones_like(t_vals)
y_ord1 = f0 + f1 * (t_vals - t0)
y_ord2 = f0 + f1 * (t_vals - t0) + (f2 / 2) * (t_vals - t0)**2

pit.figure(figsize=(10,6))
pit.plot(t_vals,y_real, 'k-', linewidth = 2.5, label = 'f(t) = e^(-t) * cos(2t)')
pit.plot(t_vals,y_ord0, '--',linewidth = 1.5, label = 'Orden 0')
pit.plot(t_vals,y_ord1, '--',linewidth = 1.5, label = 'Orden 1')
pit.plot(t_vals,y_ord2, '--',linewidth = 1.5, label = 'Orden 2')
pit.plot(t,real, 'ro', markersize = 8, label = 'f(0.5) Valor real')
pit.axvline(x=0.5, color='r', linestyle='--', label ='t=0.5s')
pit.title('Series de Taylor: f(t) = e^(-t) * cos(2t) en torno a t=0', fontsize=16)
pit.xlabel('t(segundos)',fontsize=12)
pit.ylabel('f(t)',fontsize=12)
pit.tight_layout()
pit.legend(fontsize=10,loc='best')
pit.grid()
pit.show()