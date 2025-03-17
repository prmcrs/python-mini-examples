# programs/guess_number/guess_number.py

import random

def generar_numero():
    """Genera un número aleatorio entre 1 y 1000."""
    return random.randint(1, 1000)

def main():
    print("Tengo un número entre 1 y 1000.")
    print("¿Puedes adivinar mi número?")
    jugar_otra = 's'

    while jugar_otra.lower() == 's':
        numero_secreto = generar_numero()
        print("Escribe tu primer intento.")

        while True:
            try:
                num_usuario = int(input("Introduce un número: "))

                if num_usuario == numero_secreto:
                    print("¡Excelente! ¡Adivinaste el número!")
                    break
                elif num_usuario > numero_secreto:
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    print("Demasiado bajo. Intenta de nuevo.")
            except ValueError:
                print("Por favor, introduce un número válido.")

        jugar_otra = input("¿Deseas jugar de nuevo? (s/n): ")

if __name__ == "__main__":
    main()
