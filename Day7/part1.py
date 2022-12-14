from treelib import Node, Tree

file = open('./test.txt', 'r')
list = file.readlines()

# Takes in input from file, then determines which
# kind of node that it is and returns a list with size and name
def parseInp(str):
    if str[0:3] == 'dir':
        # size will be 0 in this case b/c dir have 0 size
        return [str[4:], 0]
    else:
        ls = str.split()
        ls.reverse()
        return ls
def find_id(cd, tag):
    for i in tree.children(cd):
        if str(i.tag) == tag:
            return i.identifier
    return cd

tree = Tree()
tree.create_node('/')
cd = tree.root

for x in list:
    line = x.strip()
    if line[0:4] == '$ cd':
        if line[5:] == '..':
            cd = tree[cd].bpointer
        else:
            cd = find_id(cd, line[5:])
    elif line[0:1] != '$':
        temp = parseInp(line)
        tree.create_node(temp[0], parent = cd, data = temp[1])
        # ! need to store size somehow - there is a data value after parent = cd , data)
tree.show()