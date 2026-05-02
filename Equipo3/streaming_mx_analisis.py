# =====================================================================
# EVIDENCIA - PROGRAMACION PARA NEGOCIOS
# Analisis de datos: Plataforma Streaming MX - Q1 2026
# Boom del Regional Mexicano y Corridos Tumbados
# =====================================================================
# Tema: Analizar el catalogo top de la plataforma para identificar
# que generos, canales de descubrimiento y modelos de sello generan
# mayor valor (reproducciones, ingresos y engagement) y proponer
# acciones estrategicas con base en los datos.
# =====================================================================

# Librerias necesarias para el analisis
import pandas as pd                # manejo de datos tabulares
import matplotlib.pyplot as plt    # generacion de graficas
import numpy as np                 # operaciones numericas
import random                      # generacion aleatoria del password
import string                      # caracteres para el password
import os                          # rutas del sistema


# =====================================================================
# FUNCION 1: Generacion del password de acceso
# =====================================================================
def generar_password(longitud=8):
    """
    Genera un password aleatorio que cumple las 3 condiciones de seguridad:
    1) Tener al menos una letra mayuscula
    2) Tener al menos un digito numerico
    3) Tener una longitud minima de 8 caracteres
    """
    # Se asegura un caracter de cada tipo obligatorio
    mayuscula = random.choice(string.ascii_uppercase)
    digito = random.choice(string.digits)
    minuscula = random.choice(string.ascii_lowercase)

    # El resto del password se rellena con caracteres aleatorios
    restante = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=longitud - 3
    ))

    # Se combinan y se mezclan en orden aleatorio
    password = list(mayuscula + digito + minuscula + restante)
    random.shuffle(password)
    return ''.join(password)


# =====================================================================
# FUNCION 2: Validacion del password (3 condicionales)
# =====================================================================
def validar_password(intento, password_real):
    """
    Valida un intento de password contra el password real.
    Aplica 3 estructuras condicionales para verificar la integridad.
    """
    # Condicional 1: el password debe tener longitud minima de 8
    if len(intento) < 8:
        print("  Acceso denegado: el password debe tener al menos 8 caracteres.")
        return False

    # Condicional 2: debe contener al menos un numero
    if not any(caracter.isdigit() for caracter in intento):
        print("  Acceso denegado: el password debe contener al menos un numero.")
        return False

    # Condicional 3: debe coincidir exactamente con el password generado
    if intento != password_real:
        print("  Acceso denegado: el password no coincide.")
        return False

    print("  Acceso concedido. Bienvenido al sistema.\n")
    return True


# =====================================================================
# FUNCION 3: Carga del archivo Excel
# =====================================================================
def cargar_datos(nombre_archivo="Streaming_MX_Q1_2026.xlsx"):
    """
    Lee el archivo Excel con el catalogo de canciones de la plataforma.
    Busca el archivo en (1) la misma carpeta del script, (2) la carpeta
    de trabajo actual, y si no lo encuentra, le pide al usuario la ruta.
    Devuelve un DataFrame de pandas listo para analizar.
    """
    # Ubicacion 1: misma carpeta donde esta este .py
    carpeta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_junto_al_script = os.path.join(carpeta_script, nombre_archivo)

    # Ubicacion 2: la carpeta desde donde se ejecuta el comando
    ruta_directorio_actual = os.path.join(os.getcwd(), nombre_archivo)

    # Se prueban las rutas en orden
    if os.path.exists(ruta_junto_al_script):
        ruta_final = ruta_junto_al_script
    elif os.path.exists(ruta_directorio_actual):
        ruta_final = ruta_directorio_actual
    else:
        # Como ultimo recurso, se le pide al usuario la ruta completa
        print(f"\n  No se encontro '{nombre_archivo}' en:")
        print(f"    - {carpeta_script}")
        print(f"    - {os.getcwd()}")
        ruta_final = input("  Escribe la ruta completa del archivo Excel: ").strip()
        # Limpia comillas que a veces se pegan al arrastrar el archivo a la terminal
        ruta_final = ruta_final.strip('"').strip("'")

    df = pd.read_excel(ruta_final)
    print(f"\n  Datos cargados correctamente: {df.shape[0]} canciones x {df.shape[1]} columnas.")
    print(f"  Origen: {ruta_final}\n")
    return df


