print("""

    HANGMAN
The will start soon





""")
import random
#c=['dog', 'tiger', 'zebra' ]


print("Guess the word:>")



#def answers():
    #answer = str(input())
    #if answer == (c[0]):
        ##else:
        #print("You lost")
       #answers()
#answers()

s = ["phyton","java","javascript","php",]


a = random.choice(s)

def answers():
    answer= str(input())
    if answer == (a):
        print("You win")
    else:
        print("You lost")
        answers()
answers()