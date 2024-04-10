Algoritmo sin_titulo
	Definir num,suma,promedio Como Real
	suma <- 0
	
    Para i <- 1 Hasta 5 Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer num
        suma <- suma + num
    FinPara
	
    promedio <- suma / 5
	
    Escribir "El promedio de los números ingresados es: ", promedio
FinAlgoritmo
