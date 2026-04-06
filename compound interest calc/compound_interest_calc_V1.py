principal=0
rate=0
time=0

while True:
    try:
        principal=float(input("Enter the principle amount:"))
        if principal<=0:
            print("Principle can't be less than or equal to zero")
        else:
            break
    except ValueError:
        print("Invalid Number!")


while True:
    try:
        rate=float(input("Enter the Interest rate (%):"))
        if rate<=0:
            print("rate can't be less than or equal to zero")
        else:
            break
    except ValueError:
        print("Invalid Number!")


while True:
    try:
        time=int(input("Enter the time in years:"))
        if time<=0:
            print("time can't be less than or equal to zero")
        else:
            break
    except ValueError:
        print("Invalid Number!")

total = principal * pow(( 1 + rate / 100),time)
print(f"\nBalance after {time} year/s: ${total:.2f}")