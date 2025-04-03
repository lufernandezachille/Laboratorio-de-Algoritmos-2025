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
