# Programa para identificar de un grupo de n clientes
# cuántos son mayores de edad, cuántos foráneos y cuántos locales

n = int(input("Introduce el número de clientes: "))
print(n, "clientes")

mayores = 0
foraneos = 0
locales = 0
contador = 0

while contador < n:
    edad = int(input("Introduce la edad del cliente: "))
    ciudad = input("Introduce la ciudad del cliente: ")
    print("Edad:", edad, "- Ciudad:", ciudad)

    if edad >= 18:
        mayores += 1

    if ciudad.lower() == "local":
        locales += 1
    else:
        foraneos += 1

    contador += 1

print("Total de clientes mayores de edad")
print(mayores)
print("Total de clientes foráneos")
print(foraneos)
print("Total de clientes locales")
print(locales)
