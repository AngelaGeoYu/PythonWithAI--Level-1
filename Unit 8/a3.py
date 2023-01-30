import random
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
departure_city = input('Please enter your departure city: ')
destination_city = input('Please enter your destination city: ')
travel_date = input('Please enter your travel date: ')
first_name = first_name.upper()
last_name = last_name.upper()
departure_city = departure_city.upper()
destination_city = destination_city.upper()
travel_date = travel_date.upper()
seat = random.randint(100,300)
print('Here is your flight ticket')
print(f"""{first_name} {last_name}
FROM {departure_city} TO {destination_city} ON {travel_date}
SEAT {seat}""")