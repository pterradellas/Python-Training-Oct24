# Importamos librerias
import time

# CREACIÓN DE LA CLASE INVENTARIO
class Inventario():
    # Declaración de métodos
    # CONSTRUCTOR
    def __init__(self):
        # Inicializamos la el inventario con una lista vacía
        self.Inventario = []

    # SETTERS
    def agregarProducto(self,producto):
        # Añadimos producto al final de la lista del inventario
        if producto in self.Inventario:
            # Ya existe el producto, por lo que no debemos crearlo de nuevo
            print("Ya existe un producto con este nombre. Entre otro producto.")
            input("Presione ENTER para continuar...")
        else:
            # Añadimos producto al inventario
            self.Inventario.append(producto)

    def actualizarPrecioProducto(self,nombre,precio):
        # Validamos si el producto existe ya en el inventario
        if nombre in self.Inventario:
            # Producto existente en el inventario, y buscamos la posición que ocupa en la lista
            i = self.posiciónInventario(nombre)
            self.Inventario[i].setPrecio(precio)
        else:
            # Producto no encontrado en el inventario
            print("Producto no encontrado en el inventario")
            input("Presione ENTER para continuar...")

    def actualizarCantidadProducto(self,nombre,cantidad):
        # Validamos si el producto existe ya en el inventario
        if nombre in self.Inventario:
            # Producto existente en el inventario, y buscamos la posición que ocupa en la lista
            i = self.posiciónInventario(nombre)
            self.Inventario[i].setCantidad(cantidad)
        else:
            # Producto no encontrado en el inventario
            print("Producto no encontrado en el inventario")
            input("Presione ENTER para continuar...")
    
    def eliminarProducto(self,nombre):
        # Validamos si el producto existe ya en el inventario
        if nombre in self.Inventario:
            # Producto existente en el inventario, y lo eliminamos
            self.Inventario.remove(nombre)
            print("Eliminando producto...")
            time.sleep(3)
        else:
            # Producto no encontrado en el inventario
            print("Producto no encontrado en el inventario")
            input("Presione ENTER para continuar...")
        
    # GETTERS
    def mostrarInventario(self):
        # Método que nos muestra por pantalla el Inventario completo
        if len(self.Inventario) == 0:
            print("Iventario vacio")
        else:
            # Inventario con mínimo 1 producto
            for i in range(len(self.Inventario)):
                print("Producto",i+1,":")
                print("============")
                print("Nombre:",self.Inventario[i].getNombre(),"\nCategoria:",self.Inventario[i].getCategoria(),"\nPrecio:",self.Inventario[i].getPrecio(),"\nCantidad:",self.Inventario[i].getCantidad(),"\n")
        input("Presione ENTER para continuar...")
    
    def buscarProducto(self,nombre):
        # Método que nos busca un producto en la lista y lo muestra por pantalla
        if nombre in self.Inventario:
            # Producto en el inventario
            i = self.posiciónInventario(nombre)
            print("Nombre:",self.Inventario[i].getNombre(),"\nCategoria:",self.Inventario[i].getCategoria(),"\nPrecio:",self.Inventario[i].getPrecio(),"\nCantidad:",self.Inventario[i].getCantidad(),"\n")
        else:
            # No existe el producto en el inventario
            print("Producto no encontrado")
        input("Presione ENTER para continuar...")

    def posiciónInventario(self,nombre):
        # Método que devuelve la posición del producto dentro de la lista del inventario
        encontrado = False
        i = 0
        while encontrado == False and i <= len(self.Inventario):
            if self.Inventario[i].getNombre() == nombre:
                # Encontrada la posición del producto en la lista
                encontrado = True
                return i
            else:
                i = i + 1

    def productoExistente(self,nombre):
            # Metodo que devuelve 'True' si el producto ya existe en el inventario
            if nombre in self.Inventario:
                return True
            else:
                return False

    # DESTRUCTOR
    def __del__(self):
        self.Inventario.clear()