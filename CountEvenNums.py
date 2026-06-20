numbers = [10,2,3,4,8,11,19,20]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Count =", count)