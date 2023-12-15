<h1 align="center">Hangman Game: Game of guess</h1>

<p align="center">
<img src="hangmanimages/hangmanprofile.jpeg" />
</p>

- Uncover the word by guessing letters testing your deductive abilities in an exciting and suspenseful game.

<h2 align="center">How to play</h2>

<p align="center">
<img src="hangmanimages/Webcapture_flowchart_.jpeg" />
</p>
       
 #### First Time Visitor Goals

#### Setup
- The computer randomly picks a word from a guessed_word.
- Determine the maximum number of guesses (life) allowed. You have a chance of 6 lifes

#### Displaying the Word
Display spaces "(_)" to represent each letter in the chosen word.

#### Guessing Letters
- The player makes guesses from the list of guess_word list by typing the alphabet.
- If the guessed alphabet is part of the word reveal in the "(_)" spaces. The player continue playing.

#### Incorrect Guesses
- If the player makes incorrect guess and it is not present in the spaces revealed "(_)" . The player loses a life.
- It also keep track of a alphabet that is alraedy guessed "You have already guessed a letter"
- Keep track of a guess counter.

 #### Victory Condition
- If all letters are correctly guessed before reaching or exceeding the number of life. You win!

#### Defeat Condition
- If the player reaches the number of guesses before guessing the word or already guessed the leter. It will print  "You have alraedy guessed a letter, You lose"

  - #### Returning Visitor Goals

#### Starting a New Round

- Initiate a round where the computer chooses an unrevealed word.

  #### Return player

  - When a Hangman player comes back for another game they can expect a mix of familiarity and variety. Here's what they might encounter

#### A Range of Words
- The word keeper, the computer selects words each time leading to challenges.

#### Increasing Challenge
- As players gain experience they may come across words that are more complex and longer in length.

#### Developing Strategies
- Experienced players often develop their strategies to improve their chances of guessing the word. For example starting with vowels or common consonants can be helpful.

- #### Personal Preferences
- Players may develop preferences for word categories or themes. This can influence how much they enjoy the game.

- #### Sharpened Deduction Skills
- Returning players tend to enhance their deduction skills over time. They become better at making educated guesses based on patterns and the revealed letters.


- #### Multiplayer Experience
- In multiplayer settings players who come back to the game can enjoy the aspect of playing with friends or family competing against each other.
  

- ### Wireframes

  - Home image -                 [View](https://ascii.co.uk/)
  - caricutre of an hang man -   [caricature](https://ascii.co.uk/)



## Features


### Frameworks, Libraries & Programs Used

1. [Hangman logo:](https://ascii.co.uk/art/hangman)
    - At the start of the guessing game, hangman logo appear
2. [guess_word:](https://opeanai/)
    - The guess_word list was generated by openai.
3. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.



###  Testing

- Pass the code through a PEP8 linter and confirmed: All clear, no errors found
- I test on my local terminal.
  
  
### Remaining Bugs

- No bugs remaining
  
  ### Validator Testing
- PEP8
- No errors were returned from [testing](https://pep8ci.herokuapp.com/#)

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.



The live link can be found here - https://samakinbile.github.io/Hangman/


## Credits

### Media

- Hangman logo  [ascii ](https://ascii.co.uk)
- Guess word list [chatgpt](https://openai.com/)
 
### Content

- All content was written by the developer.

### Acknowledgements

- My Mentor for continuous helpful feedback.

- Tutor support at Code Institute for their support.
