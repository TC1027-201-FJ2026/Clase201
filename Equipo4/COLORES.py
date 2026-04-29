def pideColores():
    color1 = input("Dame un color: ")
    color2 = input("Dame otro color: ")
    return color1, color2

def mezclaColores(color1, color2):
    color1 = color1.lower()
    color2 = color2.lower()

    if (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        print("El color que se forma es PÚRPURA.")
    elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
        print("El color que se forma es ANARANJADO.")
    elif (color1 == "azul" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "azul"):
        print("El color que se forma es VERDE.")
    else:
        print("No son colores primarios.")

c1, c2 = pideColores()
mezclaColores(c1, c2)