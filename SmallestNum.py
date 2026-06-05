numbers = [2,6,8,12,20,50,1,16]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)