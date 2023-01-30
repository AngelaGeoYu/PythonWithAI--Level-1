import random
number_of_times = 100
number_of_faces = 0
counter = 1

while counter <= number_of_times:
    x = random.randint(1, 2)
    if x == 1:
        number_of_faces += 1
    counter += 1

print(f"In {number_of_times} times, I got faces {number_of_faces} times.")
print(f"It's {number_of_faces/number_of_times}.")