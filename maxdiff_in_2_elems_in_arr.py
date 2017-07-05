# max of j-i problem , 2 july 2017 1:30 am
#given a[j] >= a[i]
from sys import stdin, stdout
def max_index(arr):
    size = len(arr)
    m = [[0 for j in range(size)] for i in range(size)]
    md = 0
    for i in range(size):
        for j in range(i, size):
            if arr[j] >= arr[i]:
#                     m[i][j] = j-i
                if (j-i) > md:
                    md = (j-i)
    return md

t = int(stdin.readline())
while t:
    arrlen = stdin.readline()
    arr = list(map(int, (stdin.readline()).split()))
    print max_index(arr)
    t -= 1
# arr = [3, 5, 4, 2]
# print max_index(arr)