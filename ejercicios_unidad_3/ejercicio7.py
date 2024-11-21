import pprint
def calcular_precio(producto,lista_productos):
    i = 0
    while lista_productos:
        if(producto==(lista_productos[i])["nombre"]):
            return (lista_productos[i])["precio"]
        lista_productos=lista_productos[1:]

def calcular_total(compra,lista_productos):
    total = 0
    indice = 0
    while compra:
        total += calcular_precio((compra[indice])[0],lista_productos)*(compra[indice])[1]
        compra = compra[1:]
    return total

banana={"nombre":"banana","precio":10,"tipo":"fruta"}
manzana={"nombre":"manzana","precio":15,"tipo":"fruta"}
pera={"nombre":"pera","precio":12,"tipo":"fruta"}
lechuga={"nombre":"lechuga","precio":8,"tipo":"fruta"}
tomate={"nombre":"tomate","precio":15,"tipo":"fruta"}

lista_productos=[banana,manzana,pera,lechuga,tomate]


cliente = input("Ingresar nombre de cliente: (x para terminar) ")
ventas={}

while cliente != "x":
    prod = input("Ingrese producto. Si termino de ingresar ingrese 0 ")
    compra=[]
    while prod != "0" :
        cant = int(input("Ingrese cantidad. "))
        compra.append((prod,cant))
        prod = input("Ingrese producto. Si termino de ingresar ingrese 0 ")
    ventas[cliente] = compra
    print(f"El total de la compra es: {calcular_total(compra,lista_productos)}")
    cliente = input("Ingresar nombre de cliente: (x para terminar) ")

pprint.pprint(ventas)

