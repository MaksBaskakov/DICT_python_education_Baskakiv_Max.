def input_matrix(row):
    array_row = []
    for i in range(row):
        array_col = []
        for j in input().split():
            if j != " ":
                array_col.append(float(j))
        array_row.append(array_col)
    return array_row


def print_matrix(result, row, col):
    for i in range(row):
        for j in range(col):
            print(result[i][j], end=' ')


def add_matrix(matrix_one, matrix_two, row, col):
    matrix_sum = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(matrix_one[i][j] + matrix_two[i][j])
        matrix_sum.append(temp)
    return matrix_sum


def sum_elements(list_first, list_second):
    sum = 0
    for i in range(len(list_first)):
        sum += list_first[i] * list_second[i]
    return sum


def multiply_matrix(matrix_one, matrix_second, row, col):
    matrix_sum = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(matrix_one[i][j] * matrix_second)
        matrix_sum.append(temp)
    return matrix_sum


def matrix_secondmultiply(matrix_one, matrix_two):
    sec_multiply = [[0 for row in range(len(matrix_two[0]))] for col in range(len(matrix_one))]
    for i in range(len(matrix_one)):
        list_first = matrix_one[i]
        for j in range(len(matrix_two[0])):
            list_second = [matrix_two[x][j] for x in range(len(matrix_two))]
            value = sum_elements(list_first, list_second)
            sec_multiply[i][j] = value
    return sec_multiply


def tranpose_matrix(matrix):
    sec_multiply = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sec_multiply[i][j] = matrix[j][i]
    return sec_multiply


def tranpose_side(matrix):
    sec_multiply = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sec_multiply[i][j] = matrix[j][i]
    res1 = sec_multiply[::-1]
    for i in range(len(matrix)):
        a = res1[i][::-1]
        result.append(a)
    return result


def tranpose_vertical(matrix):
    result = []
    for i in range(len(matrix)):
        a = matrix[i][::-1]
        result.append(a)
    return result


def tranpose_horizontal(matrix):
    result = matrix[::-1]
    return result


def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        change = -1
        sum = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                temp = []
                for k in range(width):
                    if k != i:
                        temp.append(matrix[j][k])
                m.append(temp)
            change *= -1
            sum += mul * determinant(m, change * matrix[0][i])
        return sum


def m(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def reverse_mat(matrix):
    determ = determinant(matrix, 1)
    factorials = []
    if len(matrix) == 2:
        return print("This matrix doesn't have an Inverse.")
    for i in range(len(matrix)):
        factorialss = []
        for j in range(len(matrix)):
            out = m(matrix, i, j)
            factorialss.append(((-1) ** (i + j)) * determinant(out, 1))
        factorials.append(factorialss)
    factorials = tranpose_matrix(factorials)
    for i in range(len(factorials)):
        for j in range(len(factorials)):
            factorials[i][j] = factorials[i][j] / determ
    return factorials


while True:
    print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
    a = input("Your choice: ")
    if a == '1':
        inp_row, inp_column = map(int, input("Enter size of first matrix:").split())
        print('Enter first matrix:')
        matrix_first = input_matrix(inp_row)
        matrix_row, matrix_column = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        matrix_second = input_matrix(matrix_row)
        if inp_row != matrix_row and inp_column != matrix_column:
            print('The operation cannot be performed.')
        else:
            matrix_result = add_matrix(matrix_first, matrix_second, inp_row, inp_column)
            print_matrix(matrix_result, inp_row, inp_column)
    elif a == '2':
        inp_row, inp_column = map(int, input("Enter size of matrix:").split())
        print('Enter matrix:')
        matrix_first = input_matrix(inp_row)
        print("Enter constant:")
        matrix_second = float(input())
        matrix_result = multiply_matrix(matrix_first, matrix_second, inp_row, inp_column)
        print_matrix(matrix_result, inp_row, inp_column)
    elif a == '3':
        inp_row, inp_column = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        matrix_first = input_matrix(inp_row)
        matrix_row, matrix_column = map(int, input('Enter size of second matrix:').split())
        print('Enter second matrix:')
        matrix_second = input_matrix(matrix_row)
        matrix_result = matrix_secondmultiply(matrix_first, matrix_second)
        print('The result is:')
        print_matrix(matrix_result, inp_row, matrix_column)
    elif a == '4':
        print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        tranpose_choice = int(input('Your choice:'))
        if tranpose_choice == 1:
            inp_row, inp_column = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix_first = input_matrix(inp_row)
            result = tranpose_matrix(matrix_first)
            print('The result is:')
            print_matrix(result, inp_row, inp_column)
        elif tranpose_choice == 2:
            inp_row, inp_column = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix_first = input_matrix(inp_row)
            result = tranpose_side(matrix_first)
            print('The result is:')
            print_matrix(result, inp_row, inp_column)
        elif tranpose_choice == 3:
            inp_row, inp_column = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix_first = input_matrix(inp_row)
            result = tranpose_vertical(matrix_first)
            print('The result is:')
            print_matrix(result, inp_row, inp_column)
        elif tranpose_choice == 4:
            inp_row, inp_column = map(int, input('Enter matrix size:').split())
            print('Enter matrix:')
            matrix_first = input_matrix(inp_row)
            result = tranpose_horizontal(matrix_first)
            print('The result is:')
            print_matrix(result, inp_row, inp_column)
    elif a == '5':
        inp_row, inp_column = map(int, input('Enter matrix size:').split())
        print('Enter matrix:')
        matrix_first = input_matrix(inp_row)
        result = determinant(matrix_first, 1)
        print('The result is: \n', result)
    elif a == '6':
        inp_row, inp_column = map(int, input('Enter matrix size:').split())
        print('Enter matrix:')
        matrix_first = input_matrix(inp_row)
        result = reverse_mat(matrix_first)
        print('The result is:')
        print_matrix(result, inp_row, inp_column)
    elif a == '0':
        break