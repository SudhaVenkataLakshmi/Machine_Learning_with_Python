# import string
# s = "Pack my box with five dozen liquor jugs"
# alphabet = set(string.ascii_lowercase)
# if set(s.lower()) >= alphabet:
#     print("Given sentence is Pangram")
# else:
#     print("Given Senetence is Not a Pangram")



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(15)) 



# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# nums = [2,4,6,2,3,4,6]
# unique = []
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print("Unique elements:", unique)




# nums = [16,23,9,35]
# squares = [n**2 for n in nums]
# print("Squares:", squares)



# sentence = "Python Problem Solving"
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print(reversed_sentence)




# list1 = [1,5,5,6,9,0,2,1,3,1,4,6,3,2]
# list2 = [3,3,5,4,4,6,7,9,2,3,4,6,8,0,4]
# common = []
# for x in list1:
#     if x in list2:
#         common.append(x)
# print("Common elements:", common)



# nums = [9,45,27,88,30,26,12,6,2,89]
# largest = nums[0]
# smallest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
#     if n < smallest:
#         smallest = n
# print("Largest =", largest, " Smallest =", smallest)



# nums = [12,5,90,27,3,66,99,36]
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




# a = 7
# b = 6
# result = 1
# for i in range(b):
#     result *= a
# print("Power = ", result)



# s = "Python Programming Language"
# upper = lower = 0
# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# print("Uppercase = ",upper, "Lowercase = ",lower)





# nums = [100,11,37,68,90,123,9]
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



