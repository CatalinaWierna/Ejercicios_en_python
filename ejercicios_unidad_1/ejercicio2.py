"""
Ejercicio 2:
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos. 
"""

import sys

proposicion = int(sys.argv[1])%2==0 and int(sys.argv[2])%2==0 and int(sys.argv[3])%2==0

print("La proposicion: todos los argumentos son pares es:")
print(proposicion)