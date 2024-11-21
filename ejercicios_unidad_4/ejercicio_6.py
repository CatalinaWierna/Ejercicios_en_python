"""Ejercicio 6 – Dificultad alta
 Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes
componentes:
[3, 44, 21, 78, 5, 56, 9] """

def agregar_lista_ordenado(nro, lista_ordenada):
    if not lista_ordenada or nro < lista_ordenada[0]:
        return [nro] + lista_ordenada
    else:
        aux = lista_ordenada[0]
        lista_ordenada = lista_ordenada[1:]
        return [aux] + agregar_lista_ordenado(nro,lista_ordenada)

def ordenar_lista(lista,lista_ordenada=[]):
    if not lista:
        return lista_ordenada
    else:
        lista_ordenada = agregar_lista_ordenado(lista[0],lista_ordenada)
        return ordenar_lista(lista[1:],lista_ordenada)

lista = [3, 44, 21, 78, 5, 56, 9]
lista = ordenar_lista(lista,lista_ordenada=[])
print(lista)
