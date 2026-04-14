"""
Convierte grados Centígrados a grados Fahrenheit.

Fórmula:
    F = C * (9/5) + 32

Salida esperada:
    X grados Centígrados corresponde a X grados Fahrenheit.
"""


def convertir_centigrados_a_fahrenheit(grados_centigrados: float) -> float:
    """
    Convierte una temperatura de grados Centígrados a Fahrenheit.

    Args:
        grados_centigrados: Temperatura en grados Centígrados.

    Returns:
        La temperatura equivalente en grados Fahrenheit.
    """
    return grados_centigrados * (9 / 5) + 32


def main() -> None:
    """
    Solicita una temperatura en grados Centígrados, realiza la conversión
    a Fahrenheit y muestra el resultado.
    """
    try:
        grados_centigrados = float(
            input(
                "Digite el número de grados Centígrados que desea convertir a grados Fahrenheit: "
            )
        )
        grados_fahrenheit = convertir_centigrados_a_fahrenheit(grados_centigrados)

        print(
            f"{grados_centigrados} grados Centígrados corresponde a "
            f"{grados_fahrenheit} grados Fahrenheit."
        )
    except ValueError:
        print("Error: debes ingresar un valor numérico válido.")


if __name__ == "__main__":
    main()