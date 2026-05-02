def pedir_articulos():
    cantidad = int(input("¿Cuántos artículos seleccionaste? "))
    return cantidad

def calcular_total(cantidad):
    total = 0.0
    for i in range(1, cantidad + 1):
        nombre = input(f"Nombre del artículo {i}: ")
        precio = float(input(f"Precio de {nombre}: "))
        total += precio
    print("Total a pagar")
    print(f"$ {total}")

def main():
    cantidad = pedir_articulos()
    calcular_total(cantidad)

if __name__ == "__main__":
    main()
