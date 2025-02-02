def histo(a):
    res=[]
    for i in a:
        res.append('*'*i)
    return res
a=list(map(int,input().split()))
print(*histo(a), sep='\n')