class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre_restaurante} Y la cocina es {self.tipo_cocina}.")
    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto.")