class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        # Agregación: La tienda contiene ventas, pero las ventas son registros independientes.
        self.ventas = []

    def registrar_venta(self, venta):
        self.ventas.append(venta)