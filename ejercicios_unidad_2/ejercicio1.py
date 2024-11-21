"""Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos. Utilice la estructura if/else"""
import sys
def esPar (nro):
    return not nro%2

def mostrarSiEsPar (nro,indice):
    if(esPar(nro)):
        print("El numero ",indice," ingresado es par.")
    else :
        print("El numero ",indice," ingresado es impar.")


mostrarSiEsPar(int(sys.argv[1]),1)
mostrarSiEsPar(int(sys.argv[2]),2)
mostrarSiEsPar(int(sys.argv[3]),3)

