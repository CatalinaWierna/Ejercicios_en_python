"""Ejercicio 3:
Cree una funcion lamda que sea equibalente a la sguiente funcion:
def sumar(valor1, valor2):
 res = valor1 + valor2
 return res"""

suma = lambda nro1, nro2: nro1+nro2

a = int (input("Ingresar primer nro:"))
b = int (input("Ingresar segundo nro:"))
print(f"La suma de los numero es {suma(a,b)}")