Algoritmo Calculo_Pago_Tienda
		Definir valor_unitario, cantidad, valor_sin_iva, valor_con_iva Como Real
		
		Escribir "Ingrese el valor unitario del producto:"
		Leer valor_unitario
		
		Escribir "Ingrese la cantidad de productos comprados:"
		Leer cantidad
		
		valor_sin_iva <- valor_unitario * cantidad
		valor_con_iva <- valor_sin_iva + (valor_sin_iva * 0.16)  // Adiciona el 16% correspondiente al IVA
		
		Escribir "El valor total a pagar con IVA incluido es:", valor_con_iva
FinAlgoritmo
