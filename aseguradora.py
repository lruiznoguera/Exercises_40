monto = float(input("Por favor ingrese el monto de la fianza "))

if monto <= 50000:
    cuotaCliente = monto * 0.03
else:
    cuotaCliente = monto * 0.02

print(f"La cuota a pagar por el cliente es ${cuotaCliente: .0f}")