# =====================================================================
# FUNCION 4: Estadistica descriptiva por columna numerica
# =====================================================================
def estadistica_descriptiva(df, columna):
    """
    Calcula y muestra los principales descriptores estadisticos de
    una columna numerica del DataFrame:
    media, mediana, desviacion estandar, minimo, maximo, cuartiles.
    """
    if columna not in df.columns:
        print(f"  La columna '{columna}' no existe.")
        return

    serie = df[columna]

    # Solo aplica a columnas numericas
    if not pd.api.types.is_numeric_dtype(serie):
        print(f"  La columna '{columna}' no es numerica.")
        return

    print(f"\n  Estadistica descriptiva de '{columna}':")
    print(f"  - Media:               {serie.mean():>12,.2f}")
    print(f"  - Mediana:             {serie.median():>12,.2f}")
    print(f"  - Desviacion estandar: {serie.std():>12,.2f}")
    print(f"  - Minimo:              {serie.min():>12,.2f}")
    print(f"  - Maximo:              {serie.max():>12,.2f}")
    print(f"  - Q1 (25%):            {serie.quantile(0.25):>12,.2f}")
    print(f"  - Q3 (75%):            {serie.quantile(0.75):>12,.2f}")
    print(f"  - Suma total:          {serie.sum():>12,.2f}")


# =====================================================================
# FUNCION 5: Menu del programa
# =====================================================================
def mostrar_menu():
    """Imprime el menu principal del programa."""
    print("=" * 65)
    print("  STREAMING MX - PANEL DE ANALISIS Q1 2026")
    print("=" * 65)
    print("  1) Ver tabla completa de canciones")
    print("  2) Estadistica descriptiva de una columna numerica")
    print("  3) Pregunta 1: Generos lideres en reproducciones e ingresos")
    print("  4) Pregunta 2: Canales virales y su engagement")
    print("  5) Pregunta 3: Major Labels vs Independientes")
    print("  6) Pregunta 4: Duracion optima de cancion")
    print("  7) Filtrar el catalogo (variar el analisis)")
    print("  8) Salir")
    print("=" * 65)


