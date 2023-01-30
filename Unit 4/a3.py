butter_for_4 = 3/4
raito = 50/4
butter_for_50 = raito * butter_for_4

white_sugar_for_4 = 3/2
white_sugar_for_50 = raito * white_sugar_for_4

eggs_for_4 = 3
eggs_for_50 = raito * eggs_for_4

vanilla_extract_for_4 = 1
vanilla_extract_for_50 = raito * vanilla_extract_for_4

sour_milk_for_4 = 3/4
sour_milk_for_50 = raito * sour_milk_for_4

flour_for_4 = 5/2
flour_for_50 = raito * flour_for_4
result = f"""
To serve 50 people, you will need
{butter_for_50} cups of butter
{white_sugar_for_50} cups of white sugar
{eggs_for_50} eggs
{vanilla_extract_for_50} teaspoon vanilla extract
{sour_milk_for_50} cup sour milk
{flour_for_50} cup of all-purpose flour
"""
print(result)