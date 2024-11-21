#Ejercicio 1: Crear una funcion lamda que compreube si un numero es par o impar

esPar = lambda nro : nro % 2 == 0 

numero = int(input("Ingresar Nro:"))

if (esPar(numero)):
    print(f"El numero {numero} es par")
else :
    print(f"El numero {numero} es impar")
