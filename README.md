# Hangman Game

## **Planning Stage**
### Project Goals
My plan was to creare a user freindly game, that also has a range of easy words and harder less obviosy words to guess to give the player a challenge thats not impossible to play. The goal for this project was to create a claassic version of the game hangman, keeping in with the old school style of comppting in the earlier days by using ASCII art for the hangman disply.

# ** add image![hangman.png](docs/images/hangman.png)**

### Game controls 
The game controls consit of a menu bar with 2 options to begin and play or reset the game. Also entering any letter in which the player has guessed the secret word to be.

### Game rules
The player has to guess what the secret word is hidden by the underscores. The player will guess what letter they think may be in the word, if this is correct the letter will become visiable where this is placed in the word. If the player guesses all letters correctly then they have won game. If the player exceeds more than 6 wrong guesses then they will loose the game. The a

have 6 lives, if they guess right the player will win. If the player guesses 

### User Goals
The user goals for the game is for the player to guess all the letters corretly and reveal the hidden word to win the game.

### User Stories
* As a user I want the site to be fun and interactive.
* As a user I want to be able to understand how to play easily.
* As a user I want to be able to keep trying to better my score continusly.
* As a user I want to be able to use the controls at ease.
* As a user I want to be able to visually see the score.

### Design Goals
The design goal was to create a functional hangman game that has a range of easy and complex words to guess correctly or loose if not guessed correctly. When the player looses a life the stick man also looses a body part untill the man is hung and game is over.
* user friendly
* challeneg the user
* Hangman display of the stcik man loosing lives
* Customisation possiblities

### Design Choices
I decided to stay in line with traditail design for this game and created a stick man using ASCII art style.
* A classic version of the game
* A range easy and hard words
* Hangman visually loosing lives

#### Color Scheme
I wanted this game to be like hangman 101 so i decided to not do a color scheme and leave this in it's raw colors.

## **Features**
I created a menu for a feature at the begging of the game for the palyer to be able to commence playing the game or reset this again.
- Reveals letters as you've guessed correctly
- Random outcome choice for words picked
- Menu option

## **Features to be added**
Most projects are never finshed when a develper thinks they are. Our projects are constantly being improved for your development. For my next project i would like to add the following features:
- Improved grapics
- More content
- Give the player an option to level up after winning so many rounds

## **Testing**
I checked my code through PEP8 numuros times to make sure that all my code was clean with no errors. The endgame outcome would not print if or else stament when i got to that stage on the game. I fixed this by using an f string, i also used the square brakets instead of the cury within teh fstring to use word that has been radomly selcted for the game, i corrected this.
I have tested my project along the way as i was writing my code. I run into a number of errors, spelling mistakes and coding errors. I was able to use google, course work and the slack supports to help give me an idea of my errors after trying to resoved myself. I also was getting an error for .upper as i had wrote uppercase. in error, and my text wasn't being displayed in uppercase untill i corrected my error. Also when i used /n for a new line this wasnt appearing when tested as i havent put this in a string, i corrected this. Another common erros i was getting was tralling white space or not missing out spaces for the correct format. 

### Responsiveness
To test the responsiveness of the site, the page was tested through PEP8 and is completely responsive, fit for purpose. Also fits to scale depeding on the device played on for maximum game play. I orginally had an issue with the restart function but in the end after using all my resources this was an extra symbol. 

### Testing Validator
I checked my code through PEP8 numuros times to make sure that all my code was clean with no errors. 

## **Bugs**
During the development of Hangman i had a few bugs to overcome which were mostly mistakes. the main bugs were expected 2 blank lines found.

### Fixed Bugs
Firstly, i couldnt get the import function to work as i mispelt the method keyword in my code. I had to remove all the unneeded spaces and put in spaces between my lines of code. The endgame outcome would not print if or else stament when i got to that stage on the game. I fixed this by using an f string, i also used the square brakets instead of the cury within teh fstring to use word that has been radomly selcted for the game, i corrected this.
## **Technology Used**

### Languages
Python, CI template that uses HTML CSS JS and Node.js

## **Deployment**
I deployed my website on GitHub pages via the following:
1. Go to repository in projects and select the **settings** tab.
1. Near the bottom on the left side click on **pages** link.
1. Click on **Source** and on the button (None) to gt the dropdwon menu.
1. Click on **Main** and then click on **Save**.
1. Once this message **Your site is ready to be published** appears this will confirm that this has been published.
1. After a little amount of time the site will be published and this message will change to **Your site is published**.

## **Credits**
This website was designed by Georgia Kershsw.

### Content
This contains images and the process of the development of my Hangman game.