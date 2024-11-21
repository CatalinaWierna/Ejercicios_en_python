"""Ejercicio 4
Realice un programa que consulte la edad y en caso de que el valor ingresado supere
la fecha de jubilacion, presente en la terminal el mensaje "Ya esta en edade de jubilarse" en 
caso contrario que presente "Aun esta en edad de trabajar"
"""

def analizar_jubilacion (edad):
    if(edad>60):
        return "Ya esta en edad de jubilarse."
    else:
        return "Aun esta en edad de trabajar."
    
edad=int(input("Ingrese su edad: "))

print(analizar_jubilacion(edad))