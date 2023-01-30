print("Let’s play! I will echo what you say.")
message = input()

message = ""

count = 0

while message != "bye":
    message= input()
    print(f"Echo...{message}")
    count = count + 1
    if (count >= 5):
        print("Let’s take a break")
        break

print("See you around!")