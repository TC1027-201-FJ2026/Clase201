# Ejercicio 3 - Gráficas de precios y ventas de productos
import matplotlib.pyplot as plt

# Listas de productos, precios y ventas
productos = ["Sesión retrato", "Sesión producto", "Edición foto", "Impresión A3", "Sesión evento", "Paquete redes"]
precios = [1500, 2000, 300, 250, 3500, 4000]
ventas = [12, 8, 35, 20, 5, 10]

# Gráfica 1 - Precios de los productos
plt.figure(figsize=(10, 6))
barras_precio = plt.bar(productos, precios, color=['#2196F3', '#FF9800', '#4CAF50', '#9C27B0', '#F44336', '#00BCD4'])
plt.title("Precio de los principales servicios de fotografía")
plt.xlabel("Servicio")
plt.ylabel("Precio (MXN)")
plt.legend(barras_precio, productos, title="Servicios", loc="upper left", fontsize=8)
plt.xticks(rotation=25, ha='right')
plt.tight_layout()
plt.show()

# Gráfica 2 - Ventas de los productos
plt.figure(figsize=(10, 6))
plt.pie(ventas, labels=productos, autopct='%1.1f%%',
        colors=['#2196F3', '#FF9800', '#4CAF50', '#9C27B0', '#F44336', '#00BCD4'],
        startangle=140)
plt.title("Distribución de ventas por servicio de fotografía")
plt.legend(productos, title="Servicios", loc="lower right", fontsize=8)
plt.tight_layout()
plt.show()
