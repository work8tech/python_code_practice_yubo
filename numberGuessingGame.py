import random
import math

# game will have ceil(log(upper - lower +1, base 2)) turns

lower = int(input("Enter lower bound number:- "))
upper = int(input("Enter upper bound number:- "))

number = random.randint(lower, upper)

chances = math.ceil(math.log(upper - lower +1, 2))

print(f"\nYou have {chances} chances\n")

count = 0

#initialising flag at False

flag = False

while (count < chances):

	count += 1

	trial = int(input(f"Guess number {count} - "))
	
	if trial == number:
		print("You are absolutely right!")
		flag = True
		break

	elif trial > number:
		print("Too big. Try smaller.")

	else:
		print("Too small. Try bigger.")

if not flag:

	print(f"You are out of chances, number is {number}")