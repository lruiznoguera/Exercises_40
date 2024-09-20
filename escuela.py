promedio = float(input("Por favor ingrese el promedio obtenido "))
cantMaterias = int(input("Por favor ingrese la cantidad de materías a matricular "))
costoMaterias = 100
costoMatriculas = cantMaterias * costoMaterias


if promedio >= 9:
    descuento = costoMatriculas * 0.3
    total = costoMatriculas - descuento
else:
    iva = costoMatriculas * 0.1
    total = costoMatriculas + iva

print(f"El costo total a pagar es {total: .2f} Dólares")