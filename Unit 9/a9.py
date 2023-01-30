numbers = [165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 
           941,386, 462, 47, 418, 907, 982,219,521, 344, 236, 375, 823, 
           566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237]

biggest_number = numbers[0]
for i in numbers:
    if biggest_number < i:
        biggest_number = i

print(f"The biggest number is {biggest_number}")
print('Result of max(numbers) is ' + str(max(numbers)))