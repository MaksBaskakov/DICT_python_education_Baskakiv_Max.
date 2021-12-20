# print("""
#
#     HANGMAN
# The will start soon
#
#
#
#
#
# """)
# import random
# #c=['dog', 'tiger', 'zebra' ]
#
#
#
#
#
#
#
#
#
#
#
#
#
# # w = ['python', 'javascript', 'php', 'java']
# # answer_prog = random.choice(w)  #python
# # po_bukvam = list(answer_prog)   # [p,y,t,h,o,n]
# # user_word_list_null = "-" * len(answer_prog)    # ------
# # user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
# # print(user_word_list_null)
# # count = 0
# # while count != 8:
# #     count += 1
# #     answer_user = str(input('Input a letter:'))
# #     if answer_user in po_bukvam:
# #         if po_bukvam.count(answer_user) >= 2:
# #             index = po_bukvam.index(answer_user)
# #             user_list[index] = answer_user
# #             po_bukvam[index] = "-"
# #         index = po_bukvam.index(answer_user)
# #         user_list[index] = answer_user
# #     else:
# #         print("That letter doesn't appear in the word")
# #     print(''.join(user_list))
# # print("Thanks for playing!")
# # print("We'll see how well you did in the next stage")
#
# # w = ['python', 'javascript', 'php', 'java']
# # answer_prog = random.choice(w)  #python
# # po_bukvam = list(answer_prog)   # [p,y,t,h,o,n]
# # user_word_list_null = "-" * len(answer_prog)    # ------
# # user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
# # print(user_word_list_null)
# # count = 0
# # while count != 8:
# #     answer_user = str(input('Input a letter:'))
# #     if answer_user in po_bukvam:
# #         if po_bukvam.count(answer_user) >= 2:
# #             index = po_bukvam.index(answer_user)
# #             user_list[index] = answer_user
# #             po_bukvam[index] = "-"
# #         index = po_bukvam.index(answer_user)
# #         user_list[index] = answer_user
# #     elif answer_user==user_list[index]:
# #         print("No improvments")
# #         count +=1
# #     else:
# #         count +=1
# #         print("That letter doesn't appear in the word")
# #     print(''.join(user_list))
# # print("Thanks for playing!")
# # print("We'll see how well you did in the next stage")
#
# w = ['python', 'javascript', 'php', 'java']
# answer_prog = random.choice(w)  #python
# po_bukvam = list(answer_prog)   # [p,y,t,h,o,n]
# user_word_list_null = "-" * len(answer_prog)    # ------a
# user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
# print(user_word_list_null)
# count = 0
# used = []
# while count != 8:
#     answer_user = str(input('Input a letter:'))
#     if answer_user in used:
#         print("Bilo")
#         count +=1
#         continue
#     used.append(answer_user)
#     if answer_user in po_bukvam:
#         if po_bukvam.count(answer_user) >= 2:
#             index = po_bukvam.index(answer_user)
#             user_list[index] = answer_user
#             po_bukvam[index] = "-"
#         index = po_bukvam.index(answer_user)
#         user_list[index] = answer_user
#     else:
#         count +=1
#         print("That letter doesn't appear in the word")
#     print(''.join(user_list))
# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")

import random
wordlist = ['css', 'javascript', 'java', 'python', 'html', 'php']
turns = 5
print("HANGMAN")


def main(turns, user_letters, code_letter):
    while turns > 0:
        count_of_try = 0
        for letter in code_letter:
            if letter in user_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                count_of_try += 1
        if count_of_try == 0:
            print('\nYou win!')
            break
        a = input('\nInput a letter: ')
        user_letters += a
        if a not in code_letter:
            turns -= 1
            if len(a) == 0 or len(a) > 1:
                print('\nYou should input a single letter')
            if a.capitalize() == a:
                print('\nPlease enter a lowercase English letter')
            print(f'That letter doesnt appear in the word \n{turns}, more turns\n')
            if turns == 0:
                print(f'\nThe answer is {code_letter}')
    print("HANGMAN")
    start()


def start():
    code_letter = random.choice(wordlist)
    user_letters = ''
    while True:
        user_input = input('Type "play" to play the game, "exit" to quit: ')
        if user_input == 'play':
            print(len(code_letter) * '_ ', end='')
            main(turns, user_letters, code_letter)
        else:
            exit()


if __name__ == '__main__':
    start()

















