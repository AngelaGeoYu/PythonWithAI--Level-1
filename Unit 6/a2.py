print("Let’s play! I will echo what you say.")
message = input()

message = ""

while message != "bye":
    message= input()
    print(f"Echo...{message}")

print("See you around!")