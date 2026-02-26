import math
import numpy as np
import matplotlib as plt

#Clasificar sensores como exacto/inexacto y preciso/impreciso y que miden una temperatura constante real de 100.0 grados C. Toman 5 lecturas cada uno.
#Exacto / inexacto (basado en la media vs valor real)
#Preciso e impreciso ( basado en la desviación estándar)
tempConst = 100.0
sensor_A = [105.1, 104.9, 105.0, 105.2, 104.8]
sensor_B = [100.0, 120.0, 80.0, 110.0, 90.0]
sensor_C = [98.1, 101.5, 99.0, 102.1, 99.5]

def mediaSensor(sensor):
  return np.mean(sensor)

def desvEstSensor(sensor):
  return np.std(sensor)

#Guardar arrays sensores en una colección, iterar sobre ella y obtener medias y desvuiaciones estandar para imprimir en consola
sensores = {"Sensor A":sensor_A, "Sensor B":sensor_B,"Sensor C":sensor_C}

print("Medición de exactitud de los sensores con base en la media de temperatura")
for sensor,temps in sensores.items():
  if mediaSensor(temps)!=tempConst:
    print(f"El {sensor} es inexacto: {mediaSensor(temps)}")
  elif mediaSensor(temps)==tempConst:
     print(f"El {sensor} es exacto: {mediaSensor(temps)}")

print("Medición de precisión de los sensores con base en la desviación estandar de las temperaturas")
for sensor,temps in sensores.items():
  #Utilizamos el coeficiente de variación (desviación / media) * 100 y establecemos un porcentaje para definir nuestra precisión
  #Utilizaremos un porcentaje de 5% para determinar si es preciso o impreciso
  coef_var = (desvEstSensor(temps) / mediaSensor(temps)) * 100
  if coef_var>5:
    print(f"El {sensor} es impreciso: {desvEstSensor(temps)}")
  else:
     print(f"El {sensor} es preciso: {desvEstSensor(temps)}")