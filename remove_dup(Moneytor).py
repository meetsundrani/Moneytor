def re_dup(arr):
    single=[]
    for i in arr:
        if i not in single:
            single.append(i)
    return single

arr=list(input())
print(re_dup(arr))