class miExcepcion(Exception):
    # Clase Excepción para controlar el valor de las variables que nos entra el usuario
    # Constructor de la clase
    def __init__(self,valor):
        self.valor = valor

    # Devuelve el string con el mensaje de error
    def __str__(self):
        return str(self.valor)