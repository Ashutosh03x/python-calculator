# python calculator (Level: Novice)

from colorama import Fore,Style,init
init(autoreset=True)

print(Fore.CYAN+"\n===Simple Calculator===")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %, **): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "**":
        result = num1 ** num2

    elif operator == "/":
        if num2 == 0:
            print(Fore.RED+"Error: Cannot divide by zero")
        else:
            result = num1 / num2

    elif operator == "%":
        if num2 == 0:
            print(Fore.RED+"Error: Cannot modulo by zero")
        else:
            result = num1 % num2

    else:
        print(Fore.RED+"Error: Invalid operator")

    print(Fore.GREEN+f"Result: {result}")

except ValueError:
    print(Fore.RED+"Error: Please enter valid numbers")

except Exception:
    print(Fore.RED+"Unexpected error:")

    


