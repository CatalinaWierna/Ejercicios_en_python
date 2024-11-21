vocales_de_todo_tipo = {"a","e","i","o","u","A","E","I","O","U","á","é","í","ó","ú"}

def aparicion_vocales(vocales_de_todo_tipo,oracion):
    contador =0
    for x in oracion:
        if((set(x) & vocales_de_todo_tipo) != set()):
            contador +=1
    return contador

oracion = input("Ingresar una oracion.")

print(f"En la oracion hay {aparicion_vocales(vocales_de_todo_tipo,oracion)} vocales")