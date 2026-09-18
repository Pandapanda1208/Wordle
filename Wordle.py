import os
import random
import sys
import json

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

with open('words.json', 'r') as f:
	data = json.load(f)


clear()

reset = '\033[0m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'

def print_one():
	global guess_one, word, red, green, yellow, reset, correct
	clear()
	correct = 0
	if guess_one.lower()[0] == word[0]:
		print(green + word[0] + reset, end=' ')
		correct += 1
	elif guess_one.lower()[0] in word:
		print(yellow + guess_one.lower()[0] + reset, end=' ')
	else:
		print(red + guess_one.lower()[0] + reset, end=' ')

	if guess_one.lower()[1] == word[1]:
		print(green + word[1] + reset, end=' ')
		correct += 1
	elif guess_one.lower()[1] in word:
		print(yellow + guess_one.lower()[1] + reset, end=' ')
	else:
		print(red + guess_one.lower()[1] + reset, end=' ')

	if guess_one.lower()[2] == word[2]:
		print(green + word[2] + reset, end=' ')
		correct += 1
	elif guess_one.lower()[2] in word:
		print(yellow + guess_one.lower()[2] + reset, end=' ')
	else:
		print(red + guess_one.lower()[2] + reset, end=' ')

	if guess_one.lower()[3] == word[3]:
		print(green + word[3] + reset, end=' ')
		correct += 1
	elif guess_one.lower()[3] in word:
		print(yellow + guess_one.lower()[3] + reset, end=' ')
	else:
		print(red + guess_one.lower()[3] + reset, end=' ')

	if guess_one.lower()[4] == word[4]:
		print(green + word[4] + reset, end=' ')
		correct += 1
	elif guess_one.lower()[4] in word:
		print(yellow + guess_one.lower()[4] + reset, end=' ')
	else:
		print(red + guess_one.lower()[4] + reset, end=' ')

def print_two():
	global guess_two, word, red, green, yellow, reset, correct
	correct = 0
	if guess_two.lower()[0] == word[0]:
		print(green + word[0] + reset, end=' ')
		correct += 1
	elif guess_two.lower()[0] in word:
		print(yellow + guess_two.lower()[0] + reset, end=' ')
	else:
		print(red + guess_two.lower()[0] + reset, end=' ')

	if guess_two.lower()[1] == word[1]:
		print(green + word[1] + reset, end=' ')
		correct += 1
	elif guess_two.lower()[1] in word:
		print(yellow + guess_two.lower()[1] + reset, end=' ')
	else:
		print(red + guess_two.lower()[1] + reset, end=' ')

	if guess_two.lower()[2] == word[2]:
		print(green + word[2] + reset, end=' ')
		correct += 1
	elif guess_two.lower()[2] in word:
		print(yellow + guess_two.lower()[2] + reset, end=' ')
	else:
		print(red + guess_two.lower()[2] + reset, end=' ')

	if guess_two.lower()[3] == word[3]:
		print(green + word[3] + reset, end=' ')
		correct += 1
	elif guess_two.lower()[3] in word:
		print(yellow + guess_two.lower()[3] + reset, end=' ')
	else:
		print(red + guess_two.lower()[3] + reset, end=' ')

	if guess_two.lower()[4] == word[4]:
		print(green + word[4] + reset, end=' ')
		correct += 1
	elif guess_two.lower()[4] in word:
		print(yellow + guess_two.lower()[4] + reset, end=' ')
	else:
		print(red + guess_two.lower()[4] + reset, end=' ')

