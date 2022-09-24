from math import *


class InputError(Exception):
    pass


class SizeError(Exception):
    pass


init = '''
    Welcome to KMap solver for Sum of Products by Vibhav
    Follow the following syntax
    1 - for minterm
    0 - doesn't exist
    x - don't care condition
    Have Fun!
'''


def query2(matrix):
    pairs = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = []
            current = [i, j]
            adjup = [i-1, j]
            adjdwn = [i+1, j]
            adjlft = [i, j-1]
            adjrgt = [i, j+1]

            if adjdwn[0] >= len(matrix):
                adjdwn[0] -= len(matrix)

            if adjrgt[1] >= len(matrix[i]):
                adjrgt[1] -= len(matrix[i])

            if adjup[0] == -1:
                adjup[0] = len(matrix)-1

            if adjlft[1] == -1:
                adjlft[1] = len(matrix[1])-1

            if matrix[current[0]][current[1]] == 1:
                if matrix[adjup[0]][adjup[1]] in (1, 'x'):
                    # print("Pair found")
                    pairs.append((current[0], current[1], adjup[0], adjup[1]))
                if matrix[adjdwn[0]][adjdwn[1]] in (1, 'x'):
                    pairs.append(
                        (current[0], current[1], adjdwn[0], adjdwn[1]))
                    # print("Pair found")
                if matrix[adjlft[0]][adjlft[1]] in (1, 'x'):
                    # print("Pair found")
                    pairs.append(
                        (current[0], current[1], adjlft[0], adjlft[1]))
                if matrix[adjrgt[0]][adjrgt[1]] in (1, 'x'):
                    # print("Pair found")
                    pairs.append(
                        (current[0], current[1], adjrgt[0], adjrgt[1]))
    # CHECK THE PAIRS LIST FOR DUPES
    dupelocs = []
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            p1 = pairs[i]
            p2 = pairs[j]
            p1 = list(p1)
            p2 = list(p2)
            temp = 0
            temp = p2[0]
            p2[0] = p2[2]
            p2[2] = temp

            temp = p2[1]
            p2[1] = p2[3]
            p2[3] = temp

            if p1 == p2 and i != j:
                dupelocs.append(j)
                break
    # dupelocs.sort()
    todel = []
    for i in range(0, len(dupelocs), 2):
        todel.append(dupelocs[i])

    todel.sort()
    todel.reverse()
    for i in todel:
        pairs.pop(i)
    return pairs


print(init)
rows = int(input("How many rows?\n"))
table = []
for j in range(rows):
    raw = list(input())
    try:
        for i in range(len(raw)):
            if raw[i] == 'x':
                pass
            elif raw[i] == '1' or raw[i] == '0':
                raw[i] = int(raw[i])
            else:
                raise InputError
    except InputError:
        print("Oops, invalid data entered")
        exit(0)
    table.append(raw)
cols = len(table[0])
try:
    if log2(rows) - int(log2(rows)) != 0 or log2(cols) - int(log2(cols)):
        raise SizeError
except SizeError:
    print("Size of the matrix is invalid")
    exit(0)
print(query2(table))
