

# Fundamentos de POO en Python

# Se crea una clase llamada Perro
class Perro:

    # Metodo sonido
    # Devuelve el sonido caracteristico del perro
    def sonido(self):
        
        # Retorna la palabra Guau
        return "Guau"
    
# Se crea una clase llamada Gato
class Gato:

    # Metodo sonido
    # Tiene el mismo nombre que ele metodo de la clase Perro
    def sonido(self):

        # Retorna la palabra "miau"
        return "Miau"
    
# Se crea una lista llamada "Animales"
# Dentro de la lista se almacena objetos de diferentes clases
animales = [Perro(), Gato()]

# Se recorre cada objeto almacenado en la lista
for animal in animales: 

    # Se ejecuta el metodo sonido() de cada objeto
    # Dependiendo del objeto, el resultado sera diferente
    print(animal.sonido())