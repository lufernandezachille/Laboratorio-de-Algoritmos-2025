class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.sabores = ["vainilla", "chocolate", "dulce de leche", "limon"]
    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre_restaurante} Y la cocina es {self.tipo_cocina}.")
    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto.")

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina):
        super().__init__(nombre_restaurante, tipo_cocina)
    def mostrar_sabores(self):
        for sabor in self.sabores :
            print(f"\n-{sabor}")

puesto_de_helados = PuestoDeHelados('freddo', 'italiana')
print(puesto_de_helados.describir_restaurante())
puesto_de_helados.mostrar_sabores()
