# Programa para acumular los n depósitos efectuados en un mes
# en una cuenta de ahorros, validando que sea el mes en curso

n = int(input("Introduce el número de depósitos efectuados en un mes: "))
print(n, "depósitos efectuados en un mes")

mes_curso = int(input("Introduce el mes en curso (1-12): "))

total_importes = 0
depositos_correctos = 0
contador = 0

while contador < n:
    mes = int(input("Introduce el mes del depósito: "))
    importe = float(input("Introduce el importe del depósito: "))
    print("Mes:", mes, "- Importe del depósito:", importe)

    if mes == mes_curso:
        total_importes += importe
        depositos_correctos += 1
    else:
        print("Error en el mes")

    contador += 1

print("Total de importes")
print("$", total_importes)
print("Total de importes del mes en curso")
print(depositos_correctos)
