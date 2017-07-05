#second most frequent 1st july 2017 8:14 pm
arr = [ "ccc", "aaa", "ccc", "ddd", "aaa", "aaa" ]
dic = {}
for word in arr:
    if dic.has_key(word):
        dic[word] += 1
    else:
        dic[word] = 1
        
print dic

fmax = -2
smax = -2
res = ""
sres = ""
for item in dic:
    if dic[item] > fmax:
        smax = fmax
        sres = res
        res = item
        fmax = dic[item]
    elif  smax < dic[item] < fmax:
        smax = dic[item]
        sres = item
print smax
print sres