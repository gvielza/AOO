class Perro:
  def tipo(self):
    return "Mamífero"

class Cocodrilo:
  def tipo(self):
    return "Reptil"

def tipoAnimal(animal):
  return animal.tipo()
animal=Perro()
print(tipoAnimal(animal=animal))



