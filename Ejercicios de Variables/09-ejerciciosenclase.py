#Entrada el usuario
Valor_unitario = float(input("Ingrese el valor unitario el producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

#Calcular el valor total con el IVA
subtotal = Valor_unitario*cantidad
iva = subtotal * 0.16
total = subtotal + iva

#Mostrar el resultado
print("El valor total a pagar, incluyendo el 16% de IVA, es : ",total)