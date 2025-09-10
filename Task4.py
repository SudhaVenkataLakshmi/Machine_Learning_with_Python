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



s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

