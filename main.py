from abc import ABC, abstractmethod
print("Hello")
#definimos clase Automovil
class Automovil:
  ruedas=4#atributo de la clase
  #construcctor
  def __init__(self,color,marca,aceleracion):
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
    print("Conduciendo desde el automovil")
    pass


coche1=Automovil("red","Toyota",20)

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

coche2=Automovil("gris","mazda",20)
print(coche2.velocidad)
coche2.frena()
print(coche2.velocidad)
class AutomovilVolador(Automovil):
  ruedas=6
  def __init__(self,color,marca,aceleracion,esta_volando=True):
    super().__init__(color,marca,aceleracion)
    self.esta_volando=esta_volando
  def conducir(self):
    return("conduciendo automovilVolador")
  

automovilvolador1=AutomovilVolador("red","Toyota",20,False)
print(f'el automovil esta o no volando: {automovilvolador1.esta_volando}')
print(coche2.conducir())
print(automovilvolador1.conducir())
  

  