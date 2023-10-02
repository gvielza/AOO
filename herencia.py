from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def sonido(self):
        return "¡Miau!"

# Creando instancias de Perro y Gato
perro = Perro()
gato = Gato()

print("El perro hace: " + perro.sonido())
print("El gato hace: " + gato.sonido())
