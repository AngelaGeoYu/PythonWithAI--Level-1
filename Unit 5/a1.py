cher_dress_color = 'pink'
cher_shoe_color = 'white'
cher_has_earrings = True
dionne_dress_color = 'purple'
dionne_shoe_color = 'pink'
dionne_has_earrings = True

print(f"""At least one person is wearing purple?
{cher_dress_color == 'pink' or dionne_dress_color == 'purple'}
Cher and Dionne have different dress colors?
{cher_dress_color == 'pink' and dionne_dress_color == 'purple'}
Cher and Dionne are both wearing earrings?
{cher_has_earrings == True and dionne_has_earrings == True}
At least one person is wearing pink?
{cher_dress_color == 'pink' and dionne_dress_color == 'purple'}
No one is wearing green?
{not cher_dress_color == 'pink' or dionne_dress_color == 'purple'}
Cher and Dionne have the same shoe color?
{cher_shoe_color == 'white' and dionne_shoe_color == 'pink'}""")