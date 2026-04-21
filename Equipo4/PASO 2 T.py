n = int(input("¿Cuántos depósitos se hicieron? "))
mes_actual = int(input("Ingresa el mes actual (1-12): "))

total = 0
total_mes = 0

for i in range(n):
    mes = int(input("Mes del depósito (1-12): "))
    importe = float(input("Importe del depósito: "))
    
    total += importe
    
    if mes == mes_actual:
        total_mes += importe
    else:
        print("Depósito fuera del mes actual")

print("Total de todos los depósitos:", total)
print("Total del mes actual:", total_mes)
