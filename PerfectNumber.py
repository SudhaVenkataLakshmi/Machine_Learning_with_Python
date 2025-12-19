n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("It is Perfect Number")
else:
    print("It is Not Perfect Number")



