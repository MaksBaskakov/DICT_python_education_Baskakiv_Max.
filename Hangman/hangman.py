print("""

    HANGMAN
The will start soon





""")
import random
#c=['dog', 'tiger', 'zebra' ]













# w = ['python', 'javascript', 'php', 'java']
# answer_prog = random.choice(w)  #python
# po_bukvam = list(answer_prog)   # [p,y,t,h,o,n]
# user_word_list_null = "-" * len(answer_prog)    # ------
# user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
# print(user_word_list_null)
# count = 0
# while count != 8:
#     count += 1
#     answer_user = str(input('Input a letter:'))
#     if answer_user in po_bukvam:
#         if po_bukvam.count(answer_user) >= 2:
#             index = po_bukvam.index(answer_user)
#             user_list[index] = answer_user
#             po_bukvam[index] = "-"
#         index = po_bukvam.index(answer_user)
#         user_list[index] = answer_user
#     else:
#         print("That letter doesn't appear in the word")
#     print(''.join(user_list))
# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")

# w = ['python', 'javascript', 'php', 'java']
# answer_prog = random.choice(w)  #python
# po_bukvam = list(answer_prog)   # [p,y,t,h,o,n]
# user_word_list_null = "-" * len(answer_prog)    # ------
# user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
# print(user_word_list_null)
# count = 0
# while count != 8:
#     answer_user = str(input('Input a letter:'))
#     if answer_user in po_bukvam:
#         if po_bukvam.count(answer_user) >= 2:
#             index = po_bukvam.index(answer_user)
#             user_list[index] = answer_user
#             po_bukvam[index] = "-"
#         index = po_bukvam.index(answer_user)
#         user_list[index] = answer_user
#     elif answer_user==user_list[index]:
#         print("No improvments")
#         count +=1
#     else:
#         count +=1
#         print("That letter doesn't appear in the word")
#     print(''.join(user_list))
# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")

w = ['python', 'javascript', 'php', 'java']
answer_prog = random.choice(w)  #python
po_bukvam = list(answer_prog)   # [p,y,t,h,o,n]
user_word_list_null = "-" * len(answer_prog)    # ------a
user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
print(user_word_list_null)
count = 0
used = []
while count != 8:
    answer_user = str(input('Input a letter:'))
    if answer_user in used:
        print("Bilo")
        count +=1
        continue
    used.append(answer_user)
    if answer_user in po_bukvam:
        if po_bukvam.count(answer_user) >= 2:
            index = po_bukvam.index(answer_user)
            user_list[index] = answer_user
            po_bukvam[index] = "-"
        index = po_bukvam.index(answer_user)
        user_list[index] = answer_user
    else:
        count +=1
        print("That letter doesn't appear in the word")
    print(''.join(user_list))
print("Thanks for playing!")
print("We'll see how well you did in the next stage")



















