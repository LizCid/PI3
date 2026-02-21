from abc import ABC, abstractmethod

# Se utiliza ABC para definir una Clase Abstracta.
# No puede ser instanciada directamente, sirve como base estructural.
class Usuario(ABC):
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    # Método abstracto: obliga a las subclases a implementar su propia lógica.
    # Esto es la base para lograr el Polimorfismo.
    @abstractmethod
    def mostrar_info(self):
        pass