# Función que convierte millas a kilómetros
def kilometros(millas):
    km = millas * 1.609
    print(f"{millas} millas son {round(km, 2)} km")

# Llamada a la función
millas = int(input("Dame las millas que corriste: "))
kilometros(millas)