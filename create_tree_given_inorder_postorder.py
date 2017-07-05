#creating tree using postorder and inorder
# 2 july 2017 1:46 am 

class node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def addleft (n1, n2):
    n2.left = n1
    
def addright(n1, n2):
    n1.right = n2

def preorder (n, res):
#     print "s :: %s"%s
    if(n == None):
        return
    
    res.append(n.val)
    preorder(n.left, res)
    preorder(n.right, res)

def build_tree(iarr, parr, findex, lindex , preindex ):
    if(lindex < findex):
        return None
    c = parr[preindex[0]]
    n = node(c)
    preindex[0] -= 1
    if findex == lindex:
        return n
    
    temp = findex
    while (iarr[temp] != c):
        temp += 1
    

    rightnode = build_tree(iarr, parr, temp + 1, lindex, preindex )
    leftnode  = build_tree(iarr, parr, findex, temp-1 , preindex)
    addleft(leftnode, n)
    addright(n, rightnode)
    return n

io =  [4, 8, 2, 5, 1, 6, 3, 7]
po =  [8, 4, 5, 2, 6, 7, 3, 1]
tree= build_tree(io, po, 0, len(io)-1 , [len(io)-1])
res = []
preorder(tree, res)
concat_arr = reduce(lambda x, y : str(x) + " " + str(y), res )
print concat_arr
# print res
# def create_tree()