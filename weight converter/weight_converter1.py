from colorama import Fore, Style, init
init(autoreset=True)

def show_menu():
    print(Fore.CYAN + "\n=== Simple Weight Converter ===")
    print(Fore.BLUE + "\nValid weight units:")
    print("kilograms: kg")
    print("grams: g")
    print("pounds: lb")
    print("metric tonne: t")
    print("milligram: mg")

def convert_weight(weight, unit, target):
    # Convert to kg (base unit)
    if unit == "kg":
        base = weight
    elif unit == "g":
        base = weight / 1000
    elif unit == "lb":
        base = weight * 0.453592
    elif unit == "t":
        base = weight * 1000
    elif unit == "mg":
        base = weight / 1000000
    else:
        return None

    # Convert from kg to target
    if target == "kg":
        return base
    elif target == "g":
        return base * 1000
    elif target == "lb":
        return base / 0.453592
    elif target == "t":
        return base / 1000
    elif target == "mg":
        return base * 1000000
    else:
        return None


# Main Program
show_menu()

try:
    weight = float(input(Fore.YELLOW + "\nEnter the weight: "))
    unit = input(Fore.YELLOW + "Enter the unit of provided weight: ").lower()
    target = input(Fore.YELLOW + "Enter the conversion unit: ").lower()

    result = convert_weight(weight, unit, target)

    if result is None:
        print(Fore.RED + "Error: Invalid unit entered")
    else:
        print(Fore.GREEN + f"\nConverted weight: {result} {target}")

except ValueError:
    print(Fore.RED + "Error: Please enter valid numbers")