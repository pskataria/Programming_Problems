# print YES if Bracket sequence is complete else NO
#stack problem

def  braces(values):
    arr_size = len(values)
    res_arr = []
    dic = {}
    dic["}"] = "{"
    dic[")"] = "("
    dic["]"] = "["
    for i in range(arr_size):
        string = values[i]
        str_size = len(string)
        if(str_size%2 !=0 ):
            res_arr.append("NO")
            
        else:
            stack_arr = string[0]
            for j in range(1, str_size):
                if (string[j]=="{") | (string[j]=="[") | (string[j]=="("):
                    stack_arr += string[j]
                else:
                    if (stack_arr[len(stack_arr)-1] == dic.get(string[j])):
                        stack_arr = stack_arr[0:len(stack_arr)-1]
                    else:
                        res_arr.append("NO")
                        break
            if(stack_arr== ""):
                res_arr.append('YES')
        return res_arr
print braces(["{}{}[]()"])