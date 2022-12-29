with open('./input.txt', 'r') as file:
    lines = file.readlines()

def check_if_visible(i, j):
    count = 0
    left = list(lines[i][0:j])
    left.reverse()
    right = list(lines[i][j+1:])
    up = []
    down = []
    for y in range(i):
        up.insert(0, lines[y][j])
    for y in range(i+1, len(lines)):
        down.append(lines[y][j])

    list_to_itr = None
    list_to_mult = []
    for l in range(4):
        count = 0
        if l == 0:
            list_to_itr = left
        elif l == 1:
            list_to_itr = right
        elif l == 2:
            list_to_itr = up
        elif l == 3:
            list_to_itr = down
        for x in list_to_itr:
            if x < lines[i][j]:
                count += 1
            elif x >= lines[i][j]:
                count += 1
                break
        list_to_mult.append(count)
    scenic_score = 1
    for x in list_to_mult:
        scenic_score *= x
    return scenic_score

max = 0
for i in range(1, len(lines)-1):
    lines[i] = lines[i].strip()
    for j in range(1, len(lines[i])-1):
        scenic = check_if_visible(i, j)
        if scenic > max:
            max = scenic
print('max', max)