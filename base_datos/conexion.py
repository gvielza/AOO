import sqlite3
class Conexion:
  def __init__(self, nombreBD):
    self.nombreBD = nombreBD
    self.conexion = sqlite3.connect(nombreBD)
    self.cursor = self.conexion.cursor()
  
  def listar_clientes(self):
    self.cursor.execute('''SELECT * FROM vehiculos2''')
    vehiculos=self.cursor.fetchall()
    return vehiculos
  def crear_tabla(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculos2(
id INTEGER PRIMARY KEY AUTOINCREMENT,
anno INTEGER ,
modelo TEXT
)  ''')
    self.conexion.commit()
  def agregar_vehiculo(self,anno,modelo):
    self.cursor.execute('''INSERT INTO vehiculos2(anno, modelo)VALUES(?,?)''',(anno,modelo))
    self.conexion.commit()

  def cerrar_bd(self):
    self.cursor.close()
    self.conexion.close()
  def modificar_vehiculos(self,anno,modelo,id):
    self.cursor.execute('''UPDATE vehiculos2 set anno=?, modelo=? WHERE id=?''',(anno,modelo,id))
    self.conexion.commit()
  def eliminar(self,id):
    self.cursor.execute('''DELETE FROM vehiculos2 WHERE id=?''',(id))
    self.conexion.commit()

