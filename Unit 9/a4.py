import random
colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
counter = 1
while counter < 10:
    color = random.choice(colors)
    print(color)
    counter += 1