# =====================================================================
# FUNCION 6: Pregunta 1 - Generos lideres
# =====================================================================
def grafica_pregunta1(df):
    """
    Pregunta detonadora 1:
    Cuales generos generan mayor volumen de reproducciones e ingresos?
    """
    # Se agrupa por genero y se suman las metricas
    resumen = df.groupby("Genero").agg(
        Reproducciones=("Reproducciones_Millones", "sum"),
        Ingresos=("Ingresos_MXN_Miles", "sum")
    ).sort_values("Reproducciones", ascending=False)

    print("\n  Reproducciones e ingresos por genero:")
    print(resumen.round(1).to_string())

    # Grafica de barras dobles
    fig, ax1 = plt.subplots(figsize=(11, 6))
    x = np.arange(len(resumen.index))
    ancho = 0.4

    barras1 = ax1.bar(x - ancho / 2, resumen["Reproducciones"],
                      ancho, label="Reproducciones (millones)", color="#1f4e79")
    ax1.set_ylabel("Reproducciones (millones)", color="#1f4e79", fontsize=11)
    ax1.tick_params(axis="y", labelcolor="#1f4e79")
    ax1.set_xticks(x)
    ax1.set_xticklabels(resumen.index, rotation=20, ha="right")

    ax2 = ax1.twinx()
    barras2 = ax2.bar(x + ancho / 2, resumen["Ingresos"],
                      ancho, label="Ingresos (miles MXN)", color="#c0392b")
    ax2.set_ylabel("Ingresos (miles MXN)", color="#c0392b", fontsize=11)
    ax2.tick_params(axis="y", labelcolor="#c0392b")

    plt.title("Pregunta 1: Reproducciones e ingresos por genero - Q1 2026",
              fontsize=13, fontweight="bold")
    ax1.set_xlabel("Genero musical", fontsize=11)
    fig.legend(loc="upper right", bbox_to_anchor=(0.9, 0.92))
    ax1.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("grafica_1_generos.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()
    print("  Grafica guardada: grafica_1_generos.png")


# =====================================================================
# FUNCION 7: Pregunta 2 - Canales virales
# =====================================================================
def grafica_pregunta2(df):
    """
    Pregunta detonadora 2:
    Que canales de descubrimiento (origen viral) generan mayor
    engagement promedio en los oyentes?
    """
    resumen = df.groupby("Origen_Viral").agg(
        Engagement_Promedio=("Engagement_Score", "mean"),
        Canciones=("Artista", "count"),
        Reproducciones_Promedio=("Reproducciones_Millones", "mean")
    ).sort_values("Engagement_Promedio", ascending=False)

    print("\n  Engagement promedio por canal de descubrimiento:")
    print(resumen.round(2).to_string())

    # Grafica de barras horizontales
    fig, ax = plt.subplots(figsize=(11, 6))
    colores = ["#27ae60", "#2980b9", "#8e44ad", "#e67e22", "#7f8c8d"]
    barras = ax.barh(resumen.index, resumen["Engagement_Promedio"],
                     color=colores[:len(resumen)])

    # Anota el valor en cada barra
    for barra, valor in zip(barras, resumen["Engagement_Promedio"]):
        ax.text(valor + 0.5, barra.get_y() + barra.get_height() / 2,
                f"{valor:.1f}", va="center", fontsize=10, fontweight="bold")

    ax.set_xlabel("Engagement promedio (escala 0-100)", fontsize=11)
    ax.set_ylabel("Canal de descubrimiento", fontsize=11)
    ax.set_title("Pregunta 2: Engagement promedio por canal viral - Q1 2026",
                 fontsize=13, fontweight="bold")
    ax.set_xlim(0, 100)
    ax.grid(axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("grafica_2_canales.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()
    print("  Grafica guardada: grafica_2_canales.png")


# =====================================================================
# FUNCION 8: Pregunta 3 - Major vs Independiente
# =====================================================================
def grafica_pregunta3(df):
    """
    Pregunta detonadora 3:
    Como se comparan los Major Labels contra los sellos independientes
    en metricas de exito comercial y duracion en charts?
    """
    resumen = df.groupby("Sello").agg(
        Canciones=("Artista", "count"),
        Reproducciones_Prom=("Reproducciones_Millones", "mean"),
        Ingresos_Prom=("Ingresos_MXN_Miles", "mean"),
        Semanas_Prom=("Semanas_Top50", "mean"),
        Engagement_Prom=("Engagement_Score", "mean")
    )

    print("\n  Comparativo Major Labels vs Independientes:")
    print(resumen.round(2).to_string())

    # Grafica radar / agrupada
    metricas = ["Reproducciones_Prom", "Ingresos_Prom", "Semanas_Prom", "Engagement_Prom"]
    etiquetas = ["Reproducciones\n(millones)", "Ingresos\n(miles MXN)",
                 "Semanas en\nTop 50", "Engagement\n(0-100)"]

    # Para que sean comparables, se normalizan a porcentaje del maximo de cada metrica
    normalizado = resumen[metricas].copy()
    for m in metricas:
        normalizado[m] = (normalizado[m] / normalizado[m].max()) * 100

    fig, ax = plt.subplots(figsize=(11, 6))
    x = np.arange(len(metricas))
    ancho = 0.35

    ax.bar(x - ancho / 2, normalizado.loc["Major"], ancho,
           label="Major Labels", color="#1f4e79")
    ax.bar(x + ancho / 2, normalizado.loc["Independiente"], ancho,
           label="Independientes", color="#e67e22")

    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)
    ax.set_ylabel("Indice relativo (% del maximo de cada metrica)", fontsize=11)
    ax.set_title("Pregunta 3: Major Labels vs Independientes - indice relativo",
                 fontsize=13, fontweight="bold")
    ax.legend(loc="upper right")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.set_ylim(0, 110)
    plt.tight_layout()
    plt.savefig("grafica_3_sellos.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()
    print("  Grafica guardada: grafica_3_sellos.png")


# =====================================================================
# FUNCION 9: Pregunta 4 - Duracion optima
# =====================================================================
def grafica_pregunta4(df):
    """
    Pregunta detonadora 4:
    Existe una duracion optima de cancion para maximizar el engagement?
    """
    # Se segmenta la duracion en bandas para identificar el patron
    bandas = pd.cut(df["Duracion_Segundos"],
                    bins=[120, 160, 180, 200, 220, 280],
                    labels=["120-160s", "160-180s", "180-200s", "200-220s", "220-280s"])

    resumen = df.groupby(bandas, observed=True).agg(
        Canciones=("Artista", "count"),
        Engagement_Prom=("Engagement_Score", "mean"),
        Reproducciones_Prom=("Reproducciones_Millones", "mean")
    )

    print("\n  Engagement promedio por banda de duracion:")
    print(resumen.round(2).to_string())

    # Coeficiente de correlacion
    corr = df["Duracion_Segundos"].corr(df["Engagement_Score"])
    print(f"\n  Coeficiente de correlacion duracion vs engagement: {corr:.3f}")

    # Grafica de dispersion + linea de tendencia
    fig, ax = plt.subplots(figsize=(11, 6))

    # Color por genero para enriquecer la lectura
    generos = df["Genero"].unique()
    paleta = plt.cm.tab10(np.linspace(0, 1, len(generos)))
    for genero, color in zip(generos, paleta):
        subset = df[df["Genero"] == genero]
        ax.scatter(subset["Duracion_Segundos"], subset["Engagement_Score"],
                   label=genero, s=80, alpha=0.75, color=color, edgecolors="black", linewidths=0.5)

    # Linea de tendencia (regresion lineal simple)
    coef = np.polyfit(df["Duracion_Segundos"], df["Engagement_Score"], 1)
    tendencia = np.poly1d(coef)
    x_linea = np.linspace(df["Duracion_Segundos"].min(),
                          df["Duracion_Segundos"].max(), 100)
    ax.plot(x_linea, tendencia(x_linea), color="black",
            linestyle="--", linewidth=2, label=f"Tendencia (r={corr:.2f})")

    ax.set_xlabel("Duracion de la cancion (segundos)", fontsize=11)
    ax.set_ylabel("Engagement Score (0-100)", fontsize=11)
    ax.set_title("Pregunta 4: Duracion vs Engagement por genero - Q1 2026",
                 fontsize=13, fontweight="bold")
    ax.legend(loc="lower left", fontsize=8, ncol=2)
    ax.grid(linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("grafica_4_duracion.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()
    print("  Grafica guardada: grafica_4_duracion.png")


# =====================================================================
# FUNCION 10: Filtrado dinamico (estructuras de control para variar el analisis)
# =====================================================================
def filtrar_catalogo(df):
    """
    Permite al usuario filtrar dinamicamente el catalogo por genero,
    sello u origen viral para generar otras posibles soluciones.
    Aplica un ciclo for + condicionales para mostrar alternativas.
    """
    print("\n  Tipos de filtro disponibles:")
    print("    1) Por genero")
    print("    2) Por sello")
    print("    3) Por origen viral")
    opcion = input("  Selecciona tipo de filtro (1-3): ").strip()

    if opcion == "1":
        columna = "Genero"
    elif opcion == "2":
        columna = "Sello"
    elif opcion == "3":
        columna = "Origen_Viral"
    else:
        print("  Opcion invalida.")
        return

    # Se listan los valores unicos disponibles
    valores = sorted(df[columna].unique())
    print(f"\n  Valores disponibles en '{columna}':")
    for i, v in enumerate(valores, start=1):
        print(f"    {i}) {v}")

    seleccion = input(f"  Escribe el valor exacto de '{columna}' a filtrar: ").strip()

    # Se filtra y se muestra resumen
    filtrado = df[df[columna] == seleccion]
    if filtrado.empty:
        print(f"  No hay registros con '{columna}' = '{seleccion}'.")
        return

    print(f"\n  Subcatalogo filtrado ({len(filtrado)} canciones):")
    print(filtrado[["Artista", "Genero", "Sello",
                    "Reproducciones_Millones",
                    "Ingresos_MXN_Miles",
                    "Engagement_Score"]].to_string(index=False))

    # Resumen estadistico del subcatalogo
    print("\n  Resumen del subcatalogo:")
    print(f"  - Reproducciones totales: {filtrado['Reproducciones_Millones'].sum():,.1f} millones")
    print(f"  - Ingresos totales:       {filtrado['Ingresos_MXN_Miles'].sum():,.1f} miles MXN")
    print(f"  - Engagement promedio:    {filtrado['Engagement_Score'].mean():.1f} / 100")


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
def main():
    """Orquesta el flujo completo del programa."""

    # ----- Etapa 1: generacion y validacion del password -----
    print("=" * 65)
    print("  ACCESO AL SISTEMA STREAMING MX")
    print("=" * 65)
    password_sistema = generar_password(8)
    print(f"  Password generado para esta sesion: {password_sistema}")
    print("  (En produccion este password se enviaria por email seguro)")

    # Hasta 3 intentos para acceder
    intentos = 0
    autorizado = False
    while intentos < 3 and not autorizado:
        intento = input(f"\n  Intento {intentos + 1}/3 - escribe el password: ").strip()
        autorizado = validar_password(intento, password_sistema)
        intentos += 1

    if not autorizado:
        print("\n  Se agotaron los intentos. Sesion cerrada.")
        return

    # ----- Etapa 2: cargar el catalogo -----
    df = cargar_datos("Streaming_MX_Q1_2026.xlsx")

    # ----- Etapa 3: ciclo while con menu interactivo -----
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("  Selecciona una opcion (1-8): ").strip()

        if opcion == "1":
            # Tabla completa
            print("\n  Catalogo Streaming MX - Q1 2026:")
            print(df.to_string(index=False))

        elif opcion == "2":
            # Estadistica descriptiva
            columnas_num = ["Reproducciones_Millones", "Semanas_Top50",
                            "Duracion_Segundos", "Ingresos_MXN_Miles",
                            "Engagement_Score"]
            print("\n  Columnas disponibles:")
            for i, col in enumerate(columnas_num, start=1):
                print(f"    {i}) {col}")
            sel = input("  Numero de columna a analizar: ").strip()
            if sel.isdigit() and 1 <= int(sel) <= len(columnas_num):
                estadistica_descriptiva(df, columnas_num[int(sel) - 1])
            else:
                print("  Opcion invalida.")

        elif opcion == "3":
            grafica_pregunta1(df)

        elif opcion == "4":
            grafica_pregunta2(df)

        elif opcion == "5":
            grafica_pregunta3(df)

        elif opcion == "6":
            grafica_pregunta4(df)

        elif opcion == "7":
            filtrar_catalogo(df)

        elif opcion == "8":
            print("\n  Saliendo del sistema. Hasta pronto.")
            salir = True

        else:
            print("\n  Opcion invalida. Intenta de nuevo.")

        if not salir:
            input("\n  Presiona ENTER para regresar al menu...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
