print("""

    HANGMAN
The will start soon





""")
import random
#c=['dog', 'tiger', 'zebra' ]






#def answers():
    #answer = str(input())
    #if answer == (c[0]):
        ##else:
        #print("You lost")
       #answers()
#answers()

s = ["phyton","java","javascript","php",]


a = random.choice(s)

b=a[0]+a[1]+a[2]





print("Guess the word:>"+ b)



def answers():
    answer= str(input())
    if answer == (a):
        print("You win")
    else:
        print("You lost")
        answers()
answers()

