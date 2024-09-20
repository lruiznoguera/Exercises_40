opciones = int(input("Escoja la opción 1. para convertir un número binario a decimal, 2. para convertir un número decimal a binario o 3. para salir "))

if opciones == 1:
    dig1 = int(input("Ingrese un dígito entre 0 y 1 "))
    dig2 = int(input("Ingrese un dígito entre 0 y 1 "))
    dig3 = int(input("Ingrese un dígito entre 0 y 1 "))
    dig4 = int(input("Ingrese un dígito entre 0 y 1 "))
    dig5 = int(input("Ingrese un dígito entre 0 y 1 "))
    numDecimal = (dig5 * 2**0) + (dig4 * 2 ** 1) + (dig3 * 2**2) + (dig2 * 2 ** 3) + (dig1 * 2 ** 4)
    print(f"Número binario: {dig1}{dig2}{dig3}{dig4}{dig5}")
    print(f"Equivalente en decimal: {numDecimal}")
else:
    if opciones == 2:
        num = int(input("Por favor ingrese un número decimal positivo menor o igual a 25 "))
        if num <= 25:
            res1 = (num // 2**4) % 2
            res2 = (num // 2**3) % 2
            res3 = (num // 2**2) % 2
            res4 = (num // 2**1) % 2
            res5 = (num // 2**0) % 2
            numBinario = f"{res1}{res2}{res3}{res4}{res5}"
            print(f"Número decimal: {num}")
            print(f"Equivalente en binario: {numBinario}")
        else:
            print("Número no válido para la conversión a binario")
    else:
        if opciones == 3:
            print("Comience nuvamente")






