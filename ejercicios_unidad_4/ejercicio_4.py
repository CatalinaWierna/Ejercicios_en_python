# Ejercicio 4: Crea una funcion que tome como parametro una frase y la escriba al reves.

oracion_al_reves_palabras = lambda oracion : ' '.join(oracion.split()[::-1])
oracion_al_reves = lambda oracion : oracion[::-1]

oracion = input("Ingresar oracion: ")


print("La oracion al reves con las palabras al derecho es: ", oracion_al_reves_palabras(oracion))

print("La oracion al reves es: ", oracion_al_reves(oracion))