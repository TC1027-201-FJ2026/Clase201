
def pideColores():
    color1 = input("Dame un color: ").strip().lower()
    color2 = input("Dame otro color: ").strip().lower()
    return color1, color2
 
def mezclaColores(color1, color2):
    colors = {color1, color2}
    if colors == {"rojo", "azul"}:
        print("El color que se forma es PÚRPURA.")
    elif colors == {"rojo", "amarillo"}:
        print("El color que se forma es ANARANJADO.")
    elif colors == {"azul", "amarillo"}:
        print("El color que se forma es VERDE.")
    else:
        print("No son colores primarios.")
 
color1, color2 = pideColores()
mezclaColores(color1, color2)
