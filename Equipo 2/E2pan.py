#Pan
def pan(barras_no_frescas):
    precio_fresca = 15
    descuento = 0.60  # 60%
    precio_no_fresca = precio_fresca * (1 - descuento)
    costo_total = barras_no_frescas * precio_no_fresca
    
    print(f"El costo de una barra fresca es de ${precio_fresca}")
    print(f"El descuento sobre una barra no fresca es {descuento * 100}%")
    print(f"El costo final a pagar es de ${costo_total:.1f}")
