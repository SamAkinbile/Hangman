import random


select_list = ["aardvark", "baboon", "camel"]
myword = random.choice(select_list)

print(f'Psst, the solution is {myword}.')
appear_as = []
word_length = len(myword)
for _ in range(word_length):
    appear_as += "_"
    print(appear_as)
while not game_finish
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()


# Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for position in range(word_length):
    letter = myword[position]
    if letter == guess:
        appear_as[position] = letter

print(appear_as)
if "_" not in display:
    game_finish = True
    print("You win.")
