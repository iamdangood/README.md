#Solicite al usuario ingresar un tiempo en segundos (s)
tiempo_segundos = float(input("Ingrese un tiempo en segundos (s): "))
#Transformar a horas (h)
tiempo_horas = tiempo_segundos/3600

#Transformar a minutos (min)
tiempo_minutos = tiempo_segundos/60

#Resultado
print("el tiempo de",tiempo_segundos,"segundos equivale a:")
print("Horas (h)", tiempo_horas, "h")
print("Minutos (Min)", tiempo_minutos, "min")
