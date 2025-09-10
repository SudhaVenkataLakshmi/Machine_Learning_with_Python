nums = [1, 2, 3, 2, 4, 2, 5]
x = 2
count = 0
for n in nums:
    if n == x:
        count += 1
print(x, "appears", count, "times")
