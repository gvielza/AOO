from clases.automovil import Automovil
class AutomovilVolador(Automovil):
  ruedas=6
  def __init__(self,anno,modelo,color,marca,aceleracion,esta_volando=True):
    super().__init__(anno, modelo,color,marca,aceleracion)
    self.esta_volando=esta_volando
  def conducir(self):
    return("conduciendo el automovilVolador")
  