from colorama import Fore,Style,init
init(autoreset=True)

 # main menu and heading:

 
def menu():

    print(Fore.LIGHTMAGENTA_EX+'''
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝''')
    print(Fore.CYAN+"="*83)
    print(Fore.WHITE+"Use: + - * % / // ")
    print(Fore.WHITE+"Type full expression (e.g. 2+2) or continue with something like (+3, *5, %5)")
    print(Fore.WHITE+"--> Type 'c' to CLEAR and 'q' to QUIT")
    print(Fore.CYAN+"-"*80)
menu() # called the menu function
# main loop for whole calculator
result=0
while True:
    
    expr=input(Fore.YELLOW+"Enter operation:") # takes the user input

    
    if expr=="c": # clears the previous results/history
        result=0
        print(Fore.BLUE+f"Cleared. Result=0") 
        continue

    if expr=="q":
        print(Fore.BLUE+"Goodbye!👋") #QUIT
        break


    allowed="0123456789+-/*%.()"

    if not all(char in allowed for char in expr):
        print(Fore.RED+"Unsupported expression or characters")
        continue

# 🔐 SAFETY CHECK (IMPORTANT)
# This block is used to prevent unsafe or malicious input when using eval().
#
# Why it's needed:
# The eval() function can execute ANY Python code, not just math.
# Without this check, a user could run harmful commands like:
# import("os").system("shutdown /s /t 0")
# which can damage or control the system.
#
# What it does:
# It restricts the user input to only valid mathematical characters.
#
# How it works:
# - 'allowed' contains all safe characters (numbers, operators, brackets, space)
# - 'all()' checks every character in the input
# - If ANY character is not in 'allowed', the input is rejected
#
# Result:
# Only safe math expressions like "2+2" or "*5" are allowed,
# and dangerous code execution is blocked.

    #operation starts from here

    try:
        if result==0: #if the result is zero it just execute the operation and gives the output
            result=eval(expr,{"__bulitins__":None},{})
            print(Fore.YELLOW+f"Result: {result}")
        else:
               
            full_expr=str(result)+expr # after every calculation (output) it stores the result and user can calculate further using that result 
            result=eval(full_expr,{"__bulitins__":None},{})

            print(Fore.YELLOW+f"result: {result}")
            
    except Exception:
        print(Fore.RED+"Invalid Input")  

    