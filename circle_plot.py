import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo
import matplotlib.pyplot as plt
import numpy as np

# Generar puntos para el círculo con radio 5
theta = np.linspace(0, 2*np.pi, 100)
x = 5 * np.cos(theta)
y = 5 * np.sin(theta)

# Graficar el círculo
plt.plot(x, y)
plt.axis('equal')  # Para que el aspecto sea igual
plt.title('Círculo con radio 5')
plt.savefig('circle.png')  # Guardar la gráfica como imagen
plt.show()