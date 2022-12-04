file = open('input.txt', 'r')

list = file.readlines()
cals = []
cal = 0

for line in list:
    if line != '\n':
        cal = cal + int(line)
    else:
        cals.append(cal)
        cal = 0
total = 0
print('Part 1: '+str(max(cals)))
for i in range(3):
    total = total + int(max(cals))
    cals.remove(max(cals))
print('Part 2: '+str(total))
file.close()