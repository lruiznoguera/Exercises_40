cantLlantas = int(input("Ingrese la cantidad de llantas que desea comprar "))

if cantLlantas < 5:
    total = cantLlantas * 800
else:
    total = cantLlantas * 700

print("El total a pagar es ",total )
