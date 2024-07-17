import random

words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

name = input("What's your name? \n")
print(f"All  the best {name}!")

word = random.choice(words)
print(f"Word is {len(word)} characters long.")

guesses, fail = 12, 0

guessed = ""

while guesses > 0:
	print(f"You have {guesses} left.")
	guessed += char(input("Enter your guess: "))
	