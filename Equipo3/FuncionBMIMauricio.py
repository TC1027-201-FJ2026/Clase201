# Función que calcula el BMI
def modyMass():
    peso = float(input("Dame tu peso en kilogramos: "))
    estatura = float(input("Dame tu estatura en metros: "))
    bmi = peso / (estatura ** 2)
    print(f"Tu BMI es: {round(bmi, 2)}")

# Llamada a la función
modyMass()
