numbers = [10, 50, 20, 80, 5]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)