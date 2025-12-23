# import string
# s = "Pack my box with five dozen liquor jugs"
# alphabet = set(string.ascii_lowercase)
# if set(s.lower()) >= alphabet:
#     print("Given sentence is Pangram")
# else:
#     print("Given Senetence is Not a Pangram")



# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(6)) 



# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# nums = [3,5,4,5,3,5,4,6,7]
# unique = []
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print("Unique elements:", unique)




nums = [10,9,6,12,15,17]
squares = [n**2 for n in nums]
print("Squares are:", squares)



# sentence = "Practice Makes Man Perfect"
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print(reversed_sentence)




# list1 = [11,11,6,8,9,3]
# list2 = [8,7,5,4,11,9]
# common = []
# for x in list1:
#     if x in list2:
#         common.append(x)
# print("Common elements:", common)



# nums = [11,50,9,15,12,8,4]
# largest = nums[0]
# smallest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
#     if n < smallest:
#         smallest = n
# print("Largest =", largest, " Smallest =", smallest)



# nums = [12,10,9,5,7,3]
# smallest = sec_small = float('inf')
# for n in nums:
#     if n < smallest:
#         sec_small = smallest
#         smallest = n
#     elif n < sec_small and n != smallest:
#         sec_small = n
# print("Second smallest is =", sec_small)






# n = 496
# div_sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         div_sum += i
# if div_sum == n:
#     print(n, "is a Perfect Number")
# else:
#     print(n, "is not a Perfect Number")




# a = 45
# b = 2
# result = 1
# for i in range(b):
#     result *= a
# print("Power = ", result)



# s = "Practice Makes Man Perfect"
# upper = lower = 0
# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# print("Uppercase = ",upper, "Lowercase = ",lower)





# nums = [8,13,57,80,15,36]
# even_sum = odd_sum = 0
# for n in nums:
#     if n % 2 == 0:
#         even_sum += n
#     else:
#         odd_sum += n
# print("Even Sum = ",even_sum, "Odd Sum = ",odd_sum)



# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
# for i in range(7):
#     print(fib(i),end= " ")



# s = "mississippi"
# freq ={}
# for ch in s:
#     freq[ch] = freq.get(ch,0)+1
# max_char = max(freq, key=freq.get)
# print("Most Frequent char = ",max_char)



# a = int(input("Enter first: "))
# b = int(input("Enter second: "))
# c = int(input("Enter third: "))

# print("Maximum is:", max(a, b, c))




# n = int(input("Enter number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print("Factorial =", fact)




# n = int(input("Enter any number: "))
# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")




# s = input("Enter any string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for ch in s:
#     if ch in vowels:
#         count += 1

# print("Vowel count =", count)



# import random
# num = random.randint(1, 10)
# guess = int(input("Guess any number (1-10): "))
# if guess == num:
#     print("Correct! You guessed it.")
# else:
#     print("Wrong! The number was", num)



# ch = input("Enter any Letter: ").lower()

# if ch in "aeiou":
#     print("It is Vowel")
# else:
#     print("It is Consonant")



# s = input("Enter any String: ")
# count = 0
# for ch in s:
#     count += 1
# print("Length of Given String =", count)



# n = int(input("Enter any Number: "))

# if n > 0:
#     print("It is Positive")
# elif n < 0:
#     print("It is Negative")
# else:
#     print("It is Zero")




# n = int(input("Enter a Number: "))
# if n % 5 == 0 and n % 11 == 0:
#     print("It is Divisible by 5 and 11")
# else:
#     print("It is not Divisible by 5 and 11")


# n = int(input("Enter any Number: "))
# print("Square of Given Number = ", n**2)
# print("Cube of Given Number = ", n**3)


# ch = input("Enter any Character: ")
# if ch.isalpha():
#     print("It is an Alphabet.")
# elif ch.isdigit():
#     print("It is a Digit.")
# else:
#     print("It is a Special Character.")


# n = int(input("Enter n value:"))
# total = 0
# for i in range(2, n+1, 2):
#     total += i
# print("Sum of",n,"even Numbers= ",total)




# s = input("Enter any Sentence:")
# count = 0
# for ch in s:
#     if ch == " ":
#         count += 1
# print("Spaces= ",count)



# p = float(input("Enter Principal: "))
# r = float(input("Enter Rate: "))
# t = float(input("Enter Time(in Years): "))
# ci = p * ((1 + r/100) ** t) - p
# print("Compound Interest is= ",ci)



# n = int(input("Enter any Number: "))
# total = 0
# for i in range (1, n+1, 2):
#     total += i
# print("Sum of Odd Numbers: ",total)



# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     return f

# n = int(input("Enter any Number: "))
# temp = n
# s = 0

# while temp > 0:
#     digit = temp % 10
#     s += fact(digit)
#     temp //= 10

# if s == n:
#     print("It is a Strong Number")
# else:
#     print("It is Not a Strong Number")



# n = int(input("Enter any Number: "))

# print("Factors of", n, "are:")
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=" ")



# import math

# n = int(input("Enter number: "))

# if int(math.sqrt(n))**2 == n:
#     print("Perfect Square")
# else:
#     print("Not a Perfect Square")



# n = int(input("Enter any Number: "))
# count = 0

# while n > 0:
#     n //= 10
#     count += 1

# print("Number of digits =", count)



# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))

# max_num = max(a, b)
# while True:
#     if max_num % a == 0 and max_num % b == 0:
#         print("LCM of Given Numbers =", max_num)
#         break
#     max_num += 1
