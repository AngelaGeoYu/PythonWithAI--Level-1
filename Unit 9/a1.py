my_favorite_fruits = ['apple','banana','cherry']
print(my_favorite_fruits[0])
print(my_favorite_fruits[-1])
my_favorite_fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi',
'melon', 'mango']
print(my_favorite_fruits[2:5])
print(my_favorite_fruits[-4:-1])
my_favorite_fruits[1] = 'orange'
print(my_favorite_fruits[1])
if 'apple' in my_favorite_fruits :
    print("Yes, 'apple' is in the fruits list")
my_favorite_fruits.append('grape')
print(my_favorite_fruits)
print(len(my_favorite_fruits))
my_favorite_fruits.remove('apple')
your_favorite_fruits = my_favorite_fruits.copy()
print(your_favorite_fruits)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
fruits = ["banana", "apple","cherry"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)