from clases.automovil import Automovil
from clases.automovilVolador import AutomovilVolador
from clases.vehiculo import Vehiculo
import sqlite3 as sql
from base_datos.conexion import Conexion 

coche1=Automovil(2019,"Corolla","red","Toyota",20)

coche2=Automovil(2020,"ES","gris","mazda",20)

coche2.frena()


automovilvolador1=AutomovilVolador(2020,"blanco","red","Toyota",20,False)
print(f'el automovil esta o no volando: {automovilvolador1.esta_volando}')
print(coche2.conducir())
print(automovilvolador1.conducir())
print("***********Clase #13***********")
veh1=Vehiculo(2018,"B15")

print(f"el año del vehiculo es {veh1.get_anno()}")
print(f"el año del vehiculo es {veh1._anno}")
print(f"el modelo del vehiculo es {veh1.get_modelo()}")
#print(f"el modelo del vehiculo es {veh1.__modelo}")
#actualizar año
veh1.set_anno(2020)

print(f"el año del vehiculo es {veh1.get_anno()}")
print(f"el modelo del vehiculo es {veh1.get_modelo()}")
veh1.set_modelo("Corolla")
print(f"el modelo del vehiculo es {veh1.get_modelo()}")
print("**********Clase14******")
auto=Automovil(2020,"ES","gris","mazda",20)
print(auto._anno)
print(auto.get_modelo())
autovolador=AutomovilVolador(2023,"A3","blanco","AUDi",50)
#print(autovolador.__modelo)
print(autovolador.get_modelo())
autovolador.set_modelo("A4")
print(autovolador.get_modelo())

print(auto.datos())
print(autovolador.datos())

def datos_veh(auto):
  return auto.datos()

auto_dato=Automovil(2002,"Punto","verde","Fiat",10)


#comentar control+/
print(datos_veh(auto_dato))
print("**************BD********")
conexion1=sql.connect("base_datos/mi_bd.db")
cursor=conexion1.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Anno INTEGER,
modelo TEXT
)'''
)
conexion1.commit()
cursor.execute('''SELECT * FROM vehiculos''')
vehiculos=cursor.fetchall()
for vehiculo in vehiculos:
  print(vehiculo)
cursor.close()
conexion1.close()
print("\n"+"***************Desde archivo externo"+"\n")
bd="mi_bd.db"
conexion=Conexion(bd)



conexion.crear_tabla()
#conexion.agregar_vehiculo(2010,"AR")
# Obtener todos los resultados de la consulta
conexion.eliminar(str(3))
conexion.modificar_vehiculos(2010,"Audi",str(1))
resultados = conexion.listar_clientes()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.cerrar_bd()




