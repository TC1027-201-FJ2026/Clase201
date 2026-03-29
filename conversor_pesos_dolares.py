# Conversor de Pesos a Dólares

# Solicitar datos al usuario
precio_pesos = float(input("Ingresa el precio en pesos: "))
tipo_cambio = float(input("Ingresa el tipo de cambio del dólar: "))

# Calcular el precio en dólares
precio_dolares = precio_pesos / tipo_cambio

# Mostrar resultado
print("el precio del producto en dólares es:", precio_dolares, "USD")
