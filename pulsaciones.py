sexo = str(input("Por favor ingrese su sexo (Masculino o Femenino) "))
edad = int(input("Por favor ingrese su edad "))

if sexo == "masculino":
    numPulsaciones = (210 - edad) / 10
elif sexo == "femenino":
    numPulsaciones = (220 - edad) / 10
elif sexo != "masculino" and sexo != "femenino":
    numPulsaciones = "Escoja una de las dos opciones"


print(f"El número de pulsaciones que debe tener por cada 10 segundos de ejercicio aeróbico es {numPulsaciones}")