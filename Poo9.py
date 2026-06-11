

# Metodos de instancia

# Se crea una clase llamada 'Perro'
class Perro:

    # Un metodo es una funcion que esta adentro de una clase
    # En este caso, se crea un metodo llamado 'ladrar'
    # self: representa al objeto que ejecutara el metodo
    def ladrar(self):
        
        # Esta instruccion muestra el mensaje
        # En este caso, representa el sonido que hace el perro
        print("Guau Guau")

# Se crea un objeto llamado 'mi_perro' a partir de la clase 'Perro'
mi_perro = Perro()

# El objeto 'mi_perro' ejecuta el método 'ladrar()'
# Al ejecutar, se mostrara el mensaje 'Guau Guau'
mi_perro.ladrar()