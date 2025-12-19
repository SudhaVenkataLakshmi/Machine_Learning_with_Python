n = int(input("Enter a Number: "))
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print("Sum of digits of given Number: ", total)