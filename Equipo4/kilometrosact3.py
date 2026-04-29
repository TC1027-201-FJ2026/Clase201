def kilometros(millas):
    km = millas * 1.609
    print(millas, "millas son", round(km, 2), "km")

millas = float(input("Dame las millas que corriste: "))
kilometros(millas)
