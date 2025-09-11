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



# sentence = "I love Python programming"
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print(reversed_sentence)




# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []
# for x in list1:
#     if x in list2:
#         common.append(x)
# print("Common elements:", common)



nums = [12,47,90,2,0,51,75]
largest = nums[0]
smallest = nums[0]
for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest =", largest, " Smallest =", smallest)
