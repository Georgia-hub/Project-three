# Import words
import random
from words import words_index

#choose words
def get_word():
    word = random.choice(words-index)
    return word.upper()

def play(word):
words_entered = "_" * len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   lives = 6

print("Let's begin")
print(display_hangman(lives))
print()



# set lives 
# start the game



# choose words

# hide words with underscores

# user import
# if correct - reveal letter
# else loose a life - diplay a line in hangman
# continue until lives have gone
# if all letters are guessed then the man survives
# else loose and the man dies
# reset the game