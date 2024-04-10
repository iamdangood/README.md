Algoritmo Calcular_Salario
	Escribir "Ingrese el salario diario del empleado: "
	Leer salario_diario
Escribir "Ingrese el número de dias trabajados: "
Leer dias_trabajados

salario_bruto = salario_diario*dias_trabajados
descuento_pension = salario_bruto*0.10
descuento_salud = salario_bruto*0.15
salario_neto = salario_bruto - descuento_pension - descuento_salud

Escribir "El salario a pagar al empleado es: ", salario_neto
FinAlgoritmo
