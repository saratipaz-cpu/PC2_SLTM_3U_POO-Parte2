

# Atributos de instancia

# Se crea una clase llamada 'Carro'
class Carro:

    # Se define el constructor de la calse
    # Este metodo se ejecuta automaticamente cuando se crea un objeto
    # Self: representa al objeto actual
    # color: es un objeto que recibira el objeto
    def __init__(self, color):
        
        # Se crea un atributo de instancia llamado 'color'
        # El atributo pertenece unicamente al objeto que se esta creando
        # Se almacena el valor recibido en el parametro 'color'
        self.color = color