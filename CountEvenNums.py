numbers = [12,5,9,3,15,10,9]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Count =", count)