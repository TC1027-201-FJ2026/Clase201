# =============================================
# Programa: Área y Volumen de un Cilindro
# =============================================
# Fórmulas:
# Área total: AT = 2πr(h + r)
# Volumen: V = πr²h
import math # Importar módulo math para pi
# --- Título del programa ---
print("El área y volumen del cilindro")
# --- Entrada de datos ---
# Solicitar el radio y la altura del cilindro
radio = float(input("Introduzca el radio: "))
altura = float(input("Introduzca la altura: "))
# --- Proceso ---
# Calcular el área total: AT = 2 * π * r * (h + r)
area = 2 * math.pi * radio * (altura + radio)
# Calcular el volumen: V = π * r² * h
volumen = math.pi * radio**2 * altura
# --- Salida ---
# Mostrar los resultados
print("El área del cilindro es:", area)
print("El volumen del cilindro es:", volumen)
