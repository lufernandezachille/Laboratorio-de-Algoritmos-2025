from importar_clases_3_a import Usuario
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