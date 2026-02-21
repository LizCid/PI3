from usuario import Usuario

# Herencia: Cliente extiende la funcionalidad de Usuario.
class Cliente(Usuario):
    def __init__(self, nombre: str, correo: str, saldo: float):
        # super() inicializa los atributos heredados de la clase padre.
        super().__init__(nombre, correo)
        self.saldo = saldo

    # Sobrescritura de método (Polimorfismo): Implementación específica para Cliente.
    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Saldo: ${self.saldo:.2f}"