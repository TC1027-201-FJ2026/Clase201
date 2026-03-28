import math

def solve_quadratic(a, b, c):
    """
    Resuelve la ecuación cuadrática ax² + bx + c = 0
    """
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Dos raíces reales
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # Una raíz real (doble)
        root = -b / (2*a)
        return (root,)
    else:
        # Raíces complejas
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))

# Programa principal
if __name__ == "__main__":
    print("Resolutor de ecuaciones cuadráticas")
    print("ax² + bx + c = 0")
    
    try:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        
        if a == 0:
            print("Error: 'a' no puede ser cero en una ecuación cuadrática.")
        else:
            roots = solve_quadratic(a, b, c)
            print("Las raíces son:")
            for i, root in enumerate(roots):
                print(f"x{i+1} = {root}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")