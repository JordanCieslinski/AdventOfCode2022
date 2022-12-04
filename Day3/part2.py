file = open('input.txt', 'r')
list = file.readlines()

def findSimilar(first, second, third):
    commonChar = ''
    for i in first:
        if second.find(i) != -1 and third.find(i) != -1:
            return i

sum = 0
for i in range(2, len(list)+1 , 3):
    sim = findSimilar(list[i-2], list[i-1], list[i]) 
    subtract = 96
    if sim.isupper():
        subtract = 38
    sum = sum + ord(sim) - subtract
print(sum)