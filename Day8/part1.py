with open('./input.txt', 'r') as file:
    lines = file.readlines()

visible = 2 * len(lines) + 2 * len(lines[0].strip()) - 4


def negate(int):
    return -int


def check_if_visible(i, j):
    count = 0
    left = list(lines[i][0:j])
    right = list(lines[i][j+1:])
    up = []
    down = []
    for y in range(i):
        up.insert(0, lines[y][j])
    for y in range(i+1, len(lines)):
        down.append(lines[y][j])

    list_to_itr = None
    visibility = None
    for l in range(4):
        if l == 0:
            list_to_itr = left
        elif l == 1:
            list_to_itr = right
        elif l == 2:
            list_to_itr = up
        elif l == 3:
            list_to_itr = down
        for x in list_to_itr:
            if x >= lines[i][j]:
                visibility = False
                break
            else:
                visibility = True
        if visibility == True:
            return True

for i in range(1, len(lines)-1):
    lines[i] = lines[i].strip()
    for j in range(1, len(lines[i])-1):
        if check_if_visible(i, j):
            visible+=1
print(visible)