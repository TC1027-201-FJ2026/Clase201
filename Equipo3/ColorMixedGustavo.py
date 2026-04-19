# Función que pide dos colores primarios
def pideColores():
    color1 = input("Dame un color: ")
    color2 = input("Dame otro color: ")
    mezclaColores(color1, color2)

# Función que despliega el color resultante
def mezclaColores(c1, c2):
    primarios = ["rojo", "azul", "amarillo"]
    if c1 in primarios and c2 in primarios and c1 != c2:
        if (c1 == "rojo" and c2 == "azul") or (c1 == "azul" and c2 == "rojo"):
            print("El color que se forma es PÚRPURA.")
        elif (c1 == "rojo" and c2 == "amarillo") or (c1 == "amarillo" and c2 == "rojo"):
            print("El color que se forma es ANARANJADO.")
        elif (c1 == "azul" and c2 == "amarillo") or (c1 == "amarillo" and c2 == "azul"):
            print("El color que se forma es VERDE.")
    else:
        print("No son colores primarios.")

# Llamada
pideColores()