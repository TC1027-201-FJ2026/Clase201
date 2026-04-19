import math
 
def menu():
    print("1) Área del Triángulo")
    print("2) Área del Círculo")
    print("3) Área del Cuadrado")
    print("4) Área del Rectángulo")
 
def operaciones(opcion):
    if opcion == 1:
        base = float(input("Dame la base: "))
        altura = float(input("Dame la altura: "))
        print(f"El área del triángulo con base {base} y altura {altura} es: {0.5 * base * altura:.4f}")
    elif opcion == 2:
        radio = float(input("Dame el radio: "))
        print(f"El área del círculo con radio {radio} es: {math.pi * radio ** 2:.4f}")
    elif opcion == 3:
        lado = float(input("Dame el lado: "))
        print(f"El área del cuadrado con lado {lado} es: {lado ** 2:.4f}")
    elif opcion == 4:
        base = float(input("Dame la base: "))
        altura = float(input("Dame la altura: "))
        print(f"El área del rectángulo con base {base} y altura {altura} es: {base * altura:.4f}")
    else:
        print("La opción no existe.")
 
menu()
opcion = int(input("¿Qué área deseas realizar? "))
operaciones(opcion)
print("ADIOS")
