# import string
# s = "The quick brown fox jumps over the lazy dog"
# alphabet = set(string.ascii_lowercase)
# if set(s.lower()) >= alphabet:
#     print("Pangram")
# else:
#     print("Not Pangram")



# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5)) 



# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# nums = [1, 2, 2, 3, 4, 4, 5]
# unique = []

# for n in nums:
#     if n not in unique:
#         unique.append(n)

# print("Unique elements:", unique)




# nums = [1, 2, 3, 4, 5]
# squares = [n**2 for n in nums]
# print("Squares:", squares)



sentence = "I love coding"
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print(reversed_sentence)




# list1 = [1,5,3,6,9,2,7]
# list2 = [3,4,2,6,0,9,2,5]
# common = []
# for x in list1:
#     if x in list2:
#         common.append(x)
# print("Common elements:", common)



# nums = [1,13,9,25,70,45,32,24]
# largest = nums[0]
# smallest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
#     if n < smallest:
#         smallest = n
# print("Largest =", largest, " Smallest =", smallest)



# nums = [9,25,12,6,10,38]
# smallest = sec_small = float('inf')
# for n in nums:
#     if n < smallest:
#         sec_small = smallest
#         smallest = n
#     elif n < sec_small and n != smallest:
#         sec_small = n
# print("Second smallest is =", sec_small)






# n = 28
# div_sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         div_sum += i
# if div_sum == n:
#     print(n, "is a Perfect Number")
# else:
#     print(n, "is not a Perfect Number")

