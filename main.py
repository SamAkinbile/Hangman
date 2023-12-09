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

#To check the guessed letter

for position in range(word_length):
    letter = myword[position]

    if letter == guess:
        appear_as[position] = letter