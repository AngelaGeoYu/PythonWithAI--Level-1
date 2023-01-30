name = 'Angela'
print(f'Welcome to {name}’s Choose Your Own Adventure game! As you follow thestory, you will be presented with choices that decide your fate. Take care and choose wisely! Let’s begin.')
print('You find yourself in a dark room with 2 doors. The first door is red,the second is white!')
door_choice = input('which door do you want to choose? red = red door or white = white door ')

if door_choice == 'red':
    print('Great, you walk through the red door and are now in the future! You meet a scientist who gives you a mission of helping him save the world!')
choice = input('What do you want to do? 1 = Accept or 2 = Decline ')
if choice == '1':
        print("""___________SUCCESS____________
You helped the scientist save the world! In gratitude, the scientist builds a
time machine and send you home!""")
else:
        print("""___________Game Over____________
        Too bad! You declined the scientist's offer and now you are stuck in the future!""")

if door_choice == 'white':
    print('Great, you walked through the white door and now you are in the past! You meet a princess who asks you to go on quest.')
quest_choice = input('Do you want to accept her offer and go on the quest or do you want to stay where you are? 3 = Accept or 5 = Decline ')
if quest_choice == '3':
        print('The princess thanks you for accepting her offer. You begin the quest.')
else:
        print("""___________Game Over___________
        Well, I guess your story ends here!""")