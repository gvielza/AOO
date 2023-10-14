import sqlite3

class Conexion:
  def __init__(self,nombre_bd):
    self.nombre_bd=nombre_bd
    self.conexion=sqlite3.connect(nombre_bd)
    self.cursor=self.conexion.cursor()
  def crear_tabla_peliculas(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT,
        duracion INTEGER,
        genero TEXT,
        estudio_animacion TEXT
)  ''')
    self.conexion.commit()
  def agregar_pelicula(self,)
                       
    