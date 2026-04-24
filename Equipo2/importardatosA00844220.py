import pandas as pd
import matplotlib.pyplot as plt
import os

# Ir al escritorio
desktop_path = "/Users/charlottehiggo/Desktop"
os.chdir(desktop_path)
print("Trabajando desde el escritorio")

# Cargar el archivo (ya sabemos que está ahí)
df = pd.read_excel("ChartData.xlsx")
print("¡Archivo cargado correctamente!")
print(f"El archivo tiene {len(df)} filas de datos")
print(f"Columnas disponibles: {list(df.columns)}")

# Mostrar las primeras filas para verificar
print("\nPrimeras 3 filas:")
print(df.head(3))

# Preparar los datos
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Usar la columna correcta para el precio de cierre
if 'Close/Price' in df.columns:
    df['Close'] = df['Close/Price']
elif 'Close' in df.columns:
    df['Close'] = df['Close']
elif 'Price' in df.columns:
    df['Close'] = df['Price']

# Fecha del inicio de la pandemia
pandemic_date = pd.to_datetime("2020-03-11")

# GRÁFICA 1: Evolución del precio de cierre
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], color='blue', linewidth=1.5, label='Precio de cierre')
plt.axvline(pandemic_date, color='red', linestyle='--', linewidth=2, 
           label='Inicio pandemia (11 Mar 2020)')
plt.title('Evolución del precio de acciones de United Airlines\nImpacto de la pandemia COVID-19')
plt.xlabel('Fecha')
plt.ylabel('Precio de cierre (USD)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# GRÁFICA 2: Volumen de transacciones
plt.figure(figsize=(12, 6))
# Colorear puntos según antes/después de la pandemia
colors = ['lightblue' if date < pandemic_date else 'red' for date in df['Date']]
plt.scatter(df['Date'], df['Volume'], c=colors, alpha=0.7, s=15)
plt.axvline(pandemic_date, color='red', linestyle='--', linewidth=2,
           label='Inicio pandemia (11 Mar 2020)')
plt.title('Volumen de transacciones de United Airlines\n(Azul: pre-pandemia, Rojo: post-pandemia)')
plt.xlabel('Fecha')
plt.ylabel('Volumen de transacciones')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n¡Análisis completado! Las gráficas muestran claramente el impacto de la pandemia.")
