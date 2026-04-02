from colorama import Fore,Style,init
init(autoreset=True)

 #valid inputs (For now)

supported_units={
    "C": "Celsius",
    "K": "Kelvin",
    "F": "Fahrenheit",
    "R": "Rankine"
}

# conversion of units in base unit (Celsius)

to_celsius={
    "C": lambda x:x,
    "K": lambda x:x-273.15,
    "F": lambda x:(x-32)*5/9,
    "R": lambda x:(x-491.67)*5/9
}

# conversion from base unit to target unit

Target={
    "C": lambda x: x,
    "K": lambda x: x + 273.15,
    "F": lambda x: (x * 9 / 5) + 32,
    "R": lambda x: (x + 273.15) * 9 / 5
}

def menu():
    print(Fore.CYAN+"\n"+"="*35)
    print(Fore.LIGHTMAGENTA_EX+"Simple Temperature Converter")
    print(Fore.CYAN+"="*35)
    print(Fore.BLUE+"\nValid Temperature Units:")
    print(Fore.CYAN+"-"*35)

    for unit,unit_name in supported_units.items():
        print(Fore.WHITE+f"{unit} = {unit_name}")
    
    print(Fore.WHITE + "-" * 35)

def ent_temp(prompt):
    while True:
        try:
            return float(input(Fore.YELLOW+prompt))
        except ValueError:
            print(Fore.RED+"Invalid number!")

def ent_unit(prompt):
    while True:
        unit=input(Fore.YELLOW+prompt).strip().upper()
        if unit in supported_units:
            return unit
        print(Fore.RED+f"Invalid unit! use: {','.join(supported_units.keys())}")


def convert(temp,unit,target):
    base=to_celsius[unit](temp)
    return Target[target](base)


#=========MAIN LOOP=================

while True:
    menu()
    temp=ent_temp("Enter Temperature:")
    unit=ent_unit("Enter the source unit (C/K/R/F):")
    target=ent_unit("Enter target unit (C/K/R/F):")

    result=convert(temp,unit,target)

    print(Fore.GREEN+f"Result: {result:.2f}{target}")

    choice=input(Fore.YELLOW+"\nConvert again? (y/n)?").lower()
    
    if choice=="y":
        continue
    else:
        print("Goodbye!")
        break




            

