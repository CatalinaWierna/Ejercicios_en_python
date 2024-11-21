"""Tenes dos motores y tres sensores. Los primeros dos sensotes tienen: 10kW y 20kW respectivamente, mientras
que el tercero tiene 30kW. Ambos motores miden 30kW, el primero esta siempre conectado, mientras que el segundo
cuenta con una compuerta que se requeire manejar si es encesario conectarla o no. """
sensor_a = [10,False]
sensor_b = [20,False]
sensor_c = [30,False]
totalWats = 0
motor2 = False

lista_sensores = [sensor_a,sensor_b,sensor_c]


def activarSensor (nro_sensor):
    (lista_sensores[nro_sensor - 1])[1] = True

def activarSegundoMotor(cantWatts):
    if(cantWatts>30):
        return True
    else :
        return False
    
proposicion1 = input("Desea activar el sensor 1? (si para activar)")
proposicion2 = input("Desea activar el sensor 2? (si para activar)")
proposicion3 = input("Desea activar el sensor 3? (si para activar)")

if(proposicion1 == "si"):
    activarSensor(1)
    totalWats += sensor_a[0]
if(proposicion2 == "si"):
    activarSensor(2)
    totalWats += sensor_b[0]
if(proposicion3 == "si"):
    activarSensor(3)
    totalWats += sensor_c[0]

print("Total de Watts: ",totalWats)
if(activarSegundoMotor(totalWats)):
    print("Se necesita usar el segundo motor.")
else:
    print("No se necesita usar el segundo motor.")