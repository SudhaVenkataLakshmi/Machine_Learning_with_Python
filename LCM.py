a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
def gcd(x,y):
    while y:
        x,y = y, x % y
    return x
lcm = (a * b) // gcd(a,b)
print("LCM is: ",lcm)