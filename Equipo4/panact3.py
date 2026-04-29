def pan(barras):
    costo_barra = 11
    descuento = 0.60
    costo_final = barras * costo_barra * (1 - descuento)

    print("El costo de una barra fresca es de $" + str(costo_barra))
    print("El descuento sobre una barra no fresca es", descuento * 100, "%")
    print("El costo final a pagar es de $" + str(round(costo_final, 2)))

barras = int(input("Introduce el número de barras que no son frescas: "))
pan(barras)
