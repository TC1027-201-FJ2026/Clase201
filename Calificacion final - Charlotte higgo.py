# Calcular la calificación final de Programación

# Pedir las calificaciones al usuario
parcial1 = int(input("Ingrese la calificación del Parcial 1: "))
parcial2 = int(input("Ingrese la calificación del Parcial 2: "))
proyecto_final = int(input("Ingrese la calificación del Proyecto Final: "))
examen_final = int(input("Ingrese la calificación del Examen Final: "))

porcentaje1 = parcial1/100 * 20
porcentaje2 = parcial2/100 *35
porcentaje3 = proyecto_final/100 *15
porcentaje4 = examen_final/100 *30

notafinal = porcentaje1 + porcentaje2 + porcentaje3 + porcentaje4
print(notafinal) 