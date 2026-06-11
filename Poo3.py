

# Atributos

# Se crea una clase llamada Perro
# la clase es una plantilla para crear objetos 
# En esta clase se crean objetos de tipo 'Perro'
class Perro:

    # Se define el constructor de la clase
    # Este metodo se ejecuta automaticamente cuando se crea un objeto
    # Self: representa el objeto actual
    # Nombre: recibe el nombre del perro
    # Raza: recibe la raza del perro
    def __init__(self, nombre, raza):
        
        # Se crea el atributo nombre dentro del objeto
        # Self.nombre pertenece al objeto
        # Se almacena el valor recibido en el parametro 'nombre'
        self.nombre = nombre
        
        # Se crea el atributo raza dentro del objeto
        # Self.raza pertenece al objeto
        # Se almacena el valor recibido en el parametro 'raza'
        self.raza = raza