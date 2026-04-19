

def main() -> None:
    precio_pesos = float(input("Ingresa el precio del producto en pesos: "))
    tipo_cambio = float(input("Ingresa el tipo de cambio del dólar: "))

    if tipo_cambio <= 0:
        print("El tipo de cambio debe ser mayor que 0.")
        return

    precio_dolares = precio_pesos / tipo_cambio
    print(f"El precio del producto en dólares es: {precio_dolares:.2f}")


if __name__ == "__main__":
    main()
