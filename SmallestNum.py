numbers = [20,6,9,12,10,2]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)