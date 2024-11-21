"""Ejercicio 5:
Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
editor el valor incrementado en un 10%."""

def calcular_porcentaje(porcentaje,nro):
    return nro*0.01*porcentaje

nro = int(input("Ingresar un numero: "))

porcentaje = 10

print("El ",porcentaje," porciento de: ", nro," es: ",calcular_porcentaje(porcentaje,nro))