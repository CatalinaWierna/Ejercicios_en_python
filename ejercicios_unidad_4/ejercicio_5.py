"""Ejercicio 5 – Dificultad media
Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo.
1, 2, 3, 4, 5
Y
5, 4, 3, 2, 1"""
menor_a_mayor = []
mayor_a_menor = []
def anios_cumplidos (edad,i=1):
    if(edad == 0):
        print(",".join(menor_a_mayor))
        print("Y")
        print(",".join(mayor_a_menor))
        return
    else:
       menor_a_mayor.append(str(edad-(edad-i)))
       mayor_a_menor.append(str(edad))
       edad -= 1
       i += 1
       anios_cumplidos(edad,i) 
        
edad = int(input("Ingresar Edad"))
anios_cumplidos(edad)