from hangman import logo
import random

from hangman_guess_words import guess_word


myword = random.choice(guess_word)
word_length = len(myword)


game_finish = False
chances = 6

# Logo imported from hangman files
print(logo)


# Create blanks
appear_as = []
for _ in range(word_length):
    appear_as += "_"

while not game_finish:
    trial_guess = input("Guess a letter:").lower()

# If letter have already been guessed, print out the letter and let the player know

if trial_guess in appear_as:
    print(f"You have already guessed {trial_guess}")

# To check the guessed letter

for position in range(word_length):
    letter = myword[position]
   # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        appear_as[position] = letter

# We check if the user answer are wrong
if trial_guess not in myword:
    # If type letter is not in myword, print out the letter and let them know it's not in the word.
    print(
        f"You guessed {trial_guess}, that's not in the word. You lose a single life.")

chance -= 1
if chance == 0:
    game_finish = True
    print("You lose.")

# Joining element in the list and turning it to the string
 print(f"{' '.join(display)}")