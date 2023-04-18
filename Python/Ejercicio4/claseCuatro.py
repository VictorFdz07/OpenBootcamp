a = 4
b = 6
c = 7
#Condicionales
#AND
print("T y T ", True and True)
print("T y F ", True and False)
print("F y T ", False and True)
print("F y F ", False and False)
#OR
print("T o T ", True or True)
print("T o F ", True or False)
print("F o T ", False or True)
print("F o F ", False or False)
#XOR
print("T xor T ", True ^ True)
print("T xor F ", True ^ False)
print("F xor T ", False ^ True)
print("F xor F ", False ^ False)

#IF Solo se ejecuta si la condicion es cierta
if a == 5 and b <= 6:
    print("Estoy en el if")
elif a >= 6:
    print("A es mayor o igual que 6")
else:
    print("No se cumple nada de lo anterior")
print("Fin del if")

#BUCLES
#WHILE
contador = 0
while contador <= 10:
    print("Contador vale", contador)

    if contador == 5:
        print("Rompo el bucle")
        break
    
    contador += 1

    if contador % 2 == 0:
        print(contador, "es un numero par")
        continue

    print("Estoy aqui, porque contador vale", contador, "y no se ha disparado el continue")
print("Fin del while")

#FOR
#FOR valor in lista:
#   acciones
#Palabra reservada PASS usada para cuando la logica de un for aun no esta desarrollada
lista  = [1,2,3,'a',5]

longitud = len(lista)
print("La lista tiene", longitud, "items")

for valoractual in range(longitud):
    print(lista[valoractual])

#RANGE funcion que devuelve un numero de valores
for numero in range(5,10):
    print(numero)

lista2 = ["hola", "mensaje", "adios"]

if 'mensaje' in lista2:
    print("He encontrado la palabra mensaje")

for palabra in lista2:
    print("Palabra actual:", palabra)
    if palabra == 'mensaje':
        print("He encontrado la palabra mensaje")
        break
print("Fin del for")

#Ordenar una lista
lista3 = [3,4,1,2,5]
listaOrdenada = sorted(lista3)
print(listaOrdenada)
#Ordenar una lista al contrario
listaOrdenada = sorted(lista3, reverse=True)
print(listaOrdenada)

#SWITCH a partir de Python 3.10
valor = 4
match valor :
    case 1:
        print("Valor es 1")
    case 2:
        print("Valor es 2")
    case 3:
        print("Valor es 3")
    case 4:
        print("Valor es 4")
    case 4:
        print("Valor es 5")
print("Fin del match")