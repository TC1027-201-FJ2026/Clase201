def pedirNumero():
    num = int(input("Dame un número entero: "))
    return num

def revisarDigitos(num):
    if num >= -9 and num <= 9:
        print("El número tiene 1 dígito.")
    elif (num >= 10 and num <= 99) or (num <= -10 and num >= -99):
        print("El número tiene 2 dígitos.")
    elif (num >= 100 and num <= 999) or (num <= -100 and num >= -999):
        print("El número tiene 3 dígitos.")
    else:
        print("Error: tiene más de 3 dígitos.")

numero = pedirNumero()
revisarDigitos(numero)