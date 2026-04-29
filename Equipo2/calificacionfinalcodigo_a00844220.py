

def calcular_calificacion_final(
    parcial_1: float,
    parcial_2: float,
    proyecto_final: float,
    examen_final: float
) -> float:
    return (
        parcial_1 * 0.20
        + parcial_2 * 0.35
        + proyecto_final * 0.15
        + examen_final * 0.30
    )


def leer_calificacion(nombre: str) -> float:
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
            if 0 <= calificacion <= 100:
                return calificacion
            print("Error: la calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Error: ingrese un número válido.")


def main() -> None:
    print("Cálculo de calificación final de Programación")

    parcial_1 = leer_calificacion("Parcial 1")
    parcial_2 = leer_calificacion("Parcial 2")
    proyecto_final = leer_calificacion("Proyecto Final")
    examen_final = leer_calificacion("Examen Final")

    calificacion_final = calcular_calificacion_final(
        parcial_1,
        parcial_2,
        proyecto_final,
        examen_final
    )

    print(f"La calificación final de la materia es: {calificacion_final:.2f}")


if __name__ == "__main__":
    main()
