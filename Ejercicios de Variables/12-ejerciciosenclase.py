# Solicitar al usuario ingresar las longitudes de los catetos
cat1 = float(input("Ingrese la longitud del primer cateto: "))
cat2 = float(input("Ingrese la longitud del segundo cateto: "))

# Calcular la hipotenusa utilizando el Teorema de Pitágoras
hipotenusa = (cat1 * 2) + ( cat2 * 2) ** 0.5

# Mostrar el resultado
print("La longitud de la hipotenusa es:", hipotenusa)