# Programa de análisis de calificaciones del semestre pasado
import statistics

# Lista de calificaciones de los tres períodos
calificaciones = [95, 99, 99, 99, 76, 96]

print("Mis calificaciones son:", calificaciones)

# Promedio
promedio = round(statistics.mean(calificaciones), 2)
print("Mi promedio es :", promedio)

# Moda
moda = statistics.mode(calificaciones)
print("La moda de mis calificaciones :", moda)

# Máximo
maximo = max(calificaciones)
print("Mi máxima calificación que obtuve fue:", maximo)

# Mínimo
minimo = min(calificaciones)
print("Mi mínima calificación que obtuve fue:", minimo)

# Desviación estándar
desviacion = round(statistics.stdev(calificaciones), 2)
print("La desviación de mis notas fue:", desviacion)

# Conteo de 100
cuenta_100 = calificaciones.count(100)
print("Obtuve", cuenta_100, "calificaciones de: 100")

# Conteo de 70
cuenta_70 = calificaciones.count(70)
print("Obtuve", cuenta_70, "calificaciones de: 70")

# Conclusión
print("Conclusión")
print("Mi desempeño fue consistente con un promedio de", promedio,
      "y una desviación estándar de", desviacion,
      "lo que indica que mis calificaciones no variaron demasiado.",
      "Mi calificación más frecuente fue", moda,
      "lo cual refleja un buen rendimiento general.",
      "Debo trabajar en las materias donde obtuve notas más bajas para mejorar.")
