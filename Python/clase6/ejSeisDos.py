#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = None
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota > 7:
            print("El alumno",self.nombre, "esta aprobado con la nota de", self.nota)
        else:
            print("El alumno",self.nombre, "esta reprobado con la nota de", self.nota)


a = Alumno("Victor", 0)
a.aprobado()