ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000, "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200, "Septiembre": 25000, 
    "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000,
}

Venta_mas_alta = max(ventas.values())

while True:
    try:
        monto = int(input("Ingrese un monto: "))
        if monto > Venta_mas_alta:
            print("Lo siento, el monto ingresado es superior al monto más alto en las ventas.")
            
        else:
            # Crear un nuevo diccionario que contiene solo los meses y ventas que son mayores al monto ingresado
            Respuesta = {mes: venta for mes, venta in ventas.items() if venta > monto}
            print(Respuesta)
            break  # Salir del bucle si se ha ingresado un monto válido
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
