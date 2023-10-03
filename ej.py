class Ejemplo:
  __atributo_privado = "Soy un atributo inalcanzable desde fuera."
  atribut_publico="soy publico"

  def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

  def atributo_publico(self):
        return self.__atributo_privado

  def metodo_publico(self):
      return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()
class Otra:
  atributo=1
  e1=Ejemplo()
  print(e1.atributo_publico)
  print(e1.metodo_publico)
  print(e1.atributo_publico)
  print(e1.atribut_publico)