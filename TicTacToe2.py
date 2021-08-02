def createBoard(size):
    return [[0 for col in range(size)] for row in range(size)]


horizontal = []
vertical = []
cross = []


def createPossibleIndices(size):
    horizontal = [[[0, 0] for col in range(size)] for row in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            horizontal[i][j] = [i, j]
        print(i)
    print(horizontal)
    vertical = [[[0, 0] for col in range(size)] for row in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            vertical[i][j] = horizontal[j][i]
    print(vertical)
    cross = [[[0, 0] for col in range(size)] for row in range(2)]
    m = 0
    n = 0
    for i in range(0, size):
        cross[0][i] = [m, n]
        m += 1
        n += 1
    m = 0
    n = size - 1
    for i in range(0, size):
        cross[1][i] = [m, n]
        m += 1
        n -= 1
    print(cross)


# x = 1
# y = 0


def resultCheck(index, value):
    size = 3
    horizontal = [[[0, 0] for col in range(size)] for row in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            horizontal[i][j] = [i, j]
        print(i)
    print(horizontal)
    vertical = [[[0, 0] for col in range(size)] for row in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            vertical[i][j] = horizontal[j][i]
    print(vertical)
    cross = [[[0, 0] for col in range(size)] for row in range(2)]
    m = 0
    n = 0
    for i in range(0, size):
        cross[0][i] = [m, n]
        m += 1
        n += 1
    m = 0
    n = size - 1
    for i in range(0, size):
        cross[1][i] = [m, n]
        m += 1
        n -= 1
    print(cross)

    a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    for i in range(len(horizontal)):
        print(horizontal[i])
        if index in horizontal[i]:
            print("Found to match", index)
            calc = 0
            for j in horizontal[i]:
                print("From each element", j)
                if value == a[j[0]][j[1]]:
                    calc += 1
            if calc == 3:
                print("matched horizontal ", horizontal[i])
                return

    for i in range(len(vertical)):
        print(vertical[i])
        if index in vertical[i]:
            print("Found to match", index)
            calc = 0
            for j in vertical[i]:
                print("From each element", j)
                if value == a[j[0]][j[1]]:
                    calc += 1
            if calc == 3:
                print("matched vertical ", vertical[i])
                return

    for i in range(len(cross)):
        print(cross[i])
        if index in cross[i]:
            print("Found to match", index)
            calc = 0
            for j in cross[i]:
                print("From each element", j)
                if value == a[j[0]][j[1]]:
                    calc += 1
            if calc == 3:
                print("matched cross ", cross[i])
                return

    print("From after ", horizontal)
    print("Current game is ", a[1][1])
    currentColIndex = 1
    currentRowIndex = 1
    size = 3

