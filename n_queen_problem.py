# n queen problem --> backtracking
# 2 july 2017 6:15 pm 
from functools import reduce
from sys import stdin, stdout
res_string = ""
class position:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col

def rback(positions, row, n, all_res):
    if row == n:
        s = "["
        for i in  range(len(positions)):
            s +=  str(positions[i].col + 1) + " "
        all_res.append (s[:-1] + "]")
        return True
    col = -1
    not_pos_found = False
    for col in range(n):
        find_pos = True
        i = 0
        for i in range(0, row):
            pos = positions[i]
            if (pos.col == col) | (pos.row + pos.col == row + col) | (pos.row - pos.col == row - col):
                find_pos = False
                break
    
        if (find_pos == True):
            positions[row] = (position(row, col))
            if(rback(positions, row + 1, n, all_res)):
                not_pos_found = True

    return not_pos_found
        
def findsqn(n, all_res):
    positions = [None for i in range(n)]
    rback(positions, 0, n, all_res)

t = int(stdin.readline())
while(t):
    n = int(stdin.readline())
    all_res = []
    findsqn(n, all_res)
    cstr = reduce(lambda x, y : str(x) + " " + str(y) , all_res)
    t -=1 