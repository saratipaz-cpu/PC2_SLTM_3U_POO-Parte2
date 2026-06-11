# Fundamentos de POO en Python



# Se crea una clase 
# NombreClase debe de reemplazarse por el nombre que deseamos dar a la clase
class NombreClase:

    # Se define el metodo constructor
    # __init__ se ejecuta automaticamente al crear un objeto
    # self: representa al objeto actual
    # atributo1 y atributo2 son parametros que recibira el contructor
    def __init__(self, atributo1, atributo2):
        
        # Se crea el atributo 'atributo1' dentro del objeto
        # Se almacena el valor recibido en el parametro 'atributo1'
        self.atributo1 = atributo1

        # Se crea el atributo 'atributo2' dentro del objeto
        # Se almacena el valor recibido en el parametro 'atributo2'
        self.atributo2 = atributo2
