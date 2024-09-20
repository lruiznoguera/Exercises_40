superficie = float(input("Por favor ingrese el número de hectáreas a reforestar "))

if superficie > 100:
    pino = superficie * 0.7
    oyamel = superficie * 0.2
    cedro = superficie * 0.1
else:
    pino = superficie * 0.5
    oyamel = superficie * 0.3
    cedro = superficie * 0.2

