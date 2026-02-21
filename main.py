"""
Módulo Principal: Orquestador del sistema de Punto de Venta.
----------------------------------------------------------
Este archivo integra la lógica para demostrar los pilares de la POO:
- Abstracción y Herencia: Uso de clases derivadas de Usuario.
- Asociación: Vínculo entre Cliente y Venta.
- Composición: Manejo de Productos dentro de una Venta.
- Agregación: Registro de Ventas en la Tienda.
"""

from cliente import Cliente
from administrador import Administrador
from producto import Producto
from venta import Venta
from tienda import Tienda

# --- FUNCIONES DE VALIDACIÓN (Programación Defensiva) ---

def pedir_float(mensaje):
    """Garantiza la integridad de datos numéricos decimales mediante manejo de excepciones."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def pedir_int(mensaje):
    """Valida que el usuario ingrese únicamente números enteros para opciones y cantidades."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def pedir_nombre(mensaje):
    """Asegura que las cadenas de texto no contengan caracteres numéricos."""
    while True:
        nombre = input(mensaje)
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("Error: El nombre no debe contener números.")

# --- LÓGICA PRINCIPAL DEL SISTEMA ---

def ejecutar_punto_venta():
    # Instanciación de Administrador (Evidencia de Herencia y Polimorfismo)
    admin = Administrador(
        "Beth C Sanchez",
        "Jbeth@admin.com",
        ["Gestionar Inventario", "Ver Reportes","Descuentos","Cancelaciones"]
    )

    # Instanciación de Tienda (Clase contenedora para Agregación)
    tienda = Tienda("TechStore México")

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar cliente y venta")
        print("2. Ver estadísticas")
        print("3. Salir")

        opcion = pedir_int("Seleccione una opción: ")

        # Estructura de control para la navegación del sistema
        match opcion:
            case 1:
                print("\n--- Registro de Cliente ---")
                nombre = pedir_nombre("Nombre del cliente: ")
                correo = input("Correo del cliente: ")
                saldo = pedir_float("Saldo del cliente: ")

                # Asociación: Se crea un objeto Cliente que se pasará a la Venta
                cliente = Cliente(nombre, correo, saldo)
                
                # Composición Lógica: La Venta se inicializa vinculada a un Cliente
                venta = Venta(cliente)

                cantidad_productos = pedir_int("¿Cuántos productos desea agregar?: ")

                for i in range(cantidad_productos):
                    print(f"\nProducto #{i+1}")
                    nombre_producto = input("Nombre del producto: ")
                    precio_producto = pedir_float("Precio del producto: ")

                    # Uso de Decorador @staticmethod: Validación de lógica de negocio sin instanciar
                    if Producto.es_precio_valido(precio_producto):
                        # Composición: El objeto Producto se vuelve parte de la lista interna de Venta
                        producto = Producto(nombre_producto, precio_producto)
                        venta.agregar_producto(producto)
                    else:
                        print("Precio inválido. Producto no agregado.")

                # Agregación: Se añade la Venta terminada al historial de la Tienda
                # La Venta puede existir independientemente de la Tienda (Agregación)
                tienda.registrar_venta(venta)

                print("\nVenta registrada correctamente.")
                print(f"Total de la venta: ${venta.total():.2f}")

            case 2:
                # Demostración de Polimorfismo y Métodos de Clase (@classmethod)
                print("\n--- ESTADÍSTICAS ---")
                # Acceso a atributos de la clase Administrador (Herencia)
                print(f"Administrador: {admin.nombre}")
                # Reporte de Agregación
                print(f"Ventas registradas: {len(tienda.ventas)}")
                # Uso de @classmethod: Acceso al contador global de la clase Producto
                print(f"Productos creados: {Producto.total_productos()}")

            case 3:
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")

# Punto de entrada del script
if __name__ == "__main__":
    ejecutar_punto_venta()