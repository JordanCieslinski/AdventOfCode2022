file = open('input.txt', 'r')
list = file.readlines()

def findRename(str):
    a = int(str.split(',')[0].split('-')[0])
    b = int(str.split(',')[0].split('-')[1])
    c = int(str.split(',')[1].split('-')[0])
    d = int(str.split(',')[1].split('-')[1])
    return c >= a and c <= b or d >= a and d <= b or a >= c and a <=d or b >= c and b <=d
sum = 0
for line in list:
    if findRename(line):
        sum = sum + 1
print(sum)