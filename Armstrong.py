num = int(input("Enter any Number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")