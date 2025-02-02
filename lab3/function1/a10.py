def uniq(a):
    res=[]
    for i in a:
        if i not in res:
            res.append(i)
    return res
a=list(map(int,input().split()))
print(*uniq(a))