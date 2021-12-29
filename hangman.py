# Import words
import random
from words import words_index

#choose words
def get_word():
    word = random.choice(words-index)
    return word.upper()

# start the game
# set lives 
def play(word):
    game_over = False
    winner = True
    guessed_letters = []
    guessed_words = []
    print(word)
    secret_word = "_" * len(word)
    lives = 6

print("Let's begin")
print(display_hangman(lives))
print()





# choose words

# hide words with underscores

# user import
# if correct - reveal letter
# else loose a life - diplay a line in hangman
# continue until lives have gone
# if all letters are guessed then the man survives
# else loose and the man dies
# reset the game