n = int(input("Enter Number of Terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end= " ")
    a, b = b, a + b