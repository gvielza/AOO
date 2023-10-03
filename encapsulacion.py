class MiClase:
    def __init__(self):
        self.__atributo_privado = 42  # Atributo privado

    def metodo_publico(self):
        print("Este es un método público")

    def __metodo_privado(self):
        print("Este es un método privado")

    def acceder_privado(self):
        self.__metodo_privado()  # Acceder a un método privado desde uno público
        return self.__atributo_privado  # Acceder a un atributo privado desde uno público


objeto = MiClase()

# Acceso a un método público
objeto.metodo_publico()  # Salida: Este es un método público

# Acceso a un método privado desde un método público
objeto.acceder_privado()  # Salida: Este es un método privado

# Intento de acceso a un atributo privado desde fuera de la clase (esto generará un error)
print(objeto.__atributo_privado)  # Generará un error

# Intento de acceso a un método privado desde fuera de la clase (esto generará un error)
objeto.__metodo_privado()  # Generará un error
