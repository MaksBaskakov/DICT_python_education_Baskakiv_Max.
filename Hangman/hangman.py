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






w = ['python', 'javascript', 'php', 'java']
answer_prog = random.choice(w)  #python
word_list = list(answer_prog)   # [p,y,t,h,o,n]
user_word_list_null = "-" * len(answer_prog)    # ------
user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
print(user_word_list_null)
count = 0
while count != 8:
    count += 1
    answer_user = str(input('Input a letter:'))
    if answer_user in word_list:
        if word_list.count(answer_user) >= 2:
            index = word_list.index(answer_user)
            user_list[index] = answer_user
            word_list[index] = "-"
        index = word_list.index(answer_user)
        user_list[index] = answer_user
    else:
        print("That letter doesn't appear in the word")
    print(''.join(user_list))
print("Thanks for playing!")
print("We'll see how well you did in the next stage")









