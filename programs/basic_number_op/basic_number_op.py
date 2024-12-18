def sumar_numeros():
    numero1 = int(input("Escriba el primer entero: "))
    numero2 = int(input("Escriba el segundo entero: "))
    print(f"La suma es {numero1 + numero2}")

def comparar_numeros():
    numero1 = int(input("Escriba el primer entero: "))
    numero2 = int(input("Escriba el segundo entero: "))
    if numero1 == numero2:
        print(f"{numero1} == {numero2}")
    if numero1 != numero2:
        print(f"{numero1} != {numero2}")
    if numero1 < numero2:
        print(f"{numero1} < {numero2}")
    if numero1 > numero2:
        print(f"{numero1} > {numero2}")
    if numero1 <= numero2:
        print(f"{numero1} <= {numero2}")
    if numero1 >= numero2:
        print(f"{numero1} >= {numero2}")

def calcular_producto():
    x = int(input("Escriba el primer entero: "))
    y = int(input("Escriba el segundo entero: "))
    z = int(input("Escriba el tercer entero: "))
    print(f"El producto es {x * y * z}")

def main():
    while True:
        print("Seleccione una opción:")
        print("1. Sumar dos números")
        print("2. Comparar dos números")
        print("3. Calcular el producto de tres números")
        print("4. Salir")
        opcion = input("Ingrese su elección: ")

        if opcion == "1":
            sumar_numeros()
        elif opcion == "2":
            comparar_numeros()
        elif opcion == "3":
            calcular_producto()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
