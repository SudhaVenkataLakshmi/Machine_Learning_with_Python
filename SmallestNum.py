numbers = [10,5,8,3,2,12]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)