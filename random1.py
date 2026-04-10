# This is a guess the number game.
import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
guess = None
for guesses_taken in range(1, 7):
    print(f'Take a guess. (Attempt {guesses_taken}/6)')
    try:
        guess = int(input())
    except ValueError:
        print('Please enter a valid number!')
        continue

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secret_number:
    print(f'Good job! You guessed my number in {guesses_taken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secret_number}')