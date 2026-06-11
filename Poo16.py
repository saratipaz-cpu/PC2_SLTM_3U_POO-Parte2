

# Fundamentos de POO en Python

# Se crea clase llaada CuentaBancaria
# Esta clase servira como plantilla para crear cuentas bancarias
class CuentaBancaria:

    # Contructor de la clase
    # titular: recibe el nombre del propietario de la cuenta
    # saldo= 0 indica que si no se envia un saldo, automaticamente inciara en 0
    def __init__(self, titular, saldo=0):
        
        # Atributo publico que almacena el nombre del titular
        self.titular = titular

        # Atributo privado que almacena el saldo
        # los dos guiones bajos indican encapsulamiento
        self.__saldo = saldo

    # Metodo para depositar dinero
    def depositar(self, cantidad):

        # Suma la cantidad recibida al saldo actual
        self.__saldo += cantidad

        # Muestra un mensaje confirmando el deposito
        print(f"Deposito de {cantidad} realizado")

    # Metodo para retirar dinero
    def retirar(self, cantidad):

        # Verifica si existe saldo suficiente
        if cantidad <= self.__saldo:

            # Resta la cantidad de saldo suficiente
            self.__saldo -= cantidad

            # Muestra mensaje de retiro exitoso
            print(f"Retiro de {cantidad} realizado")
        
        else: 

            # Muestra mensaje si el saldo es insuficiente
            print("Saldo insuficiente")

    # Metodo para mostrar el saldo actual
    def mostrar_saldo(self):

        # Muestra el saldo disponible
        print(f"Saldo disponible: {self.__saldo}")

# Se crea un objeto llamado cuenta
# Titular: Sara
# Saldo inicial : 100
cuenta = CuentaBancaria("Sara", 100)

# Se deposita 50 al saldo
cuenta.depositar(50)

# Se retiran 30 del saldo
cuenta.retirar(30)

# Se muestra el saldo final
cuenta.mostrar_saldo()