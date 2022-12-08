file = open('./input.txt', 'r')
list = file.readline()

def findnorepeats():
    bool = False
    for i in range(14, len(list)):
        str = list[i-14:i]
        for j in str:
            if str.count(j) > 1:
                bool = True
                break
            else:
                bool = False
        if bool == False:
            print(i)
            break

findnorepeats()