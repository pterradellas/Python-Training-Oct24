# Python-Training-Oct24

Exercicio final para el curso de Python

__Descripción del ejercicio:__ Crea una aplicación en Python para la gestión de un inventario de productos, usando programación orientada a objetos (POO). El sistema debe permitir agregar, actualizar, eliminar y mostrar productos en un inventario, cada uno de los cuales es representado como un objeto de la clase Producto.

__Estructura ficheros:__
- Main.py --> Fichero principal de ejecución de la aplicación
- Producto.py --> Fichero de la clase 'Producto', con los siguientes atributos y métodos:
    - Atributos:
        - Nombre: El nombre del producto.
        - Categoria: La categoría a la que pertenece el producto.
        - Precio: El precio del producto (debe ser mayor que 0).
        - Cantidad: La cantidad en stock (debe ser mayor o igual que 0).

    - Métodos:
        - def __init__(self,nombre,categoria,precio,cantidad)   --> Contructor
        - def __eq__ (self,nombre)                              --> Sobreescribo el método __eq__ para que me busque productos por el atributo nombre
        - def setNombre(self,nombre)                            --> Setter Nombre Producto
        - def setCategoria(self,categoria)                      --> Setter Categoria Producto
        - def setPrecio(self,precio)                            --> Setter Precio Producto
        - def setCantidad(self,cantidad)                        --> Setter Cantidad Proucto
        - def getNombre(self):                                  --> Getter Nombre Producto
        - def getCategoria(self):                               --> Getter Categoria Producto
        - def getPrecio(self):                                  --> Getter Precio Producto
        - def getCantidad(self):                                --> Getter Cantidad Producto

- Inventario.py --> Fichero de la clase 'Inventario', con los siguientes atributos y métodos:
    - Atributos: NA
    - Métodos:
        - def __init__(self)                                    --> Constructor
        - def agregarProducto(self,producto)                    --> Setter Producto
        - def actualizarPrecioProducto(self,nombre,precio)      --> Setter Precio
        - def actualizarCantidadProducto(self,nombre,cantidad)  --> Setter Cantidad
        - def eliminarProducto(self,nombre)                     --> Eliminar Producto
        - def mostrarInventario(self)                           --> Getter Inventario Completo
        - def buscarProducto(self,nombre)                       --> Getter Producto
        - def posiciónInventario(self,nombre)                   --> Getter posición de un Producto dentro del Inventario
        - def productoExistente(self,nombre)                    --> Getter que nos valida si el Producto existe en el Inventario
        - def __del__(self)                                     --> Destructor

- Excepcion.py --> Fichero de la clase 'Excepción', donde sobreescribo la clase genérica Esception, y me sirve para poder controlar las excepciones generadas por el código cuando el ususario entra alguna variable errónea.
    - Excepciones controladas:
        - Nombre y Categoria deben ser como mínimo de 2 carácteres.
        - Precio debe ser superior a '0'.
        - Cantidada debe ser igual o superior a '0'.