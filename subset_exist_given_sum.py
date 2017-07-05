# subset sum problem -> does subset exitst for given sum 1 july 2017 8:31 Pm
#sort -> in place, sorted => create a new list and copies

def isSubsetRecursive(arr, n, s):
    if (n == 0):
        if s == 0:
            return True
        else:
            return False
        
    else:
        if arr[n] > s :
            return isSubsetRecursive(arr, n-1 , s)
        else:
            return isSubsetRecursive(arr, n-1, s) | isSubsetRecursive(arr, n-1, s - arr[n])

def is_subset_memoize(arr, n, s, m):
    if m[s][n] != None:
        return m[s][n]
    else:
        if arr[n] > s :
            m[s][n] = is_subset_memoize(arr, n-1, s, m)
        else:
            m[s][n] = is_subset_memoize(arr, n-1, s, m) | is_subset_memoize(arr, n-1 , s - arr[n], m)
    return m[s][n]
        
    
with open("input.txt") as f :
    vals = f.readlines()
    vals = [x.strip() for x in vals]
    it = iter(vals)
    t = int(next(it))
    for i in range(t):
        n = int(next(it))
        arr = [int(x) for x in next(it).split()]
        s = sum(arr)
        if (s % 2 == 1):
            print ("NO")
        else:
            s = s/2
            m = [[None for j in range(n)] for i in range(s + 1)]
            for i in range(n):
                m[0][i] = 1
            for i in range(1, s+1):
                m[i][0] = 0

            if is_subset_memoize(arr, len(arr)-1, s, m):
                print "YES"
            else:
                print "NO"