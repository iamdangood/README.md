#Solicitar al usuario que ingrese 5 números
num1 = float(input ("Ingrese el primer número: "))
num2 = float(input ("Ingrese el segundo número: "))
num3 = float(input ("Ingrese el tercer número: "))
num4 = float(input ("Ingrese el cuarto número: "))
num5 = float(input ("Ingrese el quinto número: "))

#Sumar los números digitados
resultado=num1+num2+num3+num4+num5 

#Calcular promedio
promedio = resultado/100

#Resultado
print(f"El promedio de los 5 números es: {promedio}")