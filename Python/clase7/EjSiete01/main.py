import calculadora as c


def main():
    obj = c.Calculadora()
    print(obj.suma(5,5))
    print(obj.resta(15,5))
    print(obj.multiplicacion(5,5))
    print(obj.division(5,5))

if __name__ == '__main__':
    main()
