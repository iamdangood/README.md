Algoritmo Transformar_Distancia
    Definir distancia_metros, distancia_km, distancia_cm, distancia_mm Como Real
	
    Escribir "Ingrese la distancia en metros:"
    Leer distancia_metros
	
    distancia_km <- distancia_metros / 1000  
    distancia_cm <- distancia_metros * 100  
    distancia_mm <- distancia_metros * 1000  
	
    Escribir "La distancia ingresada equivale a:", distancia_km, "kil�metros,", distancia_cm, "cent�metros y", distancia_mm, "mil�metros."
FinAlgoritmo
