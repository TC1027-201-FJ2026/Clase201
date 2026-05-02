def pedir_datos_iniciales():
    cantidad = int(input("¿Cuántos depósitos se efectuaron? "))
    mes_en_curso = input("Dame el mes en curso: ").strip().lower()
    return cantidad, mes_en_curso

def acumular_depositos(cantidad, mes_en_curso):
    total_importes = 0.0
    total_correctos = 0
    for i in range(1, cantidad + 1):
        mes = input(f"Dame el mes del depósito {i}: ").strip().lower()
        importe = float(input(f"Dame el importe del depósito {i}: "))
        if mes == mes_en_curso:
            total_importes += importe
            total_correctos += 1
        else:
            print("Error en el mes")
    print("Total de importes")
    print(f"$ {total_importes}")
    print("Total de importes del mes en curso")
    print(total_correctos)

def main():
    cantidad, mes_en_curso = pedir_datos_iniciales()
    acumular_depositos(cantidad, mes_en_curso)

if __name__ == "__main__":
    main()
