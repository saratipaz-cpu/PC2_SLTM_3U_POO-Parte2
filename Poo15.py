# E15_SLTM
# SLTM

# Clase Alumno
class Alumno:

    # Constructor con los atributos nombre, nota1 y nota 2
    def __init__(self, nombre, nota1, nota2):
         
        # Constructor de la clase
        # Se ejecuta automáticamente cuando se crea un objeto
        #'nombre' es un dato que recibira el objeto
        self.nombre = nombre

        # Constructor de la clase
        # Se ejecuta automáticamente cuando se crea un objeto
        #'nota1' es un dato que recibira el objeto
        self.nota1 = nota1

        # Constructor de la clase
        # Se ejecuta automáticamente cuando se crea un objeto
        #'nota2' es un dato que recibira el objeto
        self.nota2 = nota2

    #Metodo para calcular promedio
    def mostrar_promedio(self):

        # Se toman las dos notas y las dividen por la cantidad dada
        promedio = (self.nota1 + self.nota2) / 2

        # Retorna el resultado
        return promedio
    
# Crear el objeto alumno1
alumno1 = Alumno("Sara", 80,90)

# Se muestra el promedio del alumno1
print("Promedio: ", alumno1.mostrar_promedio())