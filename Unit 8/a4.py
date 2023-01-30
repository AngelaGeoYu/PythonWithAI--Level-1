user_input = input("Please enter a number: ")
if user_input.isdigit():
    int(user_input)
    print(f"You entered {user_input}.")
else:
    print(f"{user_input} is not a number.")