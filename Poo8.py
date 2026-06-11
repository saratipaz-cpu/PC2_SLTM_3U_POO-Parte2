

# Atributos de instancia

# Se crea una clase llamada 'Carro'
class Carro:

    # Se crea un atributo de clase llamado 'rueda'
    # Este atributo pertenece a la clase Carro
    # Todos los objetos creados a partir de esta clase comparten
    # este mismo valor :D
    ruedas = 4

# Se muestra el valor del atributo de la clase 'Carro'
# No es necesario crear un objeto para acceder a él
# Se accede directamente utilizando el nombre de la clase.atributo
print(Carro.ruedas)