import numpy as np
import matplotlib.pyplot as plt

# Caso de estudio: Queremos la derivada de f(x) = x^2 en x = 2.
# Sabemos por cálculo que la analítica es f'(x) = 2x -> f'(2) = 4.

def f(x):
    return x**2

def derivada_analitica(x):
    return 2*x

# Método Numérico: Diferencias Finitas (Aproximación de la pendiente)
# Fórmula: f'(x) ≈ (f(x+h) - f(x)) / h
def derivada_numerica(x, h):
    return (f(x + h) - f(x)) / h

val_x = 1
val_real = derivada_analitica(val_x)

# Probemos con diferentes tamaños de paso (h) para ver el error
pasos_h = [20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.1, 0.01, 1e-5, 1e-16] # Ojo con el último

print(f"{'h (Paso)':<15} | {'Aprox. Numérica':<20} | {'Error Absoluto':<20}")
print("-" * 60)

errores = []
h_vals = []

for h in pasos_h:
    val_aprox = derivada_numerica(val_x, h)
    error = abs(val_real - val_aprox)
    
    # Guardamos para graficar (ignorando el último caso extremo para el plot)
    if h > 1e-15:
        errores.append(error)
        h_vals.append(h)
        
    print(f"{h:<15.1e} | {val_aprox:<20.10f} | {error:<20.10f}")

# Visualización del error disminuyendo con h
plt.figure(figsize=(8, 5))
plt.loglog(h_vals, errores, marker='o', linestyle='--')
plt.title("Convergencia: El error disminuye al reducir el paso h")
plt.xlabel("Tamaño del paso (h)")
plt.ylabel("Error Absoluto")
plt.grid(True, which="both", ls="-")
plt.show()
