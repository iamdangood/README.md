Algoritmo Transformar_Distancia
    Definir distancia_metros, distancia_km, distancia_cm, distancia_mm Como Real
	
    Escribir "Ingrese la distancia en metros:"
    Leer distancia_metros
	
    distancia_km <- distancia_metros / 1000  
    distancia_cm <- distancia_metros * 100  
    distancia_mm <- distancia_metros * 1000  
	
    Escribir "La distancia ingresada equivale a:", distancia_km, "kilómetros,", distancia_cm, "centímetros y", distancia_mm, "milímetros."
FinAlgoritmo
