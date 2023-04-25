#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0

    def __init__(self):
        pass

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, vel, cil, ruedas, puertas, color):
        super().__init__()
        self.velocidad = vel
        self.cilindrada = cil
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def imprimirCoche(self):
        print("La velocidad del coche es",self.velocidad)
        print("El numero de cilidandrada es",self.cilindrada)
        print("Ek numero de puertas es",self.puertas)
        print("El numero de ruedas es",self.ruedas)
        print("El color es",self.color)

c = Coche(0,250,4,4,"Rojo")

c.imprimirCoche()