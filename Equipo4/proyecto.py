import pandas as pd

df = pd.read_excel("datos_proyecto_nuevo.xlsx", engine="openpyxl")
print(df.head())
password = "1234"
intento = input("Ingresa contraseña: ")

if intento != password:
    print("Acceso denegado")
    exit()
    import matplotlib.pyplot as plt

def ver_datos():
    print(df.head())

def estadisticas():
    print(df.describe())

def ventas_sucursal():
    datos = df.groupby('Sucursal')['Ventas'].sum()
    print(datos)
    datos.plot(kind='bar')
    plt.title("Ventas por sucursal")
    plt.xlabel("Sucursal")
    plt.ylabel("Ventas")
    plt.show()

def productos():
    datos = df.groupby('Producto')['Ventas'].sum()
    print(datos)
    datos.sort_values(ascending=False).plot(kind='bar')
    plt.title("Productos más vendidos")
    plt.show()

def clientes():
    datos = df.groupby('Cliente')['Ventas'].sum()
    print(datos)
    datos.sort_values(ascending=False).plot(kind='bar')
    plt.title("Mejores clientes")
    plt.show()

def proveedores():
    datos = df.groupby('Proveedor')['Precio'].mean()
    print(datos)
    datos.plot(kind='bar')
    plt.title("Precio promedio por proveedor")
    plt.show()
    password = "1234"
intento = input("Ingresa contraseña: ")

if intento != password:
    print("Acceso denegado")
    exit()
    import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("datos_proyecto_nuevo.xlsx", engine="openpyxl")
while True:
    print("\n--- MENÚ ---")
    print("1. Ver datos")
    print("2. Estadísticas")
    print("3. Ventas por sucursal")
    print("4. Productos más vendidos")
    print("5. Mejores clientes")
    print("6. Proveedores")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(df.head())
    elif opcion == "2":
        print(df.describe())
    elif opcion == "3":
        ventas_sucursal()
    elif opcion == "4":
        productos()
    elif opcion == "5":
        clientes()
    elif opcion == "6":
        proveedores()
    elif opcion == "7":
        break
    else:
        print("Opción inválida")
        
