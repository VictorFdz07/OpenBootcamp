print("Ingrese su peso en Kilogramos: ")
peso = input()
peso = float (peso)

print("Ingrese su estatura en Metros: ")
estatura = input()
estatura = float (estatura)

imc = peso/(estatura**2)

print("Tu índice de masa corporal es:",round(imc, 2))