import string
s = "The quick brown fox jumps over the lazy dog"
alphabet = set(string.ascii_lowercase)
if set(s.lower()) >= alphabet:
    print("Pangram")
else:
    print("Not Pangram")
