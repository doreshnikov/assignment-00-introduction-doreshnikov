import random

secret = random.randint(1, 1000)

guess = int(input('Please enter a number: '))
guess_count = 1

while guess != secret:
    if guess_count >= 10:
        print('You lose!')
        exit(0)

    if guess < secret:
        print('Your guess is too low')
    else:
        print('Your guess is too high')

    guess = int(input())
    guess_count += 1

print('Congrats!')