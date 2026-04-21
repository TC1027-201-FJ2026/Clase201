n = int(input("¿Cuántos clientes hay? "))

mayores = 0
foraneos = 0
locales = 0

ciudad_local = input("Ingresa tu ciudad: ")

for i in range(n):
    edad = int(input("Edad del cliente: "))
    ciudad = input("Ciudad del cliente: ")
    
    if edad >= 18:
        mayores += 1
    
    if ciudad.lower() == ciudad_local.lower():
        locales += 1
    else:
        foraneos += 1

print("Clientes mayores de edad:", mayores)
print("Clientes foráneos:", foraneos)
print("Clientes locales:", locales)
