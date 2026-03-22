import math

def newton_raphson(f,df,p0,epsilon, N_max):
  #Inicialización
  iteracion = 0
  xr_old = p0
  error = 100.0  #error alto para ver como va disminuyendo
  
  #Impresión de cabecera de la tabla
  print("Iteración | xn          | ft(xn)           | error aproximado          ")
  print("-" * 70)

  #Ciclo
  while iteracion < N_max:
    iteracion +=1
    #Evaluación de la función y su derivada
    f_val = f(xr_old)
    df_val = df(xr_old)

    #Control de excepciones: División por cero (derivada nula)
    if df_val == 0:
      print("ERROR: La derivada es cero, Falla del método")
      return None, iteracion, error #Regresamos las variables

    #Cálculo de la raíz por Newton-Raphson
    xr= xr_old - (f_val / df_val)

    #Cálculo del error relativo aproximado
    if xr!=0:
      error = abs((xr - xr_old) / xr) * 100
    else:
      error = 0.0
      
    #Impresión de la fila
    print(f"{iteracion:<9} | {xr:<12.6f} | {f_val:<12.6f} | {error:<12.6f}")  
    
    
    #Verificacion de paro
    if error < epsilon:
      return xr, iteracion, error
    
    #Actualizamos el valor anterior para la siguiente iteracion
    xr_old = xr

  #Retorna la mejor aproximación si se alcanza N_max
  return xr, iteracion, error

#----Ejemplo -----#
funcion = lambda x: math.log(x)-1
derivada = lambda x: 1 / x

#Parámetros
p_inicial = 2.5
tolerancia_error = 0.001
iteraciones_maximas = 50

#Llamado a la funcion
raiz, iteraciones, error_final = newton_raphson(funcion, derivada , p_inicial , tolerancia_error, iteraciones_maximas)

#Salida de resultados
if raiz is not None: 
  print(f"Raíz aproximada {raiz}")
  print(f"Iteraciones realizadas: {iteraciones}")
  print(f"Error aproximado final: {error_final:.8f}")
else:
  print("El método no pudo encontrar la raíz debido a una derivada nula")