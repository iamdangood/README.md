#Solicite al usuario ingresar una distancia en metros (m)
distancia_metros = float(input("Ingrese una distancia en metros (m): "))

#Transformar en Kilometros (Km)
distancia_kilometros = distancia_metros/1000

#Transformar en centimetros (Cm)
distancia_Centimetros = distancia_metros*100

#Transformar en Milímetro (Mm)
distancia_Milímetros = distancia_metros*1000

#Resultado
print("La distancia de",distancia_metros,"metros equivale a:")
print("Kilometros (Km)", distancia_kilometros, "Km")
print("Centimetros (Cm)", distancia_Centimetros, "Cm")
print("Milímetros (Mm)", distancia_Milímetros, "Mm")