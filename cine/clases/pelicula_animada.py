#PeliculaAnimada (titulo, duracion, genero, estudio_animacion)
from pelicula import Pelicula
class PeliculaAnimada(Pelicula):
  def __init__(self,titulo, duracion,genero,estudio_animacion):
    super().__init__(titulo,duracion,genero)
    self.estudio_animacion=estudio_animacion