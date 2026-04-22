# Programa para calcular el total a pagar de una compra
# de acuerdo a los n artículos seleccionados

n = int(input("Introduce el número de artículos seleccionados: "))
print(n, "artículos seleccionados")

total = 0
contador = 0

while contador < n:
    nombre = input("Introduce el nombre del artículo: ")
    precio = float(input("Introduce el precio del artículo: "))
    print("Artículo:", nombre, "- Precio:", precio)
    total += precio
    contador += 1

print("Total a pagar")
print("$", total)
