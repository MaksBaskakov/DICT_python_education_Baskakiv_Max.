print("""

    HANGMAN
The will start soon





""")
import random
c=['dog', 'tiger', 'zebra' ]


print("Guess the word:>")



def answers():
    answer = str(input())
    if answer == (c):
        print("You win")
    else:
        print("You lost")
        answers()
answers()