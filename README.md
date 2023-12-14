<h1 align="center">Hangman Game: Game of guess</h1>

<p align="center">
<img src="hangmanimages/hangmanprofile.jpeg" />
</p>

- Uncover the word by guessing letters testing your deductive abilities in an exciting and suspenseful game.

<h2 align="center">User Experience (UX)</h2>

<p align="center">
<img src="hangmanimages/Webcapture_flowchart_.jpeg" />
</p>
       
 #### First Time Visitor Goals

#### Setup
- The computer randomly picks a word from a guessed_word.
- Determine the maximum number of guesses (life) allowed. You have a chance of 6 lifes

#### Displaying the Word
Display spaces "-" to represent each letter in the chosen word.

#### Guessing Letters
- The player makes guesses from the alphabet.
- If the guessed letter is part of the word reveall in the "(_)" spaces. The player does not lose any life. The player continue playing.

#### Incorrect Guesses
- If the guessed letter is not present in the spaces revealed "(_)" . The player loses a life.
- It also keep track of a letter that is alraedy guessed "You have alraedy guessed a letter"
- Keep track of a guess counter.

 #### Victory Condition
- If all letters are correctly guessed before reaching or exceeding the number of guesses. You win!

#### Defeat Condition
- If the player reaches the number of guesses before guessing the word or already guessed the leter. It will print  "You have alraedy guessed a letter, You lose"

  - #### Returning Visitor Goals

#### Starting a New Round

- Initiate a round where the computer chooses a word.
  

  #### Return player

  - When a Hangman player comes back for another game they can expect a mix of familiarity and variety. Here's what they might encounter

#### A Range of Words
- The word keeper, the computer selects words each time leading to challenges.

#### Increasing Challenge
- As players gain experience they may come across words that are more complex and longer, in length.

#### Developing Strategies
- Experienced players often develop their strategies to improve their chances of guessing the word. For example starting with vowels or common consonants can be helpful.

- #### Personal Preferences
- Players may develop preferences for word categories or themes. This can influence how much they enjoy the game.

- #### Sharpened Deduction Skills
- Returning players tend to enhance their deduction skills over time. They become better at making educated guesses based on patterns and the revealed letters.


- #### Multiplayer Experience
- In multiplayer settings players who come back, to the game can enjoy the aspect of playing with friends or family competing against each other.




  

- ### Wireframes

  - Home image - [View](https://ascii.co.uk/)



  

## Features

- Hangman Logo

### Frameworks, Libraries & Programs Used

1. [Hangman logo:](https://ascii.co.uk/art/hangman)
    - At the start of the guessing game, hangman logo appear
2. [guess_word:](https://opeanai/)
    - The guess_word list was generated by openai.
3. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.



###  Testing

- The game was tested on github.



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

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
git clone  https://samakinbile.github.io/Hangman/
```

7. Press Enter. Your local clone will be created.

```
$ git clone  https://samakinbile.github.io/Hangman/
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Media

- Hangman logo  [ascii ](https://ascii.co.uk)
- guess_word [chatgpt](https://openai.com/)
 
### Content

- All content was written by the developer.

### Acknowledgements

- My Mentor for continuous helpful feedback.

- Tutor support at Code Institute for their support.
