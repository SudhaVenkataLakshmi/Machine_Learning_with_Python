n = int(input("Enter number: "))
if n <= 1:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
