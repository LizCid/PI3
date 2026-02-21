from cliente import Cliente
from producto import Producto

class Venta:
    def __init__(self, cliente: Cliente):
        # Asociación: La venta está relacionada con un cliente existente.
        self.cliente = cliente
        # Composición: La lista de productos vive y muere con la instancia de Venta.
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def total(self):
        # Lógica para procesar la colección de objetos Producto.
        return sum(p.precio for p in self.productos)