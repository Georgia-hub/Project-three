import random
from words import words_index
"""imports random words to use for the secrect word"""

def get_word():
    word = random.choice(words_index)
    return word.upper()
"""imports random words from words index and returns ouput in uppercase"""

def play(word):
    game_over = False
    winner = True
    guessed_letters = []
    guessed_words = []
    print(word)
    secret_word = "_" * len(word)
    lives = 5
    while game_over is False:
      print(secret_word)
      print(hangman_lives(lives))
      guess = input("Please take a guess \n").upper()
      print(guess)
"""
defines play word, the game is still going. 
letters and words that are guessed are printed.
Player only had 5 wrong tries before the end of the game.
"""
      if guess in word:
        print("it's in")
        secret_word_listed = list(secret_word)
        print(secret_word_listed)
        indices = [i for i, letter in enumerate(word)
              if letter == guess]
        for index in indices:
            secret_word_listed[index] = guess
           secret_word = "".join(secret_word_listed)
        if "_" not in secret_word: 
            game_over = True
"""
    if word guessed corrrectly the word secret word and comment is dipayed.
    power to i for i and the letter in looped over and counted times of doing until the letter is guessed.
    then to join this the secrect word, if not the secret word then the game is over.
"""
        else:
            print("It's not in")
            lives -=1
            print(lives)
            if lives == 0:
                winner = False
                game_over = True
""" if the player looses a 1 life to display this and if the lives are equal to 0 then the game is over"""        
        if game_over:
            end_game(winner, word)

def menu():
    print("[0], Let's play")
    print("[1], Reset game")
    
    option = int(input("Please select an option: "))
    if option == 0:
        play(get_word())
        print("let's play Hangman")
    elif option == 1:
        
        print("Thank you for playing")  
        print("Reset game")
        print()
        menu()
    elif option == 2:
        print(hangman_lives(0), hangman_lives(2))

def end_game(outcome, word):
    if outcome is True:
        print((f"{word} is correct, you have won!"))
        menu()
    else:
        print(f"the word was {word}, you have lost

def hangman_lives(lives):
    """
              =======
              |/    |
              |     @
              |    /|\\
              |     |
              |    / \\
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |    /|\\
              |     |
              |    /
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |    /|\\
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |    /|
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |     |
              |     |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |     @
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """,
        """
              =======
              |/    |
              |
              |
              |
              |
         _____|_________
        /     |\\        /|
        ______________ / /
                      | /
        ______________ /
        """
    ]
    return stages[lives]