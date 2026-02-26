import math
import numpy as np
import matplotlib as plt

#Clasificar sensores como exacto/inexacto y preciso/impreciso y que miden una temperatura constante real de 100.o grados C. Toman 5 lecturas cada uno.
#Exacto / inexacto (basado en la media vs valor real)
#Preciso e impreciso ( basado en la desviación estándar)
sensor_A = [105.1, 104.9, 105.0, 105.2, 104.8]
sensor_B = [100.0, 120.0, 80.0, 110.0, 90.0]
sensor_C = [98.1, 101.5, 99.0, 102.1, 99.5]

media_sensorA=np.mean(sensor_A)
media_sensorB=np.mean(sensor_B)
media_sensorC=np.mean(sensor_C)
print(f"{media_sensorA}")
print(f"{media_sensorB}")
print(f"{media_sensorC}")

desv_est_sensorA = np.std(sensor_A)
desv_est_sensorB = np.std(sensor_B)
desv_est_sensorC = np.std(sensor_C)

#Guardar arrays sensores en una colección, iterar sobre ella y obtener medias y desvuiaciones estandar para imprimir en consola