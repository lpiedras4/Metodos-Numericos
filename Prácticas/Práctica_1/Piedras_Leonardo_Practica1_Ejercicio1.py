import numpy as np
import matplotlib.pyplot as plt
#Caso de estudio: Calcular la derivada numérica de f(x) = x^4 evaluada en x = 1
# Por cálculo, la solución analítica es f'(x) = 4x^3 -> f'(1) = 4

def f(x):
    return x**4

def derivada_analitica(x): 
    return 4*x**3

# Método Numérico: Fórmula de diferencias finitas (Aproximación de la pendiente)
# Fórmula: f'(x) ≈ (f(x+h) - f(x)) / h

def derivada_numerica(x,h):
    return (f(x + h) - f(x)) / h

val_x = 1
val_real = derivada_analitica(val_x)

h = 10**-1 #Inicializamos h en 10**-1
pasos_h = []
while h>=1e-18: #Creamos un ciclo que guarde los pasos de h divididos entre 10 hasta 1e-18
    h/=10
    pasos_h.append(h)


print(f"{'h (Paso)':<15} | {'Aprox. Numérica':<20} | {'Error Absoluto':<20}")
print("-" * 60)

#Creamos lista para almacenar errores y valores de paso h para graficar y mostrar en la tabla
errores = []
h_vals =[]

for h in pasos_h:
    val_aprox=derivada_numerica(val_x,h)
    error = abs(val_real - val_aprox)

    # Guardamos para graficar (ignorando el último caso extremo para el plot)
    if h > 1e-18:
        errores.append(error)
        h_vals.append(h)
 
    print(f"{h:<15.1e} | {val_aprox:<20.10f} | {error:<20.10f}")

h_vals = np.array(h_vals)
errores = np.array(errores)

#Error teórico de f(x) = x^4 en x = 1
# f''(x) = 12x^2
# f''(1) = 2 
# h / 2 (f´´(1))
C = 6
error_teorico = h_vals * 6
# Visualización del error disminuyendo con h
plt.figure(figsize=(8, 5))
plt.loglog(h_vals, errores, marker='o', linestyle='-', color = 'green', label='Error observado')
plt.loglog(h_vals,error_teorico,marker='o',linestyle='--', color = 'black', label = ' Error teórico')
plt.title("Convergencia: El error disminuye al reducir el paso h")
plt.xlabel("Tamaño del paso (h)")
plt.ylabel("Error Absoluto")
plt.grid(True, which="both", ls="-")
plt.legend()
plt.show()
    