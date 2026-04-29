# Tablero de visualización - Impacto de la pandemia en United Airlines
# Gustavo Dueñas - A00835554

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo de Excel en un DataFrame
datos = pd.read_excel("ChartData.xlsx")

# Convertir la columna Date a formato de fecha
datos['Date'] = pd.to_datetime(datos['Date'])

# Ordenar por fecha
datos = datos.sort_values('Date')

# =============================================
# GRÁFICA 1: Línea - Precio de cierre a lo largo del tiempo
# =============================================
plt.figure(figsize=(12, 6))
plt.plot(datos['Date'], datos['Close/Price'], color='#1a5276', linewidth=1.5)

# Línea vertical para marcar el inicio de la pandemia (11 marzo 2020, declaración OMS)
plt.axvline(x=pd.Timestamp('2020-03-11'), color='red', linestyle='--', linewidth=1, label='Declaración de pandemia (OMS)')

plt.title('Precio de cierre de United Airlines (UAL) - Junio 2019 a Junio 2020')
plt.xlabel('Fecha')
plt.ylabel('Precio de cierre (USD)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafica1_precio_cierre.png", dpi=150)
plt.show()

# =============================================
# GRÁFICA 2: Barras - Volumen promedio mensual de transacciones
# =============================================

# Crear columna de mes-año para agrupar
datos['MesAnio'] = datos['Date'].dt.to_period('M')

# Calcular el volumen promedio por mes
volumen_mensual = datos.groupby('MesAnio')['Volume'].mean()

# Definir colores: rojo para meses de pandemia (marzo 2020 en adelante)
colores = []
for periodo in volumen_mensual.index:
    if periodo >= pd.Period('2020-03', freq='M'):
        colores.append('#c0392b')  # Rojo para pandemia
    else:
        colores.append('#2e86c1')  # Azul para pre-pandemia

plt.figure(figsize=(12, 6))
plt.bar(range(len(volumen_mensual)), volumen_mensual.values, color=colores)
plt.xticks(range(len(volumen_mensual)),
           [str(p) for p in volumen_mensual.index],
           rotation=45)

plt.title('Volumen promedio mensual de transacciones - United Airlines (UAL)')
plt.xlabel('Mes')
plt.ylabel('Volumen promedio de transacciones')
plt.tight_layout()
plt.savefig("grafica2_volumen_mensual.png", dpi=150)
plt.show()
