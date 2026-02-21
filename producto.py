class Producto:
    # Atributo de clase para conteo global (compartido por todas las instancias).
    contador_productos = 0

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        # Incremento del contador cada vez que se crea un objeto Producto.
        Producto.contador_productos += 1

    # @staticmethod: Método de utilidad que no depende de los atributos de instancia.
    @staticmethod
    def es_precio_valido(precio: float) -> bool:
        return precio > 0

    # @classmethod: Accede a la clase (cls) para gestionar atributos de clase.
    @classmethod
    def total_productos(cls):
        return cls.contador_productos