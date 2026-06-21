numbers = [5,9,8,2,12,10,11,20,15,23]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Count =", count)