totalCuenta = float(input("Por favor ingrese el total de la cuenta "))
numeroEscogido = int(input("Por favor ingrese el número escogido "))

if numeroEscogido >= 74:
    descuento = totalCuenta * 0.20
else:
    descuento = totalCuenta * 0.15

print(f"El descuento obtenido es ${descuento}")
print(f"El valor total a pagar es ${(totalCuenta - descuento)}")
