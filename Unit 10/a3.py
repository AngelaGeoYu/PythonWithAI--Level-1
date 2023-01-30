def calculate(principal, interest):
    total = principal * (1+interest)
    return total

deposit = 1000
rate = 15/100
total = calculate(deposit,rate)
print(f"Total is {total}.")

value = calculate(1000, 15/100)
print(f"Your total is {value}")