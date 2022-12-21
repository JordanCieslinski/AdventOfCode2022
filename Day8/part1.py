with open('./test.txt', 'r') as file:
    lines = file.readlines()

visible = 2 * len(lines) + 2 * len(lines[0].strip()) - 4

def negate(int):
    return -int

def check_if_visible(i, j, char):
    # for loop to go through all versions left, right, up, down
    #                                     0,    1,    2,   3
    # check is going to choose if it iterates through the row or col
    visible = False
    for x in range(4):
        i_add = 0
        j_add = 0
        check = ''
        var_to_itr = None
        if x == 0 or x == 1:
            check = 'col'
            j_add = 1
            var_to_itr = j
            if x == 0:
                j_add = negate(j_add)
        elif x == 2 or x == 3:
            check = 'row'
            i_add = 1
            var_to_itr = i
            if x == 2:
                i_add = negate(i_add)
        for y in range(1, var_to_itr+1)
            if lines[i+(i_add*y)][j+(j_add*y)] < lines[i][j]:
                visible = True
            else:
                break
            print(check, i_add, j_add ,lines[i][j], lines[i+i_add*y][j+j_add*y], visible)
            # ! THE ISSUE IS THAT IT IS SEEING THAT A NUMBER NEXT TO IT IS GREATER THAN THE CUR VALUE, IT CONTINUES TO GO TO THE NEXT NUMBER IN THE LOOP. YOU NEED TO STOP THE LOOP AFTER IT IS GREATER ONCE SO THAT IT DOESNT RESET VISIBLE TO TRUE
    return visible





for i in range(1, len(lines)-1):
    lines[i] = lines[i].strip()
    for j in range(1, len(lines[i])-1):
        check_if_visible(i,j, lines[i][j]), lines[i][j]
