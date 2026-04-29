def modyMass():
    peso = float(input("Dame tu peso en kilogramos: "))
    estatura = float(input("Dame tu estatura en metros: "))
    bmi = peso / (estatura * estatura)
    print("Tu BMI es:", round(bmi, 2))

modyMass()
