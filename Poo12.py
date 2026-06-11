
# Se crea una clase llamada 'Animal'
# esta sera la clase padre o superclase
class Animal: 
    
    # Se define un metodo llamado 'sonido'
    # Este metodo devuelve un solo sonido generico
    def sonido(self):

        # Retorna el texto 'sonido generico'
        return "Sonido generico"
    
# Se crea una clase llamada 'Perro'
# Entre paréntesis se indica que Perro hereda de Animal
# Perro se convierte enla clase hija o subclase
class Perro(Animal):

    # Se crea nuevamente el método sonido
    # este metodo reemplaza al metodo sonido heredado de Animal
    def sonido(self):
        return "Guau"
    
# Se crea un objeto llamado 'mi_perro' utilizando la clase Perro
mi_perro = Perro()

# Se ejecuta el metodo sonido() del objeto
# Como Perro tiene su propio metodo sonido() se ejecuta el de la clase
# Perro y no el de Animal
print(mi_perro.sonido())
