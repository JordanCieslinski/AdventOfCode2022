file = open('./test.txt', 'r')
list = file.readlines()

class node:
    def __init__(self, data, size, children = []):
        self.data = data
        self.size = size
        self.children = children
    def __str__(self, level=0):
        st = '\t'*level+repr(self.data)+' '+str(self.size)+'\n'
        for child in self.children:
            st += child.__str__(level+1)
        return st


# Need to first split up each chunk of ls btw cds, then get to the directory and use recursion to load in each node
# Eventually will need to computer total storage

root = node('/', 0)
root.children = []
curDir = None
for i in range(2, len(list)):
    if list[i][0:4] == '$ cd':
        break
    if list[i][0:3] == 'dir':
        root.children.append(node(list[i][4:len(list[i])-1], 0))
    else:
        st = list[i].split()
        root.children.append(node(st[1], st[0]))
print(root)