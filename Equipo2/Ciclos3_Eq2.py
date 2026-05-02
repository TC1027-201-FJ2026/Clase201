def pedir_clientes():
    cantidad = int(input("Dame la cantidad de clientes: "))
    ciudad_local = input("Dame la ciudad local: ").strip().lower()
    return cantidad, ciudad_local

def contar_clientes(cantidad, ciudad_local):
    mayores_edad = 0
    foraneos = 0
    locales = 0
    for i in range(1, cantidad + 1):
        edad = int(input(f"Dame la edad del cliente {i}: "))
        ciudad = input(f"Dame la ciudad del cliente {i}: ").strip().lower()
        if edad >= 18:
            mayores_edad += 1
        if ciudad == ciudad_local:
            locales += 1
        else:
            foraneos += 1
    print("Total de clientes mayores de edad")
    print(mayores_edad)
    print("Total de clientes foráneos")
    print(foraneos)
    print("Total de clientes locales")
    print(locales)

def main():
    cantidad, ciudad_local = pedir_clientes()
    contar_clientes(cantidad, ciudad_local)

if __name__ == "__main__":
    main()
