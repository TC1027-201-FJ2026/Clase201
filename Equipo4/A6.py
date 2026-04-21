# ==============================
# 1) GRAFICA DE EJEMPLO
# ==============================
import matplotlib.pyplot as plt
import statistics

print("----- GRAFICA DE EJEMPLO -----")

barlist = plt.bar(["a","b","c","d"], [1,2,3,4])
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('c')

plt.title("Ejemplo de gráfica de barras")
plt.show()


# ==============================
# 2) GRAFICAS DE PRODUCTOS
# ==============================
print("----- GRAFICAS DE PRODUCTOS -----")

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Audifonos"]
precios = [15000, 300, 800, 4000, 1200]
ventas = [10, 50, 30, 15, 25]

# Precios
plt.figure()
plt.bar(productos, precios)
plt.title("Precio de productos")
plt.xlabel("Productos")
plt.ylabel("Precio")
plt.show()

# Ventas
plt.figure()
plt.bar(productos, ventas)
plt.title("Ventas de productos")
plt.xlabel("Productos")
plt.ylabel("Cantidad vendida")
plt.show()


# ==============================
# 3) CALIFICACIONES
# ==============================
print("----- CALIFICACIONES -----")

calificaciones = []

n = int(input("¿Cuántas calificaciones quieres ingresar? "))

for i in range(n):
    nota = float(input("Ingresa la calificación: "))
    calificaciones.append(nota)

print("Mis calificaciones son:", calificaciones)

# Promedio
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio:", round(promedio, 2))

# Moda
try:
    moda = statistics.mode(calificaciones)
    print("Moda:", moda)
except:
    print("No hay moda clara")

# Máximo y mínimo
print("Máximo:", max(calificaciones))
print("Mínimo:", min(calificaciones))

# Desviación estándar
if len(calificaciones) > 1:
    desviacion = statistics.stdev(calificaciones)
    print("Desviación estándar:", round(desviacion, 2))
else:
    print("No se puede calcular desviación con un solo dato")

# Conteo
print("Cantidad de 100:", calificaciones.count(100))
print("Cantidad de 70:", calificaciones.count(70))

# Conclusión simple
if promedio >= 90:
    print("Conclusión: Tienes un excelente desempeño.")
elif promedio >= 70:
    print("Conclusión: Tienes un buen desempeño.")
else:
    print("Conclusión: Necesitas mejorar.")
