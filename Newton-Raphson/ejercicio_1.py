def newton_raphson(f,df,p0,epsilon, N_max):
  #Inicialización
  iteracion = 0
  xr_old = p0
  error = 100.0  #error alto para ver como va disminuyendo

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
    
    #Verificacion de paro
    if error < epsilon:
      return xr, iteracion, error
    
    #Actualizamos el valor anterior para la siguiente iteracion
    xr_old = xr

  #Retorna la mejor aproximación si se alcanza N_max
  return xr, iteracion, error

#----Ejemplo -----#
funcion = lambda x: x**4 - 6*x**3 + 12*x**2 - 10*x + 3
derivada = lambda x:4*x**3 - 18*x**2 + 24*x - 10

#Parámetros
p_inicial = 0.5
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