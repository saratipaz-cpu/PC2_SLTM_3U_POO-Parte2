

# Fundamentos de POO en Python

# Se crea una clase llamada CuentaBancaria 
class CuentaBancaria: 
    
    # Constructor de la clase
    def __init__(self, saldo):
        
        # Atributo privado
        # El usuario no debe modificarlo directamente
        self.__saldo = saldo

    # Metodo publico para depositar dinero
    def depositar(self, cantidad):

        # proceso interno oculto al usuario
        self.__saldo += cantidad

        # Imprimir mensaje de deposito realizado
        print("Deposito realizado correctamente")

    # Metodo publico para consultar saldo
    def consultar_saldo(self):

        # devuelve el saldo actual
        return self.__saldo
    
# Crear objeto
cuenta = CuentaBancaria(1000)

# Depositar dinero 
cuenta.depositar(500)

# Consultar saldo
print("Saldo actual ", cuenta.consultar_saldo())