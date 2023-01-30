def menu():
    display = """
Please select from the menu
A or a to Add customer
L or l to List customer
Q or q to exit
""" 
    print(display)

def addcustomer():
    print("=======in add customer function=======")

def listcustomers():
    print("=======in list customers function=======")

while True:
    menu()
    user_input = input("")
    if user_input == "A" or user_input == "a":
        addcustomer()
    elif user_input == "L" or user_input == "l":
        listcustomers()
    elif user_input == "Q" or user_input == "q":
        break
    else:
        print("Invalid option")