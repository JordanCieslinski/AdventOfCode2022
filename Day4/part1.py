file = open('input.txt', 'r')
list = file.readlines()

def contain(str):
    a = int(str.split(',')[0].split('-')[0])
    b = int(str.split(',')[0].split('-')[1])
    c = int(str.split(',')[1].split('-')[0])
    d = int(str.split(',')[1].split('-')[1])
    return a <= c and b >= d or a >= c and b <= d
sum = 0
for line in list:
    if contain(line):
        sum = sum + 1
print(sum)