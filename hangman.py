# Import words
import random
from words import words_index

#choose words
def get_word():
    word = random.choice(words-index)
    return word.upper()

# start the game
# set lives
# hide words with underscores
def play(word):
    game_over = False
    winner = True
    guessed_letters = []
    guessed_words = []
    print(word)
    secret_word = "_" * len(word)
    lives = 6
    while game_over is False
    print(secret_word)
    guess = input("Please take a guess \n")

print("Let's begin")
print(display_hangman(lives))




# user import
# if correct - reveal letter
# else loose a life - diplay a line in hangman
# continue until lives have gone
# if all letters are guessed then the man survives
# else loose and the man dies
# reset the game