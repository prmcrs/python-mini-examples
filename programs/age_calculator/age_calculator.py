from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    # Ajustar si la fecha de nacimiento aún no ha ocurrido este año
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def calculate_decade(birth_date):
    # Obtener la década de nacimiento
    decade_start = (birth_date.year // 10) * 10
    return decade_start

def main():
    birth_date_input = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
        age = calculate_age(birth_date)
        decade = calculate_decade(birth_date)
        print(f"Tienes {age} años.")
        print(f"Naciste en la década de {decade}.")
    except ValueError:
        print("Formato de fecha no válido. Por favor, introduce la fecha como YYYY-MM-DD.")

if __name__ == "__main__":
    main()
