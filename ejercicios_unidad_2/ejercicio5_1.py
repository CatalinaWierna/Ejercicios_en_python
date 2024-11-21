"""Ejercicio 3:
Escriba un programa que solicite el radio de una circunferencia y permita calcular el 
perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio"""

def calcular_perimetro_circunferencia (radio):
    return 2*radio*3.1416

radio = int(input("Ingresar radio del circulo:"))
print("El perimetro es: ",calcular_perimetro_circunferencia(radio))