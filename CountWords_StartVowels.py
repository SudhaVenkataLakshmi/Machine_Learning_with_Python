sentence = input("Enter a Sentence: ")
words = sentence.split()
count = 0
for w in words:
    if w[0].lower() in 'aeiou':
        count += 1
print("Words Starting with Vowel: ",count)