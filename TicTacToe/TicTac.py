def cells(u_c):
    print('---------')
    print('| ' + u_c[0] + ' ' + u_c[1] + ' ' + u_c[2] + ' |')
    print('| ' + u_c[3] + ' ' + u_c[4] + ' ' + u_c[5] + ' |')
    print('| ' + u_c[6] + ' ' + u_c[7] + ' ' + u_c[8] + ' |')
    print('---------')

# def result():
#     answer = []
#     if user_cells.count("X") - user_cells.count("O") >= 2:
#         return "Impossible"
#     elif user_cells.count("O") - user_cells.count("X") >= 2:
#         return "Impossible"
    # if user_cells[0] == user_cells[1] == user_cells[2] != '_':
    #     answer.append(a[0])
    # if user_cells[3] == user_cells[4] == user_cells[5] != '_':
    #     answer.append(a[3])
    # if user_cells[6] == user_cells[7] == user_cells[8] != '_':
    #     answer.append(a[6])
    # if user_cells[0] == user_cells[3] == user_cells[6] != '_':
    #     answer.append(a[0])
    # if user_cells[1] == user_cells[4] == user_cells[7] != '_':
    #     answer.append(us[1])
    # if user_cells[2] == user_cells[5] == user_cells[8] != '_':
    #     answer.append(a[2])
    # if user_cells[0] == user_cells[4] == user_cells[8] != '_':
    #     answer.append(a[0])
    # if user_cells[2] == user_cells[4] == user_cells[6] != '_':
    #     answer.append(a[2])


def result(u_c):
    answer = []
    if u_c.count("X") - u_c.count("O") >= 2:
        return "Impossible"
    elif u_c.count("O") - u_c.count("X") >= 2:
        return "Impossible"
    elif "_" in u_c:
        return "Game not finished"
    if u_c[0] == u_c[4] == u_c[8]:
        answer.append(u_c[0])
    if u_c[0] == u_c[1] == u_c[2]:
        answer.append(u_c[0])
    if u_c[0] == u_c[3] == u_c[6]:
        answer.append(u_c[0])
    if u_c[1] == u_c[4] == u_c[7]:
        answer.append(u_c[1])
    if u_c[2] == u_c[4] == u_c[6]:
        answer.append(u_c[2])
    if u_c[2] == u_c[5] == u_c[8]:
        answer.append(u_c[2])
    if u_c[3] == u_c[4] == u_c[5]:
        answer.append(u_c[5])
    if u_c[0] == u_c[4] == u_c[8]:
        answer.append(u_c[0])
    if u_c[6] == u_c[7] == u_c[8]:
        answer.append(u_c[6])
    if answer.count('X') >= 2:
        answer.remove('X')
    elif answer.count('O') >= 2:
        answer.remove('O')
    if len(answer) >= 2:
        return "Impossible"
    elif len(answer) == 1:
        return answer[0] + ' wins'
    elif len(answer) == 0:
        return "Draw"





if __name__=="__main__":
    print("""    
    
    X0X
    0XX
    00X
    
     """)

    print("Enter cells:")

    user_cells = list(input())
    cells(user_cells)
    A = result(user_cells)
    print(A)
# print("Enter cells:")
#
# user_cells=list(input())
#
# def cells():
#
#
#
#     print('---------')
#     print('| ' + user_cells[0] + ' ' + user_cells[1] + ' ' + user_cells[2] + ' |')
#     print('| ' + user_cells[3] + ' ' + user_cells[4] + ' ' + user_cells[5] + ' |')
#     print('| ' + user_cells[6] + ' ' + user_cells[7] + ' ' + user_cells[8] + ' |')
#     print('---------')
#
# cells()








