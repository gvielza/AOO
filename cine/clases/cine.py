#Cine (nombre, direccion) y una lista programacion con las películas que se le irán agregando
class Cine:
  def __init__(self,nombre,direccion):
    self.nombre=nombre
    self.direccion=direccion
    self.programacion=[]
  def agregar_pelicula(self,pelicula):
    self.programacion.append(pelicula)
    
  