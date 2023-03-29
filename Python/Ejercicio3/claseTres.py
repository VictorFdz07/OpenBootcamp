#Tipos de datos inmutables

i = 5
f = 1.5
texto = "Hola"
tupla = ('a',1,'b')

#Tipos de datos mutables
lista = ['a','b','c']
lista.append('x')
lista.remove('a')

xyz = ['x','y','z']
xyz.append(lista)

diccionario = {
    "clave": "valor",
    "clave2": 15
}

dc = {
    "clave1": 1,
    "clave2": 2,
    "clave3": 3
}

dc.pop('clave1')

conjunto = {1,2,3,1,2,3}
print(conjunto)

a = {0,2,4,6,8}
b = {1,2,3,4,5}

print(a|b)#Union de conjuntos
print(a&b)#Interseccion de conjuntos
print(a-b)#Diferencia de conjuntos
print(a^b)#Diferencia simetrica

#Conjuntos de datos
numeros = 5
cadenas = 'hola'
booleano = True
flotante = 50.5
listas = ['a','b','c']
tupla = ('a','b','c')
diccionario = {'clave': 1, 'clave2': 2}
conjunto = {1,2,3,4,1,2,3,4}

#Metodos de cadenas
mitexto = "hola, esto es un textO"
print(mitexto.capitalize())
print(mitexto.title())
print(mitexto.lower())
print(mitexto.upper())
print(mitexto.replace('a','o'))
print(mitexto.find("esto"))

#Convertir cadena a lista
print(mitexto.split())
print(mitexto.split(','))
print(mitexto.replace(',', '').lower().split())

listaTexto = mitexto.replace(',', '').lower().split()
mivarcompleta='-'.join(listaTexto)
print(mivarcompleta)

#Operadores + - *
#Division /
#Potencia **
#Modulo %
# +=, -=, *=, /=, **=, &=, |=, ^=, >>=, <<=
#comparacion ==, !=, >, >=, <, <=
#identidad is, is not
#membresia in, not in
#bit &,|,^,<<,>,~

