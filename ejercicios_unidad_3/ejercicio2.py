"""Ejercicio 2
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. 
"""
def apariciones_de_letra (letra, oracion):
    contador = 0
    for x in oracion:
        if(x==letra):
            contador += 1
    return contador

oracion = input("Ingresar Oracion: ") 

print(f"La letra aparece {apariciones_de_letra("a",oracion)} veces.")