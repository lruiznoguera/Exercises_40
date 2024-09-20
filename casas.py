ingresos = float(input("Por favor introduzca sus ingresos "))
valorCasa = float(input("Por favor ingrese el valor de la casa "))

if ingresos < 8000:
    enganche = valorCasa * 0.15
    restante = (valorCasa - enganche) / 120
else:
    enganche = valorCasa * 0.3
    restante = (valorCasa - enganche) / 84

print(f"El enganche es ${enganche: .2f} dólares")
print(f"El pago mensual es ${restante: .2f} dólares")
