# Función que calcula el costo de barras de pan no frescas
def pan(barras_no_frescas):
    precio_fresca = 11
    descuento = 0.60
    precio_no_fresca = precio_fresca * (1 - descuento)
    costo_final = barras_no_frescas * precio_no_fresca
    print(f"El costo de una barra fresca es de ${precio_fresca}")
    print(f"El descuento sobre una barra no fresca es {descuento * 100}%")
    print(f"El costo final a pagar es de ${round(costo_final, 2)}")

# Llamada a la función
barras = int(input("Introduce el número de barras que no son frescas: "))
pan(barras)