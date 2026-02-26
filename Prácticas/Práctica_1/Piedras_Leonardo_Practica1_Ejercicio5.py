#Ejecutar siguiente código en mi máquina para encontrar el error epsilon de mi sistema
import math 
import numpy as np
import matplotlib as plt
import sys

epsilon = 1.0
while (1.0 + epsilon) > 1.0:
    epsilon = epsilon / 2.0
epsilon = epsilon * 2.0
#Imprimimos resultados del épsilon máquina y épsilon oficial de Python
print(f"El épsilon de mi máquina es: {epsilon}")
print(f"Épsilon oficial de Python: {sys.float_info.epsilon}")