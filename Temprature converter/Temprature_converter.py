from colorama import Fore,Style,init
init(autoreset=True)

def menu():
    print(Fore.CYAN+"\n===Simple Temprature Converter===")
    print(Fore.BLUE+"\n==>Valid Temperature units")
    print(Fore.WHITE+"Celsius: C\nFahrenheit:F\nKelvin:K\nRankine:R")

def Temp_convert(temp,unit,target_unit):
    if unit=="C":
        base=temp
    elif unit=="K":
        base=temp-273.15
    elif unit=="F":
        base=(temp-32)*5/9
    elif unit=="R":
        base=(temp-491.67)*5/9    
    else:
        return None    

# conversion from base(celcius) to target_unit        

    if target_unit=="C":
        return base
    elif target_unit=="K":
        return base+273.15
    elif target_unit=="F":
        return (base*9/5)+32
    elif target_unit=="R":
        return (base+273.15)*9/5
    else:
        return None
menu()    

try:
    temp=float(input(Fore.YELLOW+"Enter the Temprature:"))
    unit=input(Fore.YELLOW+"Enter the unit of provided Temprature:").upper()
    target_unit=input(Fore.YELLOW+"Enter the conversion unit:").upper()

    result=Temp_convert(temp,unit,target_unit)
    
    if result is None:
        print(Fore.RED + "Error: Invalid unit entered")
    else:
        print(Fore.GREEN + f"\nConverted temperature: {result} {target_unit}") 

except ValueError:
    print(Fore.RED + "Error: Please enter valid numbers")          
    
        