import random
number = random.randint(1, 30)
guess = int(input("Guess: "))
if guess == number:
    print("Correct!")
else:
    print("Wrong! Number was", number)