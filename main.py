import random


select_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
myword = random.choice(select_list)

print(f'Psst, the solution {myword}.')
appear_as = []
word_length = len(myword)
for _ in range(word_length):
    display += "_"
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in myword:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
