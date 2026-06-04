numbers = [12,5,7,9,13,11,10,15,8]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Count =", count)