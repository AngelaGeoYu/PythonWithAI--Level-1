import random
magic_number = random.randint(1, 10)
max_tries = 3
counter = 1
print(f"Let's play the magic number. I had a number between {min} and {max} in my mind.")

while counter <= max_tries:
    guess = input("Guess a number between 1 and 10 \n")
    guess = int(guess)
    if guess == magic_number:
        print("Congratulations, you got it!")
        break
    elif guess <= magic_number:
        print("Too low, try again.")
    elif guess >= magic_number:
        print("Too high, try again.")
    else:
        print("Something weird happened")
    counter += 1

print(f"The magic number is {magic_number}!")