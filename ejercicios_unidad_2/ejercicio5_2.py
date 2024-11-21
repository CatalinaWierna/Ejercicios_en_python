"""Ejercicio 4:
Escriba un programa que solicite el radio de una circunferencia y permita calcular el
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
𝐴 = 𝜋. 𝑟ଶ
A = Área
π = Número pi igual a 3.1416
r = Radio 
"""
def calcualar_area_circunferencia(radio):
    return 3.1416*radio**2

radio = int(input("Ingresar radio del circulo: "))

print("El area del circulo es: ",calcualar_area_circunferencia(radio))