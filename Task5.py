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
#     print("Given Number is Harshad Number")
# else:
#     print("Given Number is Not a Harshad Number")


# import math
# num = int(input("Enter any Number: "))
# sum_fact = sum(math.factorial(int(d)) for d in str(num))
# sum_sq = sum(int(d) for d in str(num)) ** 2
# if sum_fact == sum_sq:
#     print("Given Number is Special Number")
# else:
#     print("Given Number is Not a Special Number")



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = 15,9
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))


# n = 5
# for i in range(1, n+1, 2):
#     print(" " * ((n-i)//2) + "*" * i)
# for i in range(n-2, 0, -2):
#     print(" " * ((n-i)//2) + "*" * i)



# num = int(input("Enter a Number: "))
# i = 2
# factors = []
# while num > 1:
#     if num % i == 0:
#         factors.append(i)
#         num //= i
#     else:
#         i += 1
# print("Prime Factors of Given Number are:", factors)



# num = input("Enter any Number: ")
# s = sum(int(d) for d in num)
# p = 1
# for d in num:
#     p *= int(d)
# if s == p:
#     print("Given Number is Spy Number")
# else:
#     print("Given Number is Not Spy Number")



# num = int(input("Enter any Number:"))
# sq = num ** 2
# if sum(int(d) for d in str(sq)) == num:
#     print("Noen Number")
# else:
#     print("Not a Noen Number")


# num = input("Enter any Number: ")
# if '0' in num[1:]:
#     print("Duck Number.")
# else:
#     print("Not a Duck Number.")



# n = int(input("Enter number of rows: "))
# for i in range(1, n + 1):
#     print("* " * i)


# nums = [7,8,4,6,3,2]
# nums[0], nums[-1] = nums[-1], nums[0]
# print(nums)


# rows = 10
# for i in range(1, rows + 1):
#     print("  " * (rows - i) + "* " * i)


# sentence = input("Enter any sentence: ")
# words = sentence.split()
# words.sort()
# print("Sorted words are:", words)

