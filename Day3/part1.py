file = open('input.txt', 'r')
list = file.readlines()

def findSimilar(rucksack):
    firstComp = rucksack[0:len(rucksack) // 2]
    secondComp = rucksack[len(rucksack) // 2:]
    for i in firstComp:
        if secondComp.find(i) != -1:
            return i
sum = 0
for line in list:
    sim = findSimilar(line)
    subtract = 0
    if sim.isupper():
        subtract = 38
    else:
        subtract = 96
    sum = sum + ord(sim) - subtract
print(sum)