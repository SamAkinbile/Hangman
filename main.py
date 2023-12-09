from hangman_art import logo
import random

from hangman_guess_words import guess_word


myword = random.choice(guess_word)
word_length = len(myword)


end_of_game = False
chances = 6

# Import the logo from hangman.py and print it at the start of the game.

from hangman import logo
print(logo)
