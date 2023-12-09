from hangman import logo
import random

from hangman_guess_words import guess_word


myword = random.choice(guess_word)
word_length = len(myword)


end_of_game = False
chances = 6

# Logo imported from hangman files
print(logo)
