def rvrs(s):
    res = []
    for i in s:
        res.append(i)
    for j in range(len(res) - 1, -1, -1):
        print(res[j], end = ' ')

s = input().split()
rvrs(s)