def primeros_auxilios():
    def evaluar_respuesta_estimulacion():
        while True:
            respuesta = input("¿Responde a Estímulos? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Valorar la necesidad de llevarlo al hospital más cercano.")
                return False
            elif respuesta == "no":
                print("Abrir la vía aérea.")
                return True
            else:
                print("Respuesta no válida, por favor ingrese 'si' o 'no'.")

    def evaluar_respiracion():
        while True:
            respuesta = input("¿Respira? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Permitirle posición de suficiente ventilación.")
                return False
            elif respuesta == "no":
                print("Administre 5 Ventilaciones y llame a una Ambulancia.")
                return True
            else:
                print("Respuesta no válida, por favor ingrese 'si' o 'no'.")

    def evaluar_signos_de_vida():
        while True:
            respuesta = input("¿Signos de Vida? (si/no): ").strip().lower()
            if respuesta == "si":
                
                return True
            elif respuesta == "no":
                
                return False
            else:
                print("Respuesta no válida, por favor ingrese 'si' o 'no'.")

    def llego_ambulancia():
        while True:
            respuesta = input("¿Llegó la Ambulancia? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Fin del procedimiento de primeros auxilios.")
                return True
            elif respuesta == "no":
                return False
            else:
                print("Respuesta no válida, por favor ingrese 'si' o 'no'.")



    if evaluar_respuesta_estimulacion():
        if evaluar_respiracion():
            while True:
                if not llego_ambulancia():
                    if not evaluar_signos_de_vida():
                        print("Administrar Compresiones Torácicas hasta que llegue la ambulancia.")
                    else:
                        print("Reevaluar a la espera de la Ambulancia.")
                else:
                    break
    

if __name__ == "__main__":
    primeros_auxilios()
