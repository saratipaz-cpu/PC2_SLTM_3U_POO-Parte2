

# Fundamentos de POO en Python 

# Se crea una clase llamada 'CuentaBancaria'
# Esta clase servirá como plantilla para crear objetos que representen 
# cuentas bancarias
class CuentaBancaria:
    
    # Constructor de la clase
    # Se ejecuta automáticamente cuando se crea un objeto
    #'saldo' es un dato que recibira el objeto
    def __init__(self, saldo):
        
        # Se crea un atributo privador llamado '__saldo'
        # Los dos guiones bajos indican encapsulamiento
        # El saldo queda protegido dentro del objeto
        self.__saldo = saldo

    # Se crea un metodo llamado 'mostrar_saldo'
    # Este metodo permitira visualizar el saldo almacenado
    def mostrar_saldo(self):

        # Se muestra el valor del atributo privado __saldo
        print(self.__saldo)