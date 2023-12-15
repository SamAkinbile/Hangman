import os
from hangman_guess import guess_word
from hangman import levels
from hangman import logo
import random

myword = random.choice(guess_word)
word_length = len(myword)

game_finish = False
chance = 6

# Logo imported from hangman files
print(logo)

# Create blanks
appear_as = []
for _ in range(word_length):
    appear_as += "_"

while not game_finish:
    trial_guess = input("Guess a letter:").lower()

    os.system('cls' if os.name == 'nt' else 'clear')

# print already guessed letter.
    if trial_guess in appear_as:
        print(f"You have already guessed {trial_guess}")

    # To check the guessed letter
    for position in range(word_length):
        letter = myword[position]

# print(f"Current position: {position}\n Current letter.
        if letter == trial_guess:
            appear_as[position] = letter
# We check if the player's answer is wrong
if trial_guess not in myword:
    # Let the player know if alphabet not in guessed_list
    print(
        f"You guessed {trial_guess}, that's not in the word.You lose a life.")
    chance -= 1
    if chance == 0:
        game_finish = True
        print("You lose.")

    # Joining elements in the list and turning it into a string
    print(f"{' '.join(appear_as)}")

    # See if the player has guessed all the right alphabets
    if "_" not in appear_as:
        game_finish = True
        print("You win.")

    # Import stages from hangman.py and make this error go away.
    print(levels[chance])
