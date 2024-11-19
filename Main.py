# Importamos la clase Producto, Inventario y miExcepcion
from Producto import Producto
from Inventario import Inventario
from Excepcion import miExcepcion

# Importamos librerias
import os
import time

# Inicializamos inventario y mensaje de bienvenida
inventario = Inventario()
opcion = 0
os.system('cls')
print("Bienvenido a la gestión del inventario.\n Inicializando inventario...")
time.sleep(2)
os.system('cls')

# Después de esperar 2 segundos, inicializamos el menú
while opcion != '6':
    print("MENU Gestión Inventario")
    print("=======================\n")
    print("1- Agregar un producto")
    print("2- Modificar el precio o la cantidad de un producto")
    print("3- Elminar un producto")
    print("4- Mostrar todo el inventario")
    print("5- Buscar un producto en el inventario")
    print("6- Limpiar el inventario y salir del programa\n")
    opcion = input("Entra el valor de la opción deseada: ")
    
    if opcion == '1':           # Agregar producto
        correcto = False    # Booleano para el bucle de entrada de variables con captura de excepción
        while correcto == False:
            # Entrada de variables por parte del ususario
            nombre = input("Escribe el nombre del producto que quieres agregar al inventario: ")
            categoria = input("Escribe la categoria del producto que quieres agregar al inventario: ")
            precio = int(input("Entra el precio del producto que quieres agregar al inventario: "))
            cantidad = int(input("Entra la cantidad del producto que quieres agregar al inventario: "))
            try:
                # Creamos producto y lo añadimos al inventario
                producto = Producto(nombre,categoria,precio,cantidad)
                inventario.agregarProducto(producto)
                correcto = True
                os.system('cls')
            except miExcepcion as e:
                # Error en la entrada de variables
                print(f"Error en los datos proporcionados: {e}")
                input("\nPresione ENTER para volver a introducir los datos...")
    
    elif opcion == '2':         # Modificar producto (precio i/o cantidad)
        # Booleano para el bucle de entrada de variables con captura de exepción
        correcto = False
        # Entrada del Nombre del producto que el usuario quiere modificar
        nombre = input("Escribe el nombre del producto que quieres actualizar: ")
        
        if inventario.productoExistente(nombre):
            # El producto existe en el inventario
            print("¿Qué parámetro del producto quieres actualizar?")
            print("1- Modificar el precio")
            print("2- Modificar la cantidad")
            print("Cualquier otra tecla para volver al menú principal")
            sub_opcion = input("Entra el valor de la opción deseada: ")
            
            if sub_opcion == '1':       # Modificar precio
                while correcto == False:
                    precio = int(input("Entra el nuevo valor del precio: "))
                    try:
                        inventario.actualizarPrecioProducto(nombre,precio)
                        correcto = True
                    except miExcepcion as e:
                        # Error en la entrada de Precio
                        print(f"Error en los datos proporcionados: {e}")
                        input("\nPresione ENTER para volver a introducir el precio...")
            
            elif sub_opcion == '2':     # Modificar cantidad
                while correcto == False:
                    cantidad = int(input("Entra el nuevo valor de la cantidad: "))
                    try:
                        inventario.actualizarCantidadProducto(nombre,cantidad)
                        correcto = True
                    except miExcepcion as e:
                        # Error en la entrada de cantidad
                        print(f"Error en los datos proporcionados: {e}")
                        input("\nPresione ENTER para volver a introducir la cantidad...")
            
            else:
                print("Volviendo al menú principal...")
                time.sleep(2)
            os.system('cls')
        
        else:
            # Producto no existe en el inventario
            print("ERROR - El producto debe existir en el inventario")
            input("Presione ENTER para continuar...")
            os.system('cls')
    
    elif opcion == '3':         # Eliminar producto
        nombre = input("Escribe el nombre del producto que quieres eliminar del inventario: ")
        inventario.eliminarProducto(nombre)
        os.system('cls')
    
    elif opcion == '4':         # Mostrar inventario
        inventario.mostrarInventario()
        os.system('cls')
    
    elif opcion == '5':         # Buscar producto
        nombre = input("Escribe el nombre del producto que quieres buscar del inventario: ")
        inventario.buscarProducto(nombre)
        os.system('cls')
    
    elif opcion == '6':         # Eliminar inventario y salir del programa
        del inventario
        print("Eliminando inventario y saliendo del programa...")
        time.sleep(2)
        os.system('cls')
    
    else:                       # Cualquier opción que no sea las anteriores
        input("Opción incorrecta. Presione ENTER para continuar...")
        os.system('cls')