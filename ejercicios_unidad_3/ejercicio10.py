"""Ejercicio 10
Escriba un programa que guarde en una variable una contraseña y 
consutle al usuario por la contraseña hasta que esta sea correcta. 
El programa debe informar al usuario si la contraseña fue correcta
o no."""

contrasenia="asmaosif120398"

while True:
    intento=input("Ingresar contrasenia")
    if(intento==contrasenia):
        print("Encontraste la clave.")
        break
    else:
        print("la contrasenia es incorrecta")
        continue