def print_three():
	global guess_three, word, red, green, yellow, reset, correct
	correct = 0
	if guess_three.lower()[0] == word[0]:
		print(green + word[0] + reset, end=' ')
		correct += 1
	elif guess_three.lower()[0] in word:
		print(yellow + guess_three.lower()[0] + reset, end=' ')
	else:
		print(red + guess_three.lower()[0] + reset, end=' ')

	if guess_three.lower()[1] == word[1]:
		print(green + word[1] + reset, end=' ')
		correct += 1
	elif guess_three.lower()[1] in word:
		print(yellow + guess_three.lower()[1] + reset, end=' ')
	else:
		print(red + guess_three.lower()[1] + reset, end=' ')

	if guess_three.lower()[2] == word[2]:
		print(green + word[2] + reset, end=' ')
		correct += 1
	elif guess_three.lower()[2] in word:
		print(yellow + guess_three.lower()[2] + reset, end=' ')
	else:
		print(red + guess_three.lower()[2] + reset, end=' ')

	if guess_three.lower()[3] == word[3]:
		print(green + word[3] + reset, end=' ')
		correct += 1
	elif guess_three.lower()[3] in word:
		print(yellow + guess_three.lower()[3] + reset, end=' ')
	else:
		print(red + guess_three.lower()[3] + reset, end=' ')

	if guess_three.lower()[4] == word[4]:
		print(green + word[4] + reset, end=' ')
		correct += 1
	elif guess_three.lower()[4] in word:
		print(yellow + guess_three.lower()[4] + reset, end=' ')
	else:
		print(red + guess_three.lower()[4] + reset, end=' ')

def print_four():
	global guess_four, word, red, green, yellow, reset, correct
	correct = 0
	if guess_four.lower()[0] == word[0]:
		print(green + word[0] + reset, end=' ')
		correct += 1
	elif guess_four.lower()[0] in word:
		print(yellow + guess_four.lower()[0] + reset, end=' ')
	else:
		print(red + guess_four.lower()[0] + reset, end=' ')

	if guess_four.lower()[1] == word[1]:
		print(green + word[1] + reset, end=' ')
		correct += 1
	elif guess_four.lower()[1] in word:
		print(yellow + guess_four.lower()[1] + reset, end=' ')
	else:
		print(red + guess_four.lower()[1] + reset, end=' ')

	if guess_four.lower()[2] == word[2]:
		print(green + word[2] + reset, end=' ')
		correct += 1
	elif guess_four.lower()[2] in word:
		print(yellow + guess_four.lower()[2] + reset, end=' ')
	else:
		print(red + guess_four.lower()[2] + reset, end=' ')

	if guess_four.lower()[3] == word[3]:
		print(green + word[3] + reset, end=' ')
		correct += 1
	elif guess_four.lower()[3] in word:
		print(yellow + guess_four.lower()[3] + reset, end=' ')
	else:
		print(red + guess_four.lower()[3] + reset, end=' ')

	if guess_four.lower()[4] == word[4]:
		print(green + word[4] + reset, end=' ')
		correct += 1
	elif guess_four.lower()[4] in word:
		print(yellow + guess_four.lower()[4] + reset, end=' ')
	else:
		print(red + guess_four.lower()[4] + reset, end=' ')

def print_five():
	global guess_five, word, red, green, yellow, reset, correct
	correct = 0
	if guess_five.lower()[0] == word[0]:
		print(green + word[0] + reset, end=' ')
		correct += 1
	elif guess_five.lower()[0] in word:
		print(yellow + guess_five.lower()[0] + reset, end=' ')
	else:
		print(red + guess_five.lower()[0] + reset, end=' ')

	if guess_five.lower()[1] == word[1]:
		print(green + word[1] + reset, end=' ')
		correct += 1
	elif guess_five.lower()[1] in word:
		print(yellow + guess_five.lower()[1] + reset, end=' ')
	else:
		print(red + guess_five.lower()[1] + reset, end=' ')

	if guess_five.lower()[2] == word[2]:
		print(green + word[2] + reset, end=' ')
		correct += 1
	elif guess_five.lower()[2] in word:
		print(yellow + guess_five.lower()[2] + reset, end=' ')
	else:
		print(red + guess_five.lower()[2] + reset, end=' ')

	if guess_five.lower()[3] == word[3]:
		print(green + word[3] + reset, end=' ')
		correct += 1
	elif guess_five.lower()[3] in word:
		print(yellow + guess_five.lower()[3] + reset, end=' ')
	else:
		print(red + guess_five.lower()[3] + reset, end=' ')

	if guess_five.lower()[4] == word[4]:
		print(green + word[4] + reset, end=' ')
		correct += 1
	elif guess_five.lower()[4] in word:
		print(yellow + guess_five.lower()[4] + reset, end=' ')
	else:
		print(red + guess_five.lower()[4] + reset, end=' ')

