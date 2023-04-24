#Funciones
temperatura = 12.0
def mifuncion(nombre):
    print("Temperatura: ", temperatura)
    print("hola", nombre)

mifuncion("Victor")

def suma(a,b):
    print(a+b)

suma(5,4)

#Funciones dentro de funciones

def matematicas(a,b):
    def suma(a,b):
        print(a+b)
    
    def resta(a,b):
        print(a-b)
    
    suma(a,b)
    resta(a,b)

matematicas(5,3)

#Funciones con parametros opcionales
def imprimeNombre(nombre="Juan"):
    print("Hola, ", nombre)
imprimeNombre()

def operacion(a=1,b=5,c=5):
    print(a+b+c)
operacion(c=9)

#Funciones con parametros variables
def parametrosVariables(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    print(resultado)
parametrosVariables(1,2,3,4)

def parametrosVariblesDos(**kwargs):
    #Verificar si existe un elemento en un diccioario
    if 'coche' not in kwargs:
        return
    
    if kwargs['coche'] == 'bonito':
        print("Tu choche es bonito")

    for key, value in kwargs.items():
        print(key, "=", value)
    
parametrosVariblesDos(vivienda="Piso", coche="bonito")

#Devolver valores de una funcion
def operaciones(a,b):
    return a+b, a-b, a*b, a/b
resultado = operaciones(2,4)
print(resultado)

def sumador(**kwargs):
    inical = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inical

    resultado = 0
    for x in range(inical, final + 1):
        resultado += x
    return resultado

print(sumador(inicial=15))

#Funciones lambda/anonima
anonima = lambda nombre, nombre2: print("Hola", nombre, "Adios", nombre2) 

anonima("Pepe", "Juan")

sumatoria = lambda x: x+x
print(sumatoria(2))