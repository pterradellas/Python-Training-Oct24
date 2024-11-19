# Python-Training-Oct24

Exercicio final para el curso de Python

Descripción del ejercicio: Crea una aplicación en Python para la gestión de un inventario de productos, usando programación orientada a objetos (POO). El sistema debe permitir agregar, actualizar, eliminar y mostrar productos en un inventario, cada uno de los cuales es representado como un objeto de la clase Producto.

Estructura ficheros:
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
    - Atributos:
    - Métodos:
    
- Excepcion.py --> Fichero de la clase 'Excepción', donde sobreescribo la clase Esception y me sirve para poder controlar las excepciones generadas por el código cuando el ususario entra alguna variable errónea.