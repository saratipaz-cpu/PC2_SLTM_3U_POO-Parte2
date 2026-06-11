

# Se crea una clase llamada "Persona"
# La clase sirve como plantilla para crear objetos de un tipo 'Persona'
class Persona:

    # Se define el metodo constructor
    # __init__ se ejecuta automaticamente al crear un objeto
    # self: representa al objeto actual
    # nombre y edad son parametros que recibira el contructor
    def __init__(self, nombre, edad):
        
        # Se crea el atributo 'nombre' dentro del objeto
        # Se almacena el valor recibido en el parametro 'nombre'
        self.nombre = nombre

        # Se crea el atributo 'edad' dentro del objeto
        # Se almacena el valor recibido en el parametro 'edad'
        self.edad = edad

# Se crea un objeto llamado 'persona1' utilizando la clase Persona
# Se envian dos datos al constructor:
# nombre = "Carlitos"
# edad = 30
persona1 = Persona(nombre='Carlitos',edad=30)

# Se imprime el valor almacenado en el atributo 'nombre' del objeto persona1
# el resultado que aparecera en pantalla sera: Carlitos
print(persona1.nombre)
