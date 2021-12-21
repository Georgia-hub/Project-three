# Import words
import random
from words import words_index

def get_word():
    word = random.choice(words-index)
    return word.uppercase()

# set lives 
# start the game

def play(word):
word_entered = "_" * len(word)
guessed = False
guessed_letters = []
guessed_words = []
lives = 6

# choose words
-

# hide words with underscores
# user import
# if correct - reveal letter
# else loose a life - diplay a line in hangman
# continue until lives have gone
# if all letters are guessed then the man survives
# else loose and the man dies
# reset the game