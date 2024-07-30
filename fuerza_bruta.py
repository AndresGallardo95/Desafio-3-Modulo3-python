from string import ascii_lowercase
import getpass

letras = ascii_lowercase
intentos = 0
adivinanza = ''

while True:
    # Utilizar getpass para ingresar la contraseña de forma invisible
    password = getpass.getpass("Ingrese la contraseña a evaluar: ").lower().strip()

    # Verificar si la contraseña contiene solo letras alfabéticas minúsculas
    if all(char in letras for char in password):
        break
    else:
        print("Error: Solo se aceptan contraseñas alfabéticas minúsculas. Por favor, intente nuevamente.")

for char in password:
    for letra in letras:
        intentos += 1
        if letra == char:
            adivinanza += letra
            break

print(f'Cantidad de intentos: {intentos}, Contraseña a evaluar: {password}')
