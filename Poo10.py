
# Metodo con parametros

# Se crea la clase llamada 'Persona'
class Persona:

    # Se define un metodo llamado 'saludar()'
    # self: representa al objeto que ejecuta el metodo
    # 'nombre': es un parametro que recibira informacion
    # cuando el metodo sea llamado
    def saludar(self, nombre):

        # Se muestra el mensaje 'Salida de datos'
        # La f antes de las comillas: indica un f-string
        # Permite insertar el valor de la variable 'nombre'
        # dentro del texto
        print(f"Hola {nombre} !" )

# Se crea un objeto llamado 'p' a partir de la clase 'Persona'
p = Persona()

# El objeto 'p' ejecuta el metodo 'saludar()'
# Se envia el valor 'Maulwurf' como argumento al parametro 'nombre'
p.saludar("Maulwurf")