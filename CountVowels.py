s = input("Enter any String: ")
count = 0
for ch in s.lower():
    if ch in 'aeiou':
        count += 1
print("Count of Vowels in Given String: ",count)