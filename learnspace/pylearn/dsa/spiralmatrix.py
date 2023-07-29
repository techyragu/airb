
def generateMatrix(A):
    matrix = [ [0] * A for i in range(A) ]

    i = j = 0
    start = 1

    def move_right():
        k=0
        while k < A:
            matrix[i][j] = start
            j += 1
            start += 1
            k += 1

    def move_down():
        k=0
        while k < A:
            matrix[i][j] = start
            i += 1
            start += 1
            k += 1

    def move_left():
        k=0
        while k < A:
            matrix[i][j] = start
            j -= 1
            start += 1
            k += 1

    def move_up():
        k=0
        while k < A:
            matrix[i][j] = start
            i -= 1
            start += 1
            k += 1

    while A > 1:
        move_right()
        move_down()
        move_left()
        move_up()
        i += 1
        j += 1
        A -= 2

    if A == 1:
        matrix[i][j] = start

    return matrix

print(generateMatrix(3))





