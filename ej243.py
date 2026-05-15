while True:
    try:
        cantidad_pasajes = int(input("¿Cuántos pasajes deseas vender?: "))
        break
    except ValueError:
        print("Error. Ingrese un valor numérico entero.")

precio_total = 0

for contador in range(cantidad_pasajes):
    while True:
        try:
            precio = int(input(f"Ingresa el precio del pasaje {contador+1}: "))
            precio_total = precio_total + precio
            break
        except ValueError:
            print("Error. Ingrese un valor numérico entero.")

print(f"El precio total de los {cantidad_pasajes} pasajes es: ${precio_total}")