def print_six():
	global guess_six, word, red, green, yellow, reset, correct
	correct = 0
	if guess_six.lower()[0] == word[0]:
		print(green + word[0] + reset, end=' ')
		correct += 1
	elif guess_six.lower()[0] in word:
		print(yellow + guess_six.lower()[0] + reset, end=' ')
	else:
		print(red + guess_six.lower()[0] + reset, end=' ')

	if guess_six.lower()[1] == word[1]:
		print(green + word[1] + reset, end=' ')
		correct += 1
	elif guess_six.lower()[1] in word:
		print(yellow + guess_six.lower()[1] + reset, end=' ')
	else:
		print(red + guess_six.lower()[1] + reset, end=' ')

	if guess_six.lower()[2] == word[2]:
		print(green + word[2] + reset, end=' ')
		correct += 1
	elif guess_six.lower()[2] in word:
		print(yellow + guess_six.lower()[2] + reset, end=' ')
	else:
		print(red + guess_six.lower()[2] + reset, end=' ')

	if guess_six.lower()[3] == word[3]:
		print(green + word[3] + reset, end=' ')
		correct += 1
	elif guess_six.lower()[3] in word:
		print(yellow + guess_six.lower()[3] + reset, end=' ')
	else:
		print(red + guess_six.lower()[3] + reset, end=' ')

	if guess_six.lower()[4] == word[4]:
		print(green + word[4] + reset, end=' ')
		correct += 1
	elif guess_six.lower()[4] in word:
		print(yellow + guess_six.lower()[4] + reset, end=' ')
	else:
		print(red + guess_six.lower()[4] + reset, end=' ')



word = random.choice(data['words'])

for i in range(6):
	print('* * * * *')

guess_one = input("What's your guess?")

while len(guess_one) != 5:
	print('That is not the right length.')
	guess_one = input("What's your guess?")

correct = 0

clear()

print_one()
print()

for i in range(5):
	print('* * * * *')

if correct == 5:
	print ('Yay You guessed it in one try!')
	input()
	sys.exit(0)

guess_two = input("What's your guess?")

while len(guess_two) != 5:
	print('That is not the right length.')
	guess_two = input("What's your guess?")

correct = 0

print_one()
print()
print_two()
print()

for i in range(4):
	print('* * * * *')

if correct == 5:
	print('Yay You guessed it in two tries!')
	input()
	sys.exit(0)

guess_three = input("What's your guess?")

while len(guess_three) != 5:
	print('That is not the right length.')
	guess_three = input("What's your guess?")

correct = 0

print_one()
print()
print_two()
print()
print_three()
print()

for i in range(3):
	print('* * * * *')

if correct == 5:
	print('Yay You guessed it in three tries!')
	input()
	sys.exit(0)

guess_four = input("What's your guess")

while len(guess_four) != 5:
	print('That is not the right length.')
	guess_four = input("What's your guess")

correct = 0

print_one()
print()
print_two()
print()
print_three()
print()
print_four()
print()

for i in range(2):
	print('* * * * *')

if correct == 5:
	print('Yay You guess it in four tries!')
	input()
	sys.exit(0)

guess_five = input("What's your guess?")

while len(guess_five) != 5:
	print('That is not the right length.')
	guess_five = input("What's your guess?")

correct = 0

print_one()
print()
print_two()
print()
print_three()
print()
print_four()
print()
print_five()
print()

print('* * * * *')

if correct == 5:
	print('Yay You guessed it in five tries!')
	input()
	sys.exit(0)

guess_six = input("What's your guess?")

while len(guess_six) != 5:
	print('That is not the right length.')
	guess_six = input("What's your guess?")

correct = 0

print_one()
print()
print_two()
print()
print_three()
print()
print_four()
print()
print_five()
print()
print_six()
print()

if correct == 5:
	print('Yay You guessed it in six tries!')
	input()
else:
	print(f"You didn't guess the correct answer, the word was {word}")
	input()
