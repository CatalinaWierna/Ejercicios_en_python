"""Ejercicio 2 – Dificultad media
Crear una función lambda que sea equivalente a la siguiente función:
def multiplicar_por_tres(valor):
 res = 3 * valor
 return res """

triple = lambda valor : valor*3

nro = int(input("Ingresar nro:"))

print(f"El triple del nro es: {triple(nro)}")