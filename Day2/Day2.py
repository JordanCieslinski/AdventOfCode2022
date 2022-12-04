file = open('./input.txt', 'r')

list = file.readlines()

# A = Rock
# B = Paper
# C = Scissors


#Rock beats Scissors
#1 / 3
#Paper beats rock
# 2 / 1
#Scissors beats paper
# 3 / 2


# X = Rock - 1
# Y = Paper - 2
# Z = Scissors - 3


# X = lose
# Y = Draw
# Z = Win

Dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
losses = {1 : 3, 2 : 1, 3 : 2}
wins = {3 : 1, 1 : 2, 2 : 3}

def findWhatToAdd(elf, you):
    if you == 'X':
        return losses[Dict[elf]]
    elif you == 'Y':
        return 3 + Dict[elf]
    elif you == 'Z':
        return 6 + wins[Dict[elf]]

elf = ''
you = ''
points = 0
for line in list:
    elf = line.split()[0]
    you = line.split()[1]
    points = points + findWhatToAdd(elf, you)
print(points)