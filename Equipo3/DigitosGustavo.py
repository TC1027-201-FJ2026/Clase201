# Función que pide el número al usuario
def pedir_numero():
    numero = int(input("Dame un número entero: "))
    contar_digitos(numero)

# Función que cuenta y muestra los dígitos
def contar_digitos(num):
    num = abs(num)
    if num <= 9:
        print("El número tiene 1 dígito.")
    elif num <= 99:
        print("El número tiene 2 dígitos.")
    elif num <= 999:
        print("El número tiene 3 dígitos.")
    else:
        print("Error: el número tiene más de 3 dígitos.")

# Llamada
pedir_numero()