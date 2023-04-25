def isBisiesto(year):
    if year % 4 == 0:
        return "Es un año bisiesto"
    else:
        return "No es un año bisiesto"

print(isBisiesto(1992))