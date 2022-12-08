file = open('./input.txt', 'r')
input = file.readlines()
ls = [[],[],[],[],[],[],[],[]]
moves= []

for i in range(len(ls)):
    input[i] = list(input[i])
    for j in range(1, len(input[i]) -2, 4):
        ls[i].append(input[i][j])

for i in range(len(ls)+2, len(input)):
    li = input[i].split(' ')
    for j in range(1, 6, 2):
        moves.append(int(li[j]))