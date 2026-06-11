# Se crea una clase llamada "Carro"
class Carro:
    # Se crea un constructor de la clase
    # Se ejecuta automaticamente al crear un objeto
    def __init__(self, marca,modelo):
        
        # Se crea el atributo 'marca'
        # Y se guarda el valor recibido en el parametro 'marca'
        self.marca = marca

        # Se crea el atributo 'modelo' y se guarda el valor
        # recibido en el parametro 'modelo'
        self.modelo = modelo

# Crear el objeto 'carrito'
# La marca sera 'Toyota' y el modelo es 'Corolla'
carrito = Carro(marca="Toyota",modelo= "Corolla")

# Se imprime el atributo 'marca' del objeto 'carrito'
# Si se desea que se muestre la marca o modelo debe de 
# agregarse .atributo
print(carrito.marca) # Resultado: Toyota

