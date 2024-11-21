"""Ejercicio 4
Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido. 
"""
def anios_cumplidos(edad):
    for x in range(1,edad+1):
        print(f"Cumplio {x}")

edad = int(input("Ingresar edad"))
anios_cumplidos(edad)

