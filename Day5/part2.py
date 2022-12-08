from parseInput import ls, moves
def printls():
    print()
    for i in ls:
        print(i)

def findrowoftop(start):
    for i in range(0, len(ls)):
        if ls[i][start] == ' ' and i == len(ls) - 1:
            return len(ls)
        elif ls[i][start] != ' ':
            return i

def moveslist(q ,start, end):
    start = start - 1
    end = end - 1
    if(findrowoftop(end) - q < 0):
            for j in range(0 - (findrowoftop(end) - q)):
                ls.insert(0, [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' '])
    for i in range(q, 0, -1):
        ls[findrowoftop(end)-1][end] = ls[findrowoftop(start)+i-1][start]
        ls[findrowoftop(start)+i-1][start] = ' '
        
for i in range(2, len(moves), 3):
    moveslist(moves[i-2], moves[i-1], moves[i])

str = ''
for i in range(len(ls[0])):
    str = str+ls[findrowoftop(i)][i]
print(str)