#Modulos
#Añadir modulos externos sys.path.append("ubicacion")
#import operaciones.restador.resta as r
#import operaciones.sumador.suma as s
#from operaciones import restador, sumador
#from operaciones import *
import operaciones.sumador.suma as s
import pprint
import sys
import math

def main():
    obj = s.Sumatorio()
    obj.suma(2,2)

    help(obj.suma)


if __name__ == '__main__':
    main()

