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

root = node('/', 0)
root.children = []
curDir = None
for line in list:
    if line[0:4] == '$ cd':
        print()