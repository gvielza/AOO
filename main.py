from clases.automovil import Automovil
from clases.automovilVolador import AutomovilVolador
from clases.vehiculo import Vehiculo



coche1=Automovil(2019,"Corolla","red","Toyota",20)

print(coche1.ruedas)
print(coche1.aceleracion)
coche1.aceleracion=30
print(coche1.aceleracion)
coche1.acelera()
print(coche1.velocidad)
coche1.acelera()
print(coche1.velocidad)
coche1.aceleracion=50
coche1.acelera()
print(coche1.velocidad)
coche1.ruedas=5
print(coche1.ruedas)
coche1.frena()
print(coche1.aceleracion)

coche2=Automovil(2020,"ES","gris","mazda",20)
print(coche2.velocidad)
coche2.frena()
print(coche2.velocidad)


automovilvolador1=AutomovilVolador("red","Toyota",20,False)
print(f'el automovil esta o no volando: {automovilvolador1.esta_volando}')
print(coche2.conducir())
print(automovilvolador1.conducir())
print("\n")
print("***********Clase #13***********")
veh1=Vehiculo(2018,"B15")

print(f"el año del vehiculo es {veh1.get_anno()}")
print(f"el año del vehiculo es {veh1._anno}")
print(f"el modelo del vehiculo es {veh1.get_modelo()}")
print(f"el modelo del vehiculo es {veh1.__modelo}")
#actualizar año
veh1.set_anno(2020)

print(f"el año del vehiculo es {veh1.get_anno()}")
print(f"el modelo del vehiculo es {veh1.get_modelo()}")
veh1.set_modelo("Corolla")
print(f"el modelo del vehiculo es {veh1.get_modelo()}")
