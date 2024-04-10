#Solicitar al usuario la velocidad en kilometros por hora (Km/h)
velocidad_Kmh = float(input("Ingrese la velocidad en kilometros por hora (Km/h): "))

#Solicitar al usuario el tiempo en horas (h)
tiempo_horas = float(input("Ingrese el tiempo en horas (h): "))

#Calcular la distancia recorrida en kilometros (Km)
distancia_km = velocidad_Kmh*tiempo_horas

#resultado
print("La distancia recorrida es:", distancia_km, "Kilometros")
