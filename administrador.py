from usuario import Usuario

# Herencia: Administrador es otro tipo especializado de Usuario.
class Administrador(Usuario):
    def __init__(self, nombre: str, correo: str, permisos: list):
        super().__init__(nombre, correo)
        self.permisos = permisos

    # Polimorfismo: El mismo método que en Cliente, pero con comportamiento distinto.
    def mostrar_info(self):
        permisos_str = ", ".join(self.permisos)
        return f"Administrador: {self.nombre}, Permisos: [{permisos_str}]"