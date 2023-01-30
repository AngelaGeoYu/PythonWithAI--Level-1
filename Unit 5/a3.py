a = input("Please enter a number for a: ")
a = int(a)
b = input("Please enter a number for b: ")
b = int(b)
if a > b:
    print(f" a({a}) is greater than b({b}).")
elif a == b:
    print(f" a({a}) is equal to b({b}).")
else:
    print(f" a({a}) is less than b({b}).")