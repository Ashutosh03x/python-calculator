from colorama import Fore,Style,init
init(autoreset=True)

#valid inputs (For now)
# will try to add more units in future

supported_weights={
    "kg": "kilogram",
    "g" : "gram",
    "lb": "pounds",
    "t" : "metric tonne",
    "mg": "milligram"
}

# conversion of units in base unit (kilograms)

to_kg={
    "kg": lambda x:x,
    "g" : lambda x:x/1000,
    "lb": lambda x:x*0.453592,
    "t" : lambda x:x*1000,
    "mg" : lambda x:x/1000000
}

# conversion from base unit to target unit

Target={
    "kg": lambda x:x,
    "g" : lambda x:x*1000,
    "lb": lambda x:x/0.453592,
    "t" : lambda x:x/1000,
    "mg": lambda x:x*1000000
}

#main menu
# info about the converter ,styling etc...

def menu():
    print(Fore.LIGHTMAGENTA_EX+'''
█░█░█ █▀▀ █ █▀▀ █░█ ▀█▀   █▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ ▀█▀ █▀▀ █▀█
▀▄▀▄▀ ██▄ █ █▄█ █▀█ ░█░   █▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ░█░ ██▄ █▀▄''')
    print(Fore.CYAN+"="*63)
    print(Fore.BLUE+"\nValid Weight Units:")
    print(Fore.CYAN+"-"*20)

# used above dictionaries for keys and values

    for unit,unit_name in supported_weights.items():
        print(Fore.WHITE+f"{unit} = {unit_name}")

    print(Fore.WHITE+"-"*20)

#user input: enter the weight you want to convert

def ent_weight(prompt):
    while True:
        try:
            return float(input(Fore.YELLOW+prompt))
        except ValueError:
            print(Fore.RED+"Invalid number!")
        except Exception:
            print(Fore.RED+"Error! Unexpected")    

#user input: Enter the hte unit of the provided weight            

def ent_unit(prompt):
    while True:
        try:
            unit=input(Fore.YELLOW+prompt).strip().lower()
            if unit in supported_weights:
                return unit
            print(Fore.RED+f"Invalid unit! Use: {','.join(supported_weights.keys())}") 
        except Exception:
            print(Fore.RED+"Error! Unexpected")

# conversion process:            

def convert(weight,unit,target):
    base=to_kg[unit](weight)
    return Target[target](base)

#=========MAIN LOOP=================

while True:
    menu()
    weight=ent_weight("Enter the weight:")
    unit=ent_unit("Enter the source unit (kg/g/lb/t/mg):")
    target=ent_unit("Enter the target unit (kg/g/lb/t/mg):")

    result=convert(weight,unit,target)

    print(Fore.GREEN+f"Result:{result:.2f}{target}")


    choice=input(Fore.YELLOW+"\nConvert again? (y/n/c(clear history))?").lower()
    
    if choice=="y":
        continue
    elif choice=="c":
        print("\033c",end="")
    else:
        print("Goodbye!👋")
        break

