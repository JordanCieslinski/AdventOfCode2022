from treelib import Node, Tree
#https://treelib.readthedocs.io/en/latest/treelib.html#module-treelib.tree

file = open('./input.txt', 'r')
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
tree.create_node('/', data = 0)
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

cd = tree.root

total_sum = 0
def iterate_dir(d, r):
    dir = d.identifier
    sum = 0
    global total_sum
    # print(d.tag)
    for i in tree.children(dir):
        if i.data == 0:
            # print('s')
            # print(sum)
            sum+=iterate_dir(i, True)
        elif i.data != 0:
            sum+= int(i.data)    
    tree[dir].data = sum 
    if sum <= 100000:
        total_sum+=sum
    if r == True:
        return sum
iterate_dir(tree[tree.root], False)
# tree.show()
print(total_sum)


