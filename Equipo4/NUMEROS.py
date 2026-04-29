def menu():
    print("1) Área del Triángulo")
    print("2) Área del Círculo")
    print("3) Área del Cuadrado")
    print("4) Área del Rectángulo")

def operaciones(opcion):
    if opcion == 1:
        base = float(input("Dame la base: "))
        altura = float(input("Dame la altura: "))
        area = (base * altura) / 2
        print("El área del triángulo es:", area)

    elif opcion == 2:
        radio = float(input("Dame el radio: "))
        area = 3.1416 * radio * radio
        print("El área del círculo es:", area)

    elif opcion == 3:
        lado = float(input("Dame el lado: "))
        area = lado * lado
        print("El área del cuadrado es:", area)

    elif opcion == 4:
        base = float(input("Dame la base: "))
        altura = float(input("Dame la altura: "))
        area = base * altura
        print("El área del rectángulo es:", area)

    else:
        print("La opción no existe.")

menu()
opcion = int(input("¿Qué área deseas realizar? "))
operaciones(opcion)
print("ADIOS")