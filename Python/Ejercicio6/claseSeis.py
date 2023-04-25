#Clases y Objetos
class Juguete:
    _encendido = True #Propiedad

    def __init__(self, x):
        print("Estoy en la clase juguete, en su constructor", x)

    def enciende(self):
        print("Enciendo el aparato")
        self._encendido = True
    
    def apaga(self): #Metodo
        print("Apago el aparato")
        self._encendido = False

    def isEncendido(self):
        return self._encendido
    

class Dino(Juguete):
    color = None
    nombre = None
    #Constructor
    def __init__(self, nombre):
        #Juguete.__init__(self) 1ra forma de llamado al constructor de la clase padre
        super().__init__(nombre) #2da forma
        self.color = "Verde"
        self.nombre = nombre
        print("Estoy en el constructor de la clase Dino", nombre)

    #Destructores (en python no es necesario)
    #def __del__(self):
        #print("Estoy en el destuctor de la clase", self.__class__)

    def verEscamas(self):
        pass

#Instancias
d = Dino("Mi dinosaurio")
print(d.color)
print(d.nombre)
# del(d) llamado al destructor


#Clase estatica comparten un mismo espacio de memoria   
class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero+=1

Estatica.incrementa()
print(Estatica.numero)

#Las clases en python no existen, son diccionarios
print("-------------------------------------")

def enciende(nombre):
    print("Invoco a enciende", nombre)

diccionario = {
    'enciende': enciende,
}

diccionario['enciende']("Hola")

print("------------------")

#Clases abstractas, define funciones que seran comunes a otras clases
from abc import ABC , abstractclassmethod

class Animal(ABC):
    @abstractclassmethod #Notacion para definir metodos abstractos
    def sonido(self): #Los metodos abstractos deberan de ser utilizados en las clases que ereden de la clase abstracta padre
        pass

    def diHola(self):
        print("Hola")

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

p = Perro()
p.sonido()
p.diHola()

g = Gato()
g.sonido()
g.diHola()

print("------------")
#Relaciones HAS-A
#Composicion una clase que esta compuesta de otras clases
class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5

    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()
print("Motor es", c.motor.tipo)

c.carroceria.ventanas.cambiarCantidad(3)
print("Ventanas:", c.carroceria.ventanas.cantidad)
