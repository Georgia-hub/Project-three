import random
from words import words_index

def get_word():
    word = random.choice(words_index)
    return word.upper()



#game menu
def menu():
    print("[0], Let's play")
    print("[1], Reset game")
    menu():
option = int(input("Please select an option: "))
while option == 0:
        play(word) = True
        # Begin playing the game
        # play(word)
        print("let's play Hangman")
    else:
        option == 1:
        play(word) = False
        print("Reset game")
        print()
        menu()
option = int(input("Please select an option: "))
print("Thank you for playing")      

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
    print(hangman_lives(lives))
    guess = input("Please take a guess \n")
# if correct - reveal letter
    if guess in word:
        print("it's in")

# continue until lives have gone
# if all letters are guessed then the man survives
        secret_word_listed = (secret_word)
        print(secret_word_listed)
        indices = [i for i letter in enumerate(word)
                   if letter == guess]
        for index in indices:
            secret_word_listed =[index] = guess
            secret_word = "".join(secret_word_listed)
        if "_" not in secret_word: 
        game_over = True
# else loose a life - diplay a line in hangman
# else loose and the man dies
    else:
        print("its not in")
        lives -=1
        print(lives)
        if lives == 0
        winner = False
        game_over = True
end_game(winner)

# user import
def end_game(outcome):
    if outcome:
        is winner
        print("{secret_word} is correct, you have won!")
    else:
        is looser
        print("{secret_word} is incorrect, you have lost")

        
# hangman diplay of lives
def hangman_lives(lives):
    stages = ["""
 O
/|\
/ \
====""",
"""
/|\
/ \
====""",
"""
/|
/ \
====""",
"""
 |
/ \
====""",
"""
/ \
====""",
"""
/
====""",
]

# reset the game