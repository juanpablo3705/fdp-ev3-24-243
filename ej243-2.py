while True:
    try:
        cantidad_pasajes = int(input("Ingrese la cantidad de pasajes a vender: "))
        if cantidad_pasajes > 0:
            break
        else:
            print("Error. Ingrese una cantidad de pasajes positiva.")
    except ValueError:
        print("Error. Ingrese sólo números, no letras.")

total_ingresos = 0

for index in range(cantidad_pasajes):

    while True:
        try:
            precio = int(input(f"Ingresa el precio del pasaje número {index + 1}: "))
            if precio > 0:
                break
            else:
                print("Error. El precio debe ser mayor que cero.")
        except ValueError:
            print("Error. Ingrese números, no letras.")

    total_ingresos = total_ingresos + precio

print(f"El total de ingresos por la venta de los pasajes es: ${total_ingresos}.")