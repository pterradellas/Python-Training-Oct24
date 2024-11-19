# Importamos la excepción personalizada creada para controlar las variables de entrada
from Excepcion import miExcepcion 

# CREACIÓN DE LA CLASE PRODUCTO
class Producto():
    # Declaración de métodos
    # CONSTRUCTOR
    def __init__(self,nombre,categoria,precio,cantidad):
        # Utilizo el setter para inicializar los atributos para así controlar la excepción en un único sitio
        self.setNombre(nombre)
        self.setCategoria(categoria)
        self.setPrecio(precio)
        self.setCantidad(cantidad)
    
    # Sobreescribo el método __eq__ para que me busque productos por el atributo nombre
    def __eq__ (self,nombre):
        return self.__nombre == nombre

    # SETTERS
    def setNombre(self,nombre):
        if len(nombre) >= 2:
            self.__nombre = nombre
        else:
            # Lanzamos excepción para controlar la variable 'nombre'
            raise(miExcepcion('El nombre del prouducto deber ser como mínimo de 2 carácteres.'))
    def setCategoria(self,categoria):
        if len(categoria) >= 2:
            self.__categoria = categoria
        else:
            # Lanzamos excepción para controlar la variable 'categoria'
            raise(miExcepcion('El nombre de la categoria deber ser como mínimo de 2 carácteres.'))
    def setPrecio(self,precio):
        if precio>0:
            self.__precio = precio
        else:
            # Lanzamos excepción para controlar la variable 'precio'
            raise(miExcepcion('El valor del precio tiene que ser superior a 0.'))
    def setCantidad(self,cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            # Lanzamos excepción para controlar la variable 'cantidad'
            raise(miExcepcion('El valor de la cantidad tiene que ser superior o igual a 0.'))
    
    # GETTERS
    def getNombre(self):
        return self.__nombre
    def getCategoria(self):
        return self.__categoria
    def getPrecio(self):
        return self.__precio
    def getCantidad(self):
        return self.__cantidad