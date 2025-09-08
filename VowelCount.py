text = input("Enter text: ")
vowels = "AEIOUaeiou"
v_count = 0
for ch in text:
    if ch in vowels:
        v_count += 1
print("Vowel count: ", v_count)