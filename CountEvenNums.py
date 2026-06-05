numbers = [20,50,30,34,23,21,11,7,9,12]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Count =", count)