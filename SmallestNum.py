numbers = [12,5,9,7,3,10,15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)