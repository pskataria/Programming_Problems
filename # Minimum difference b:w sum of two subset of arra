# Minimum difference b/w sum of two subset of array
# minimum subset problem 3july 2017 10:44

def getmin(arr):
    size = len(arr)
    total = sum(arr)
    boolarr = [[False for j in range(total+1)] for i in range(size+1)]
    for i in range(0, size+1):
        boolarr[i][0] = True
    for i in range(1, size + 1):
        for j in range(1, total + 1):
            boolarr[i][j] = boolarr[i-1][j]
            if arr[i-1] <= j:
#                 print "i :: %i , j-arr[i-1] :: %i " %(i, j-arr[i-1])
                boolarr[i][j] =  boolarr[i][j] | (boolarr[i-1][j-arr[i-1]])
            
    j = total/2
    while(j > 0):
        if(boolarr[size][j] == True):
            print (total - 2 * j)
            break
        j = j-1

string = "37 28 16 44 36 37 43 50 22 13 28 41 10 14 27 41 27 23 37 12 19 18 30 33 31 13 24 18 36 30 3 23 9 20"
getmin([int(x) for x in string.split()])