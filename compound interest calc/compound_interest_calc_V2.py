
def positive_number(prompt):
    while True:
        try:
            value=float(input(prompt))
            if value<=0:
                print("Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid number!")

principal = positive_number("Enter the principal amount: ")
rate = positive_number("Enter the interest rate: ")
time = positive_number("Enter the time in years: ")

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")            