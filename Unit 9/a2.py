favourite_things = []
print('Hi, tell me 5 of your favourite things. ')
counter = 1
while counter <= 5:
    thing = input(f"OK, favourite {counter}: ")
    favourite_things.append(thing)
    counter += 1
print("Here are your favourite things.")
print(favourite_things)