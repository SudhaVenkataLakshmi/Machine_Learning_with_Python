# for num in range(1,1001):
#     order = len(str(num))
#     s = sum(int(d)**order for d in str(num))
#     if s == num:
#         print(num, end= " ")


# import math
# for num in range(1, 501):
#     s = sum(math.factorial(int(d)) for d in str(num))
#     if s == num:
#         print(num, end= " ")


# def magic_number(n):
#     while n > 9:
#         n = sum(int(d) for d in str(n))
#         return n == 1
# num = int(input("Enter Any Number: "))
# print("It is Magic Number" if magic_number(num) else "It is Not Magic Number")


# num = int(input("Enter any Number: "))
# sq = num ** 2
# if str(sq).endswith(str(num)):
#     print("Automorphic Number")
# else:
#     print("Not Automorphic Number")


# num = int(input("Enter any Number: "))
# s = sum(int(d) for d in str(num))
# if num % s == 0:
#     print("Harshad Number")
# else:
#     print("Not a Harshad Number")


# import math
# num = int(input("Enter any Number: "))
# sum_fact = sum(math.factorial(int(d)) for d in str(num))
# sum_sq = sum(int(d) for d in str(num)) ** 2
# if sum_fact == sum_sq:
#     print("Special Number")
# else:
#     print("Not a Special Number")



# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# a, b = 12, 18
# print("GCD:", gcd(a, b))
# print("LCM:", lcm(a, b))


# n = 5
# for i in range(1, n+1, 2):
#     print(" " * ((n-i)//2) + "*" * i)
# for i in range(n-2, 0, -2):
#     print(" " * ((n-i)//2) + "*" * i)



# num = int(input("Enter any Number: "))
# i = 2
# factors = []
# while num > 1:
#     if num % i == 0:
#         factors.append(i)
#         num //= i
#     else:
#         i += 1
# print("Prime Factors are:", factors)



num = input("Enter any Number: ")
s = sum(int(d) for d in num)
p = 1
for d in num:
    p *= int(d)
if s == p:
    print("Spy Number")
else:
    print("Not Spy Number")
