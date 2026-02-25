#Ejercicio 2: Series de Taylor en tiempo real
# Función f(t) = e^(-t) * cos(2t) 
# Predecir f(0.5), sabiendo que estamos actualmente en t=0
#Implementar en código la Serie de Taylor usando aproximaciones hasta 2do orden

import math
import numpy as np
import matplotlib as pit

#Datos
t = 0.5
t0 = 0 
# Paso h = t - ti
h = t - t0

#Función a evaluar
print("Taylor de f(t) = e^(-t) * cos(2t), t = 0.5, t0 = 0")

#Derivadas en t0

