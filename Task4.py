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

# print(factorial(7)) 



# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# nums = [4,3,5,6,4,3,9,8,12,4]
# unique = []
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print("Unique elements:", unique)




# nums = [8,4,9,13,17,25]
# squares = [n**2 for n in nums]
# print("Squares:", squares)



# sentence = "Practice Makes Man Perfect"
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print(reversed_sentence)




# list1 = [1,5,7,9,3,2,4,7]
# list2 = [3,6,9,7,2,1,5]
# common = []
# for x in list1:
#     if x in list2:
#         common.append(x)
# print("Common elements:", common)



# nums = [11,5,7,90,23,50,12,12,7,9]
# largest = nums[0]
# smallest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
#     if n < smallest:
#         smallest = n
# print("Largest =", largest, " Smallest =", smallest)



# nums = [10,20,35,6,12,82,95,12,60]
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




a = 15
b = 8
result = 1
for i in range(b):
    result *= a
print("Power = ", result)



# s = "Practice Makes Man Perfect"
# upper = lower = 0
# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# print("Uppercase = ",upper, "Lowercase = ",lower)





# nums = [10,45,7,92,12,60,35]
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




# n = int(input("Enter number: "))
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




# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for ch in s:
#     if ch in vowels:
#         count += 1

# print("Vowel count =", count)

