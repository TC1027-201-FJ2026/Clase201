def contarDigitos(numero):
    digitos = len(str(abs(numero)))
    if digitos == 1:
        print("El número tiene 1 dígito.")
    elif digitos == 2:
        print("El número tiene 2 dígitos.")
    elif digitos == 3:
        print("El número tiene 3 dígitos.")
    else:
        print("Error: el número tiene más de 3 dígitos.")
 
def pedirNumero():
    numero = int(input("Dame un número entero (1, 2 o 3 dígitos): "))
    return numero
 
numero = pedirNumero()
contarDigitos(numero)
