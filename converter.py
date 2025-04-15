def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    # Convert input to Celsius first
    if from_unit == 'celsius':
        temp_c = value
    elif from_unit == 'fahrenheit':
        temp_c = fahrenheit_to_celsius(value)
    elif from_unit == 'kelvin':
        temp_c = kelvin_to_celsius(value)
    else:
        raise ValueError("Invalid source unit")

    # Convert Celsius to target unit
    if to_unit == 'celsius':
        return temp_c
    elif to_unit == 'fahrenheit':
        return celsius_to_fahrenheit(temp_c)
    elif to_unit == 'kelvin':
        return celsius_to_kelvin(temp_c)
    else:
        raise ValueError("Invalid target unit")

def show_menu():
    print("\nTemperature Converter")
    print("---------------------")
    print("Supported units: Celsius, Fahrenheit, Kelvin")
    print("Example input: 100 Celsius to Fahrenheit")

def main():
    show_menu()
    try:
        while True:
            user_input = input("\nEnter conversion (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            parts = user_input.strip().split()
            if len(parts) != 4 or parts[2].lower() != "to":
                print("Invalid format. Please use: <value> <from_unit> to <to_unit>")
                continue

            value = float(parts[0])
            from_unit = parts[1]
            to_unit = parts[3]

            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit.capitalize()} = {result:.2f} {to_unit.capitalize()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
