# This is a guess the number game.
import random
guessestaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 1)
print('guess number between 1 and 20, ' + myName)

while guessestaken < 6:
    print('take a guess!')
    guess = input()
    guess = int(guess)

    guessestaken = guessestaken + 1

    if guess < number:
        print('your guess is too low, guess higher')
    if guess > number:
        print('your guess is too high, guess lower')

    if guess == number:
        break

if guess == number:
    guessestaken = str(guessestaken)
    print('nice ' + myName + ' you guessed the number in ' + guessestaken + ' tries!')

if guess != number:
    number = str(number)
    print('hah nobb you did guess the number it was ' + number )