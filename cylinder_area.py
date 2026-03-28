import math

def calculate_cylinder_area(radius, height):
    """
    Calcula el área total de un cilindro.
    Área total = 2 * π * r² + 2 * π * r * h
    """
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius ** 2
    total_area = lateral_area + base_area
    return total_area

# Programa principal
if __name__ == "__main__":
    print("Calculadora del área de un cilindro")
    print("Fórmula: Área total = 2πr² + 2πrh")
    
    try:
        radius = float(input("Ingrese el radio del cilindro: "))
        height = float(input("Ingrese la altura del cilindro: "))
        
        if radius <= 0 or height <= 0:
            print("Error: El radio y la altura deben ser valores positivos.")
        else:
            area = calculate_cylinder_area(radius, height)
            print(f"El área total del cilindro es: {area:.2f} unidades cuadradas")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")