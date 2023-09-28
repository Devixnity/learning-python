import random

number = random.randint(1,2)

print('do you want to paly a game?')

answer1 = str(input())

if 'yes' in answer1:
    print('lets play a guessing game, what is the number i am thinking of between 1 and 2')
    
    guess = int(input())
    if guess == number:
        print('congrats you got it correct')

    if guess != number:
        print('you got the number wrong')

else:
    print('ok dude')
