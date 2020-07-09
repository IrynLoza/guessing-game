"""A number-guessing game."""
import random

greet = input("Hey! DO you wanna play a game?")
player_name = input("What is your name, player?")
print(f'{player_name}, I am thinking of a number between 1 and 100. Try to guess my number.')

too_low = 0
too_high = 101
counts = 0

number = random.randint(1, 101)

while True:
	try: 
		guess = int(input("What number do you want to chose?"))
		counts+= 1
		if guess > too_high or guess < too_low:
			print("Please, chose the number from 1 to 100. Try again.")
		elif guess > number:
			too_high = guess
			print("Too high, try again")
		elif guess < number:
			too_low = guess	
			print("Too low, try again")
		else: 
			print(f'Congratulation! My number is {number}! You spent {counts} attemts!')
			break

	except ValueError:
		print("Ho-ho! Not a number! Be careful and try with number from 1 to 100")
		
				







