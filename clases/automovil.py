from abc import ABC, abstractmethod

from clases.vehiculo import Vehiculo
print("Hello")
#definimos clase Automovil
class Automovil(Vehiculo):
  ruedas=4#atributo de la clase
  #construcctor
  def __init__(self,anno, modelo,color,marca,aceleracion):
    super().__init__(anno, modelo)
    self.color=color
    self.marca=marca
    self.aceleracion=aceleracion
    self.velocidad=0
  def acelera(self):
    self.velocidad=self.velocidad+self.aceleracion
  def frena(self):
    self.velocidad=self.velocidad-self.aceleracion
    if(self.velocidad<0):
      self.velocidad=0
  @abstractmethod
  def conducir(self):
    print("Conduciendo el automovil")
    pass
  def datos(self):
    return f"Automovil de {self.ruedas} "
 