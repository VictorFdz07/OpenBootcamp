peso = input("Ingrese su peso en Kilogramos: ")

estatura = input("Ingrese su estatura en Metros: ")

imc = round(float(peso)/(float(estatura)**2),2)

print("Tu índice de masa corporal es: "+str(imc))