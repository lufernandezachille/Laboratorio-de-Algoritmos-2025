class Usuario:
    def __init__(self, nombre, apellido, mail, alias):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.alias = alias
    def describir_usuario(self):
        print(f"El nombre del usuario es {self.nombre} {self.apellido}, su mail es {self.mail} y su alias es {self.alias}.")
    def saludar_usuario(self):
        print(f"Hola, {self.alias}.")

class Administrador(Usuario):
    def __init__(self, nombre, apellido, mail, alias):
        super().__init__(nombre, apellido, mail, alias)  
        self.privilegios = Privilegio()  


class Privilegio() :
    def __init__(self):
        self.privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios"]
    def mostrar_privilegios(self):
        for privilegio in self.privilegios :
            print(f"\n-El administrador {privilegio}")