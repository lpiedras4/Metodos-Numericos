import math
import numpy as np
import matplotlib.pyplot as pit

# math.log --> función logarítmica en python
#Datos
x0 = 1
x = 1.1
h = x - x0 

#Derivadas en x0
f0 = 0
f1 = 1
f2 = -1

#Términos en la serie de taylor
taylor_0 = f0
taylor_1 = f1 * h
taylor_2 = f2 * (h**2) / math.factorial(2)

#Aproximacion de Taylor
P0 = taylor_0
P1 = P0 + taylor_1
P2 = P1 + taylor_2

aproximaciones =[P0,P1,P2]
real = math.log(x)

#Imprimir resultados
print("\n Orden | Aproximación | Error %")
for i, aprox in enumerate(aproximaciones):
  error = abs((real-aprox) / real) * 100
  print(f"{i} | {aprox:8f} | {error:8f}%" )

  #Crear gráfica
  x_vals = np.linspace(x0 - 0.2, x + 0.2, 300) #linspace crea un vector

  #Función real
  y_real = np.log(x_vals)

  #Funciones de Taylor alrededor de x0
  y_ord0 = f0 * np.ones_like(x_vals)
  y_ord1 = f0 + f1 * (x_vals - x0)
  y_ord2 = f0 + f1 * (x_vals - x0) + (f2 / 2) * (x_vals - x0)**2

pit.figure(figsize=(10,6))
pit.plot(x_vals,y_real, 'k-', linewidth = 2.5, label = 'f(x) = e^(-x)')
pit.plot(x_vals,y_ord0, '--',linewidth = 1.5, label = 'Orden 0')
pit.plot(x_vals,y_ord1, '--',linewidth = 1.5, label = 'Orden 1')
pit.plot(x_vals,y_ord2, '--',linewidth = 1.5, label = 'Orden 2')

#Marcar punto de exapnsion y punto de evaluación
pit.plot(x0,math.log(x0), 'ro', markersize = 8,
         label = f'x0={x0}')
pit.plot(x,real,'go', markersize = 8,
         label = f'x={x}')
pit.xlabel('x',fontsize=12)
pit.ylabel('y',fontsize=12)
pit.title('Series de Taylor: f(x) = lin-x) centrada en x0 = 1', fontsize=16)
pit.legend(fontsize=10,loc='best')
pit.grid(True, alpha=0.3) # agrega cuadros a la gráfica
pit.axvline(x=x0, color = 'red' , linestyle = ':', alpha = 0.5) #agrega lineas verticales
pit.axvline(x=x, color = 'green' , linestyle = ':', alpha = 0.5)
pit.tight_layout()
pit.show()